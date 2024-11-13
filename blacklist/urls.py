from django.urls import path, re_path
from . import views

urlpatterns = [
    path('blacklist/', views.black_list, name='black_list'),  # Blacklist of IP
    path('blacklist/add/', views.ip_add, name='ip_add'),  # Add Blacklist of IP
    re_path(r'^blacklist/del/(?P<pk>\d+)/$', views.ip_del, name='ip_del'),  # Delete IP based on pk
]