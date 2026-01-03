# from django.urls import path
# from .views import index, Companyreg
# from .adminviews import Userdata

# urlpatterns=[
#     path('',index,name='index'),
#     path('Userdata/',Userdata,name="Userdata"),
#     path('Companyreg/',Companyreg,name='Companyreg'),

# ]

# placementapp/urls.py

from django.urls import path
from .views import index, Companyreg
from .adminviews import Userdata

urlpatterns = [
    path('', index, name='index'),
    path('Userdata/', Userdata, name='Userdata'),
    path('Companyreg/', Companyreg, name='Companyreg'),
]
