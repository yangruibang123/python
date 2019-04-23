from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('b.html', views.my_douban, name='my_douban'),
    path('c.html', views.my_jindong, name='my_jindong'),
]