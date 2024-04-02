from django.contrib import admin
from django.urls import path, include
from .views import index, registration_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", index, name="index"),
    path("accounts/register/", registration_view, name="register")
] 
