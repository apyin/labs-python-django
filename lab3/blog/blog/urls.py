from django.contrib import admin
from django.urls import path
from articles import models
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive')
]
