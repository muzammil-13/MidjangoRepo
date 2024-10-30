from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo,name="demo"),
    #path('/index/',views.index,name="index"),
    #path('/about/',views.about,name="about"),
]