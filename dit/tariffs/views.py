from django.http import HttpResponse
from django.template import loader


from .view_model import make_static_example


def index(request, heading):

    view_model = make_static_example(heading)

    template = loader.get_template('tariffs/landingpage.html')
    return HttpResponse(template.render(view_model.data, request))
