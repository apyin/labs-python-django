from django.contrib import admin
from django.urls import path
from articles import models
from articles import views
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    re_path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article'),
]
