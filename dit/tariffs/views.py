from django.shortcuts import render

from .view_model import ViewModel


def index(request, heading):
    view_model = ViewModel(heading)
    return render(request, "tariffs/heading.html", view_model.data)
