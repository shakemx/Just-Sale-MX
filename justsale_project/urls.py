"""justsale_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from os import environ
from home.sitemaps import StaticViewSitemap

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if environ['DEBUG'] == 'True' else False
sitemaps = {
    'static': StaticViewSitemap,
}

if DEBUG:
    urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')), 
    path('admin', admin.site.urls),
    path('', include('home.urls')),
    path('shake/',include('app_news.urls')), 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
] 
        
else:
    urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('home.urls')),
    path('shake/',include('app_news.urls')), 
     # SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
] 


