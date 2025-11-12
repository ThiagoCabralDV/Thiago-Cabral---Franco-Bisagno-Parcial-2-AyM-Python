from django.urls import path
from .views import registro, login_view, logout_view

urlpatterns = [
    path("register/", registro, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
