from django.urls import path
from . import views

app_name='calc'
urlpatterns = [
    path("homepage/", views.homepage, name='homepage'),
    path("homepage/operate/", views.operate, name='operate'),
    path("register/", views.register, name='register'),
    path("", views.login_request, name='login_request'),
    path("logout/", views.logout_request, name="logout_request"),
]
