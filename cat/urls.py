from django.urls import path, re_path
from . import views

urlpatterns = [
    path('panel/category/list/', views.cat_list, name='cat_list'),  # For Admin Panel Category List
    path('panel/category/add/', views.cat_add, name='cat_add'),    # For Admin Panel Category Add
    path('export/cat/csv/', views.export_cat_csv, name='export_cat_csv'),  # To download/export csv file
    path('import/cat/csv/', views.import_cat_csv, name='import_cat_csv'),  # To import csv file
]