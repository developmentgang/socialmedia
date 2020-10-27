from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from Home import views

admin.site.site_header = "Friend Finder"
admin.site.site_title = "Friend Finder Admin Portal"
admin.site.index_title = "Welcome to Friend Finder Admin panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('Home.urls')),
    path('',include('login.urls')),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
