from django.urls import path
from flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # Сделайте так, чтобы по адресу http://127.0.0.1:8000/hello/ возвращался тот же самый текст
    path('hello/', views.home, name='home')
]
