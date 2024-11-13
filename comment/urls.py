from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^comment/add/news/(?P<pk>\d+)/$', views.news_cm_add, name='news_cm_add'),
    path('comments/list/', views.comments_list, name='comments_list'),  # Comments list in Panel
    re_path(r'^comments/del/(?P<pk>\d+)/$', views.comments_del, name='comments_del'),  # Comments delete in Panel
    re_path(r'^comments/confirm/(?P<pk>\d+)/$', views.comments_confirm, name='comments_confirm'),  # Comments Confirm in Panel
]