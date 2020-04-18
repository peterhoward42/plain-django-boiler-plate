from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    context = {'foo': "bar"}
    return render(request, 'tariffs/index.html', context)
