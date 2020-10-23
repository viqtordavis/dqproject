from django.urls import path
from . import views

urlpatterns = [
    path("login",views.loginview.as_view(),name="login"),
    path("logout",views.logout,name="logout"),
]