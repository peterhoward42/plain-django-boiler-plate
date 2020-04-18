from django.http import HttpResponse

from django.shortcuts import render


def index(request, heading):
    context = {'heading': heading}
    return render(request, 'tariffs/index.html', context)
