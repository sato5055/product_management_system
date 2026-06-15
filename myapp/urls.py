from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index),
    path('searchResult/', views.show_search),
    path('login/', views.login),
    path('registerUser/', views.registerUser),
    path('registerUserConfirm/', views.registerUserConfirm),
    path('registerUserCommit/', views.registerUserCommit)
]