from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [

    path("", views.rexsite, name="rexsite"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("reserve/", views.reserve, name="reserve")

]