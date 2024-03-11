from django.contrib import admin
from django.urls import path, include
from list.views import index

urlpatterns =[
    path("", index, name="index")
]