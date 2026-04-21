from django.urls import path 
from .views import Register , Login , Logout , Home , BookCreate, UpdateBook
urlpatterns = [
    path("register/", Register, name="register"),
    path("login/", Login , name ="login"),
    path("logout/", Logout , name ="logout"),
    path("", Home, name= "home" ),
    path("create-book/" , BookCreate , name = "create-book" ),
    path("update-book/<int:b_id>/" , UpdateBook , name= "update-book")
]