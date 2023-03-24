from django.urls import path
from main import views

app_name = "cisowianka"

urlpatterns = [
    path("", views.main, name="main"),
]
