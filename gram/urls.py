from django.conf.urls import url
from . import views

#Create your Urls here
urlpatterns=[
    url('^$',views.welcome,name = 'welcome')
]