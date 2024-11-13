from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import path

urlpatterns = [
    
    path('admin/' , admin.site.urls),      # Django Default Admin Panel
    path('', include('main.urls')),         # here main is an app name
    path('', include('news.urls')),         # here news is an app name
    path('', include('cat.urls')),          # here cat is an app name
    path('', include('subcat.urls')),       # here subcat is an app name
    path('', include('contactform.urls')),       # here contactform is an app name
    path('', include('trending.urls')),       # here trending is an app name
    path('', include('manager.urls')),       # here manager is an app name
    path('', include('newsletter.urls')),       # here newsletter is an app name
    path('', include('comment.urls')),       # here comment is an app name
    path('', include('blacklist.urls')),       # here blacklist is an app name (for IP)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)