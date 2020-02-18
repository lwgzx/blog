"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.bin.website.blog.models import Entry

import blog

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modifyed_time'
}

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
      name='django.contrib.sitemaps.views.sitemap'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error