from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader

from .models import heading_regex
from .view_model import make_static_example


def index(request, heading):

    # Make sure request provides a 4 digit heading.
    if heading_regex.search(heading) is None:
        return HttpResponseBadRequest(
            f'The heading in the URL must be 4 digits: ({heading})')

    view_model = make_static_example(heading)
    template = loader.get_template('tariffs/landingpage.html')
    return HttpResponse(template.render(view_model.data, request))
