from bs4 import BeautifulSoup
import requests
import re
import MySQLdb

# 读取每一个网页25个电影信息


def info25(movie):
    movieData = []
    for i in range(0, 25):
        ranking = movie[i].find('em').string  # 获得排名
        img = movie[i].find('img', attrs={'src': True}).attrs['src']  # 获得图片网址
        title = movie[i].find('span', class_="title").string  # 获得影片名称
        information = movie[i].find('div', class_="bd").find('p').text

        # 分离导演、主演、上映日期、上映地点、电影类型的方法
        patten = re.compile('导演:(.*?)\\xa0')
        director = ''.join(patten.findall(''.join(information)))
        director = str(director).replace("'","''")
        patten = re.compile('主演:(.*?)\n')
        star = ''.join(patten.findall(''.join(information))).replace("'","''")
        patten = re.compile('\n.*?(\d+)\\xa0')
        time = ''.join(patten.findall(''.join(information)))
        patten = re.compile('/\\xa0(.*?)\\xa0')
        adress = ''.join(patten.findall(''.join(information)))
        patten = re.compile('/\\xa0.*?\\xa0/\\xa0(.*?)\\n')
        movie_type = ''.join(patten.findall(''.join(information)))

        score = movie[i].find('span', class_="rating_num").string  # 获得影片评分
        number = movie[i].find('div', class_="star").find_all(
            'span')[-1].string.strip('人评价')  # 获得影片评价人数
        evaluate = movie[i].find('span', class_="inq")  # 获得影片短评

        if director is None:
            director = "暂无"
        if star is None:
            star = "暂无"
        if time is None:
            time = "暂无"
        if adress is None:
            adress = "暂无"
        if movie_type is None:
            movie_type = "暂无"
        if evaluate is None:
            evaluate = "暂无"
        else:
            evaluate=evaluate.string
        evaluate = str(evaluate).replace("'","''")
        
        movieData.append([ranking, img, title, director, star,
                          time, adress, movie_type, score, number, evaluate])
    return movieData


def parse_one_page():
    movieData250 = []
    for i in range(10):
        h = "https://movie.douban.com/top250?start=" + str(i*25) + "&filter="
        r = requests.get(h)
        r.encoding = 'utf-8'
        html = BeautifulSoup(r.text, "html.parser")
        movieList = html.find('ol', attrs={'class': "grid_view"})
        movie = movieList.find_all('li')  # 获取每一个li（每个li是一个电影），以数组方式
        movieData250 += info25(movie)
    return movieData250


def conns(movieData250):
    conn = MySQLdb.connect(host='localhost', user='root',
                           passwd='tiger', db='test1', charset='utf8')
    cur = conn.cursor()
    for list3 in movieData250:
        cur.execute("insert into yrb_douban (myranking,myimg,mytitle,mydirector,mystar,mytime,myadress,mymovie_type,myscore,mynumber,myevaluate) values ('%s','%s',\
                    '%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (list3[0], list3[1], list3[2], list3[3], list3[4], list3[5], list3[6], list3[7], list3[8], list3[9], list3[10]))
    cur.close()
    conn.commit()
    conn.close()


def main():
    movieData250 = parse_one_page()
    conns(movieData250)

if __name__ == "__main__":
    main()
