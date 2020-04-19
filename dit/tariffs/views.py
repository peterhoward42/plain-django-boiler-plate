from django.http import HttpResponse
from django.template import loader

from .view_model import ViewModel
from .models import heading_validator


def index(request, heading):

    view_model = ViewModel(heading)

    template = loader.get_template('tariffs/landingpage.html')
    return HttpResponse(template.render(view_model.data, request))
