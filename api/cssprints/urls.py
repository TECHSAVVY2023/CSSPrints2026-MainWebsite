from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register),
    path("get-users/", views.get_all_users)
]