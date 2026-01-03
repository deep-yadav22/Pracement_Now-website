# from django.shortcuts import render,redirect

# from .models import UserRegistration , CompanyRegistration

# def Userdata(request):
#     Data = UserRegistration.objects.all()

#     return render(request,'adminuserviews.html',{"Data":Data})
# placementapp/adminviews.py

from django.shortcuts import render
from .models import UserRegistration

def Userdata(request):
    data = UserRegistration.objects.all()
    return render(request, 'adminuserviews.html', {"Data": data})
