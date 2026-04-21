from django.urls import path 
from .views import Register , Login , Logout , Home , BookCreate, BookUpdate ,BookDelete
urlpatterns = [
    path("register/", Register, name="register"),
    path("login/", Login , name ="login"),
    path("logout/", Logout , name ="logout"),
    path("", Home, name= "home" ),
    path("create-book/" , BookCreate , name = "create-book" ),
    path("update-book/<int:b_id>/" , BookUpdate , name= "update-book"),
    path("delete-book/<int:b_id>/" , BookDelete , name= "delete-book")
]