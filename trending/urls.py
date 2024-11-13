from django.urls import path, re_path
from . import views

urlpatterns = [
    path('panel/trending/', views.trending_add, name='trending_add'),  # Admin Panel Trending Add   
    re_path(r'^panel/trending/del/(?P<pk>\d+)/$', views.trending_del, name='trending_del'),  # Admin Panel Delete Trending 
    re_path(r'^panel/trending/edit/(?P<pk>\d+)/$', views.trending_edit, name='trending_edit'),  # Admin Panel Edit Trending 
]