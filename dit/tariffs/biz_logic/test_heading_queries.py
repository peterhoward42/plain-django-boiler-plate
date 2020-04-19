import datetime

import pytest

from .heading_queries import HeadingQueries
from ..models import LastUpdated


@pytest.mark.django_db
def test_is_in_database_false():
    hq = HeadingQueries('no such heading')
    assert hq.is_in_database() is False


@pytest.mark.django_db
def test_is_in_database_true():
    _HEADING = "some heading"
    last_updated = LastUpdated(
        heading=_HEADING,
        when=datetime.datetime.now())
    last_updated.save()

    hq = HeadingQueries(_HEADING)
    assert hq.is_in_database() is True
