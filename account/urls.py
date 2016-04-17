'''
Created on 17 de abr. de 2016

@author: alvar
'''
from django.conf.urls import url
from . import views

urlpatterns = [
       # post views
       url(r'^login/$', views.user_login, name='login'),
]