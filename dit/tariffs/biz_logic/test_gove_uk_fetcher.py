import pytest

from requests.exceptions import HTTPError

from .govuk_fetcher import GovUKFetcher


@pytest.mark.django_db
def test_fetch_runs_without_crashing():
    fetcher = GovUKFetcher(heading='0708')
    data_dict = fetcher.fetch()
    assert data_dict is not None

def test_fetch_handles_malformed_headings_sensibly():
    fetcher = GovUKFetcher(heading='garbage')
    with pytest.raises(HTTPError):
        content = fetcher.fetch()
