from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('user/create/', views.user_create, name="user_create"),
]