import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
import MySQLdb

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 50)


def search(jingDonData):
    browser.get('https://www.jd.com/')
    try:
        input = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#key"))
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#search > div > div.form > button"))
        )

        input[0].send_keys('python')
        submit.click()

        total = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')
            )
        )
        html = browser.page_source
        jingDonData += prase_html(html)
        return total[0].text
    except TimeoutError:
        search(jingDonData)


def next_page(page_number, jingDonData):
    try:
        # 滑动到底部，加载出后三十个货物信息
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    # 翻页动作
        button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next > em'))
        )
        button.click()
        wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#J_goodsList > ul > li:nth-child(60)"))
        )
    # 判断翻页成功
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"), str(page_number))
        )
        html = browser.page_source
        jingDonData += prase_html(html)
    except TimeoutError:
        return next_page(page_number, jingDonData)


def prase_html(html):
    data = []
    html = etree.HTML(html)
    items = html.xpath('//li[@class="gl-item"]')
    for i in range(len(items)):

        if html.xpath('//div[@class="p-img"]//img')[i].get('data-lazy-img') != "done":
            img = html.xpath('//div[@class="p-img"]//img')[i].get('data-lazy-img')
        else:
            img = html.xpath('//div[@class="p-img"]//img')[i].get('src')
        title = html.xpath('//div[@class="p-name"]//em')[i].xpath('string(.)')
        price = html.xpath('//div[@class="p-price"]//i')[i].text

        if price is None:
            price="0"

        commit = html.xpath('//div[@class="p-commit"]//a')[i].text

        title=str(title).replace("'","''")
        data.append([img,title, price, commit])
    return data


def conns(jingDonData):
    conn = MySQLdb.connect(host='localhost', user='root',
                           passwd='tiger', db='test1', charset='utf8')
    cur = conn.cursor()
    for list3 in jingDonData:
        cur.execute("insert into yrb_jingdon (img,title,price,commit) \
            values ('%s','%s','%s','%s')" % (list3[0], list3[1], list3[2], list3[3]))
    cur.close()
    conn.commit()
    conn.close()

def main():
    jingDonData=[]
    total=int(search(jingDonData))#得到页数
    for i in range(2, total+1):
            time.sleep(1)
            next_page(i, jingDonData)
    conns(jingDonData)

if __name__ == "__main__":
    main()
