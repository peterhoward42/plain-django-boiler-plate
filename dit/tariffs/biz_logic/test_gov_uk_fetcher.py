import pytest

from requests.exceptions import HTTPError

from .govuk_fetcher import GovUKHeadingFetcher, GovUKCommodityFetcher


@pytest.mark.django_db
def test_fetch_heading_runs_without_crashing():
    heading_json, commodity_ids = GovUKHeadingFetcher.fetch_from_api('0708')
    assert heading_json is not None
    assert len(commodity_ids) > 0


def test_fetch_handles_malformed_headings_sensibly():
    with pytest.raises(HTTPError):
        GovUKHeadingFetcher.fetch_from_api('garbage')


@pytest.mark.django_db
def test_fetch_commodity_runs_without_crashing():
    # To obtain a valid commodity id, we will fetch a heading
    # and use a commodity that is included by it.
    _, commodity_ids = GovUKHeadingFetcher.fetch_from_api('0708')

    a_commodity_id = commodity_ids[0]
    commodity_json = GovUKCommodityFetcher.fetch_from_api(a_commodity_id)
    assert commodity_json is not None

