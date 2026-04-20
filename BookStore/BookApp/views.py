from django.shortcuts import render , redirect
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Register(request):   
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "BookApp/register.html", context)