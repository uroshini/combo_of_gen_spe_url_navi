from django.urls import path
from specific.views import *
app_name='something'
urlpatterns=[
    path('ishu/',ishu,name='ishu'),
    path('sravani/',sravani,name='sravani'),
]