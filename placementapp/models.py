from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    resume = models.FileField(upload_to='resumes/')
    photo = models.ImageField(upload_to='photos/')
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=50)

class CompanyRegistration(models.Model):
    namecompany = models.CharField(max_length=50)
    gstid = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    companytype = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/')


