from django.http import HttpResponse

from django.shortcuts import render


def heading(request, heading):
    context = {"heading": heading}
    return render(request, "tariffs/heading.html", context)
