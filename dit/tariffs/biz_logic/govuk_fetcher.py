import requests
from requests import HTTPError

URL_ROOT = f'https://www.trade-tariff.service.gov.uk/api/v2'


class GovUKHeadingFetcher:
    """
    Knows how to call the GovUK public API to fetch information about
    a heading.
    """

    @staticmethod
    def fetch_from_api(heading: str) -> (dict, [str]):
        """
        The dict returned is the full json response from the API.
        The list of strings, is the set of included-commodity ids.
        """
        url = f'{URL_ROOT}/headings/{heading}'
        # TODO For now, let real exceptions be propagated.
        response = requests.get(url)
        # But we need to check explicitly for failure codes.
        response.raise_for_status()
        json_response = response.json()

        included = json_response['included']
        commodity_ids = []
        for item in included:
            its_type = item.get('type', None)
            if its_type == 'commodity':
                commodity_id = item['attributes']['goods_nomenclature_item_id']
                commodity_ids.append(commodity_id)

        return json_response, commodity_ids


class GovUKCommodityFetcher:
    """
    Knows how to call the GovUK public API to fetch information about
    a commodity.
    """

    @staticmethod
    def fetch_from_api(commodity_id: str) -> dict:
        url = f'{URL_ROOT}/commodities/{commodity_id}'
        # TODO For now, let real exceptions be propagated.
        response = requests.get(url)
        # But we need to check explicitly for failure codes.
        response.raise_for_status()
        json_response = response.json()

        return json_response

