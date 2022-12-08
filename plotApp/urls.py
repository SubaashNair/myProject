from django.urls import path
from .views import DashBoard

urlpatterns = [
    path("", DashBoard, name="DashBoard"),
]
