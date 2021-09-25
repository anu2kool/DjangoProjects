from django.urls import path
from . import views
urlpatterns = [
    path("",views.home, name='home'),
    path("content/<str:pk>/", views.content, name="content"),
    path("register/", views.register, name="register"),
    path("login_request/", views.login_request, name="login_request"),
    path("logout_request/", views.logout_request, name="logout_request"),
]
