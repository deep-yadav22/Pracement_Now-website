from django.contrib import admin

from .models import UserRegistration , CompanyRegistration

admin.site.register(UserRegistration)
admin.site.register(CompanyRegistration)
