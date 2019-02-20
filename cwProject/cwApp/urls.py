from django.urls import path
from . import views  #from cwApp

urlpatterns = [
    path('',views.index,name='index'),    #index
]