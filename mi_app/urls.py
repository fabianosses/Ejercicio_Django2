from .views import home, test
from django.urls import path

urlpatterns = [
    path("home/", home, name="home"),
    path("test/<str:variable>/", test, name="test"),
]