from django.shortcuts import render , redirect
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout , authenticate
# Create your views here.

def Register(request):   
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "BookApp/register.html", context)


def Home(request):
    return render(request, "BookApp/home.html")


def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # True , False
        user = authenticate(request , username = username , password = password)
        
        if user :
            login(request,user)
            return redirect("home")
        
        else:
            raise ValueError("Invalid data")
    return render(request, "BookApp/login.html")


def Logout(request):

    logout(request)
    return redirect("login")



   









