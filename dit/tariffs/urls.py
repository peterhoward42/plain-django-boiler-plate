from django.urls import path

from . import views

urlpatterns = [
    path('<heading>', views.index, name='index'),
]
