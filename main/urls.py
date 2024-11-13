from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name='home'),                        ## Front Home Page
    path('about/', views.about, name='about'),                ## Front About Page
    path('panel/', views.panel, name='panel'),                ## Admin Panel Home Page
    path('login/', views.mylogin, name='mylogin'),            ## Front Login Page
    path('register/', views.myregister, name='myregister'),    ## Front Register Page
    path('logout/', views.mylogout, name='mylogout'),         ## Front Logoout Page
    path('panel/setting/', views.site_setting, name='site_setting'),  ## Admin Panel Settings
    path('panel/about/setting/', views.about_setting, name='about_setting'),  ## This is for about(about seeting) in admin panel
    path('contact/', views.contact, name='contact'),          ## Front Contact Pages
    path('panel/change/pass/', views.change_pass, name='change_pass'),  ## Password Change (By clicking setting button in admin pannel)
]