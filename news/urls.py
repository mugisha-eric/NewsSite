from django.urls import path, re_path
from . import views

urlpatterns = [
    path('news/<str:word>/', views.news_detail, name='news_detail'),       # Front News Details Page   
    path('panel/news/list/', views.news_list, name='news_list'),          # Admin Panel News List
    path('panel/news/add/', views.news_add, name='news_add'),            # Admin Panel Add News      
    re_path(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),  # Admin Panel Delete News
    re_path(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),    # Admin Panel Edit News
    re_path(r'^panel/news/publish/(?P<pk>\d+)/$', views.news_publish, name='news_publish'),  # Admin Panel Publish News   
    re_path(r'^urls/(?P<pk>\d+)/$', views.news_detail_short, name='news_detail_short'),  # Front News Short Url  
]