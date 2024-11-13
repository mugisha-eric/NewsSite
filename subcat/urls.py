from django.urls import path
from . import views

urlpatterns = [
    path('panel/subcategory/list/', views.subcat_list, name='subcat_list'),  # Admin Panel Subcategory List
    path('panel/subcategory/add/', views.subcat_add, name='subcat_add'),    # Admin Panel Add Subcategory
]