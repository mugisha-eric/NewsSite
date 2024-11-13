from django.contrib import admin
from .models import Main, Members
from django.contrib.auth.models import Permission ## To give user permission

# Register your models here.
admin.site.register(Members)
admin.site.register(Main)
admin.site.register(Permission)  ## To give user permission and register it on admin area