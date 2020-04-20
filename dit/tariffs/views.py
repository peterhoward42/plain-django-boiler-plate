import logging

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader

from .biz_logic.govuk_loader import GovUKLoader
from .models import heading_regex, Heading
from .view_model import make_static_example

logger = logging.getLogger(__name__)

def index(request, heading):

    # Make sure request provides a 4 digit heading.
    if heading_regex.search(heading) is None:
        return HttpResponseBadRequest(
            f"The requested heading must be 4 digits: ({heading_digits})"
        )

    if _heading_unknown_to_database(heading):
        logger.info(f'Heading unknown: <{heading}, so fetching it now from GovUK API')
        heading_loader = GovUKLoader(heading=heading)
        heading_loader.load_heading_from_govuk_api_call()

    view_model = make_static_example(heading)
    template = loader.get_template("tariffs/landingpage.html")
    return HttpResponse(template.render(view_model.data, request))


def _heading_unknown_to_database(heading_digits: str) -> bool:
    exists = Heading.objects.filter(heading_digits=heading_digits).exists()
    return not exists
