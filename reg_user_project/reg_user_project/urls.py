from django.contrib import admin
from django.urls import path
from app_reg_users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', views.create_user, name='create_user'),
]
