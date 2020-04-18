from django.http import HttpResponse

from django.shortcuts import render

from .view_model import ViewModel


def heading(request, heading):
    context = {"heading": heading}
    view_model = ViewModel(heading)
    return render(request, "tariffs/heading.html", view_model.data)
