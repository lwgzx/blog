import django.conf.urls
from . import views

app_name = 'blog'

urlpatterns = [
    django.conf.urls.url(r'^$', views.index, name='blog_index'),
    django.conf.urls.url(r'^$', views.index, name='blog_index'),
]
