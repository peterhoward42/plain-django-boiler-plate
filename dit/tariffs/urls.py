from django.urls import path

from . import views

urlpatterns = [
    path("<heading>", views.index, name="index"),
    path("<heading>/<reload>", views.index, name="index"),
]
