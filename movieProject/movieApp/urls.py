from django.urls import path
from movieApp import views

app_name='movieApp'
urlpatterns = [
    path('', views.index,name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/<int:movie_id>/',views.add_movie,name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add/',views.add_amovie,name='add_amovie'),
]