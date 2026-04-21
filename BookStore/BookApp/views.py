from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

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
    return redirect("home")


def Home(request):
    books = Book.objects.all()
    context = {"books":books}
    return render(request, "BookApp/home.html" , context)



@login_required(login_url="login")
def BookCreate(request):

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect("home")

    else:
        form = BookForm()
    context = {"form":form}
    return render(request , "BookApp/book_create.html" , context )


@login_required(login_url="login")
def UpdateBook(request , b_id):

    book = Book.objects.get(id = b_id)
    if request.method == "POST":
        form = BookForm(request.POST , instance=book)
        
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect("home")
    else:
        form = BookForm(instance=book)

    context = {"form": form , "book": book}
    return render(request, "BookApp/book_update.html", context)


