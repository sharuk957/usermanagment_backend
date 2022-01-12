from os import name
from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path,include


router = SimpleRouter()
router.register('accounts', views.UserManagmentView, basename="accounts")

urlpatterns = [
    path('',include(router.urls)),
    path('login',views.LoginView.as_view(),name="login"),
    path('registration/',views.UserRegistrationView.as_view(),name="registration"),

]
