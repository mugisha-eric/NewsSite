from django.urls import path, re_path
from . import views

urlpatterns = [
    path('newsletter/add/', views.news_letter, name='news_letter'),
    path('panel/newsletter/emails/', views.news_emails, name='news_emails'),
    path('panel/newsletter/phones/', views.news_phones, name='news_phones'),
    re_path(r'^panel/newsletter/del/(?P<pk>\d+)/(?P<num>\d+)/$', views.news_txt_del, name='news_txt_del'),
]