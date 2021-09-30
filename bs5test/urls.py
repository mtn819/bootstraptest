from django.urls import path
from . import views

app_name = "bs5test"
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
]