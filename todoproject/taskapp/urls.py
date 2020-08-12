
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('',v.index,name="list"),
    path('update/<str:pk>/',v.updatetask,name="update"),
    path('delete/<str:pk>/',v.deletetask,name="delete"),
]
