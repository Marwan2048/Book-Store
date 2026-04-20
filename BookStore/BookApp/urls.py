from django.urls import path 
from .views import Register , Login , Logout , Home
urlpatterns = [
    path("register/", Register, name="register"),
    path("login/", Login , name ="login"),
    path("logout/", Logout , name ="logout"),
    path("", Home, name="home"),
]