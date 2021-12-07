from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path(
        "", include("django.contrib.auth.urls")
    ),  # we will use django's premade/bulit in user authentication system
    path("register/", views.register, name="register"),
]
