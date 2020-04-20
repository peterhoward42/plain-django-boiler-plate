import pytest

from requests.exceptions import HTTPError

from .govuk_fetcher import GovUKHeadingFetcher, GovUKCommodityFetcher


@pytest.mark.django_db
def test_fetch_heading_runs_without_crashing():
    heading_info = GovUKHeadingFetcher.fetch_from_api("0708")
    assert heading_info is not None
    assert len(heading_info.commodity_info) > 0


def test_fetch_handles_malformed_headings_sensibly():
    with pytest.raises(HTTPError):
        GovUKHeadingFetcher.fetch_from_api("garbage")


@pytest.mark.django_db
def test_fetch_commodity_runs_without_crashing():
    commodity_json = GovUKCommodityFetcher.fetch_from_api("0708100000")
    assert commodity_json is not None
