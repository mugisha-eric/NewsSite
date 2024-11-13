from django.urls import path, re_path
from . import views

urlpatterns = [
    path('panel/manager/list/', views.manager_list, name='manager_list'),  # Manager List in Admin Panel
    re_path(r'^panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),  # Delete Manager List in Admin Panel
    path('panel/manager/group/', views.manager_group, name='manager_group'),  # Manager Group in Admin Panel
    path('panel/manager/group/add/', views.manager_group_add, name='manager_group_add'),  # Add Manager Group in Admin Panel
    re_path(r'^panel/manager/group/del/(?P<name>.*)/$', views.manager_group_del, name='manager_group_del'),  # Delete Manager Group in Admin Panel
    re_path(r'^panel/manager/group/show/(?P<pk>\d+)/$', views.users_groups, name='users_groups'),  # Users Groups Show in Admin Panel
    re_path(r'^panel/manager/addtogroup/(?P<pk>\d+)/$', views.add_users_to_groups, name='add_users_to_groups'),  # Add Users To Groups in Admin Panel
    re_path(r'^panel/manager/delgroup/(?P<pk>\d+)/(?P<name>.*)/$', views.del_users_to_groups, name='del_users_to_groups'),  # Delete Users from Group in Admin Panel
    path('panel/manager/perms/', views.manager_perms, name='manager_perms'),  # Manager Permissions in Admin Panel
    re_path(r'^panel/manager/perms/del/(?P<name>.*)/$', views.manager_perms_del, name='manager_perms_del'),  # Delete Manager Permission in Admin Panel
    path('panel/manager/perms/add/', views.manager_perms_add, name='manager_perms_add'),  # Add Manager Permission in Admin Panel
    re_path(r'^panel/manager/perms/show/(?P<pk>\d+)/$', views.users_perms, name='users_perms'),  # Users Permissions Show in Admin Panel
    re_path(r'^panel/manager/delperm/(?P<pk>\d+)/(?P<name>.*)/$', views.users_perms_del, name='users_perms_del'),  # Delete Users permissions in Admin Panel
    re_path(r'^panel/manager/addperm/(?P<pk>\d+)/$', views.users_perms_add, name='users_perms_add'),  # Add Users permissions in Admin Panel
    re_path(r'^panel/manager/addpermtogroup/(?P<name>.*)/$', views.groups_perms, name='groups_perms'),  # Groups Permissions Show in Admin Panel
    re_path(r'^panel/manager/group/delperms/(?P<gname>.*)/(?P<name>.*)/$', views.groups_perms_del, name='groups_perms_del'),  # Delete Groups Permissions in Admin Panel
    re_path(r'^panel/manager/group/addperms/(?P<name>.*)/$', views.groups_perms_add, name='groups_perms_add'),  # Add Groups Permissions in Admin Panel
]