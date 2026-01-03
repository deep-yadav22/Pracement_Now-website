
from django.forms import ModelForm 
from .models import UserRegistration,CompanyRegistration

class UserRegistrationForm(ModelForm):
    class Meta:
        model= UserRegistration
        fields = '__all__'

class CompanyRegistrationForm(ModelForm):
    class Meta:
        model= CompanyRegistration
        fields = '__all__'
