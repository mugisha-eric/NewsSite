from django.urls import path, re_path
from .import views

urlpatterns = [
    
    path('contact/submit/', views.contact_add, name='contact_add'),  # when we click the send button, it will take me msgbox.html page
    path('panel/contactform/', views.contact_show, name='contact_show'),  # This is for admin panel
    re_path(r'^panel/contactform/del/(?P<pk>\d+)/$', views.contact_del, name='contact_del'),  ## Messages Delete in admin panel
]