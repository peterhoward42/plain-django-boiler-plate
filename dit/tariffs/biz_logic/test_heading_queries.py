import datetime

import pytest

from .heading_queries import HeadingQueries
from ..models import Heading


@pytest.mark.django_db
def test_is_in_database_false():
    hq = HeadingQueries("no such heading")
    assert hq.is_in_database() is False


@pytest.mark.django_db
def test_is_in_database_true():
    _HEADING = "some heading"
    heading = Heading(heading_digits=_HEADING, last_updated=datetime.datetime.now())
    heading.save()

    hq = HeadingQueries(_HEADING)
    assert hq.is_in_database() is True
