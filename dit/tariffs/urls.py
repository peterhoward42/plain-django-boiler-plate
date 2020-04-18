from django.urls import path

from . import views

urlpatterns = [
    path("<heading>", views.heading, name="index"),
]
