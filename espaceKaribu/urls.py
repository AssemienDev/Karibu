"""
URL configuration for espaceKaribu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from utilisateur.sitemaps import StaticViewSitemap
from utilisateur import views

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    #path('admin/', admin.site.urls),

    path('admini/', include('administrateur.urls')),
    path('', include('utilisateur.urls')),

    path('', include('pwa.urls')),

    # URL pour le sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # URL pour robots.txt
    path('robots.txt', views.robots_txt),
]
