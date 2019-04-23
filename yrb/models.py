from django.db import models


class douban(models.Model):
    myranking = models.CharField(max_length=255)
    myimg = models.CharField(max_length=255)
    mytitle = models.CharField(max_length=255)
    mydirector = models.CharField(max_length=255)
    mystar = models.CharField(max_length=255)
    mytime = models.CharField(max_length=255)
    myadress = models.CharField(max_length=255)
    mymovie_type = models.CharField(max_length=255)
    myscore = models.CharField(max_length=255)
    mynumber = models.CharField(max_length=255)
    myevaluate = models.CharField(max_length=255)

class jingdon(models.Model):
    img = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    commit = models.CharField(max_length=255)


