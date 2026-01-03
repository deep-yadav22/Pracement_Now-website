from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, CompanyRegistrationForm

def index(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Userdata')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form})

def Companyreg(request):
    if request.method == "POST":
        form = CompanyRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Userdata')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'Companyreg.html', {"form": form})

def Userdata(request):
    return render(request, 'adminuserviews.html')  # ✅ Yeh template yahan lagega
