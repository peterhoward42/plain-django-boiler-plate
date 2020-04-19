import requests
from requests import HTTPError


class GovUKFetcher:
    """
    Knows how to call the GovUK public API to fetch information about
    a heading.
    """

    def __init__(self, heading:str):
        self.heading = heading

    def fetch(self) -> dict:
        url = f'https://www.trade-tariff.service.gov.uk/api/v2/headings/{self.heading}'
        # For now, let real exceptions be propagated.
        response = requests.get(url)
        # But we need to check explicitly for failure codes.
        response.raise_for_status()
        json_response = response.json()
        return json_response['data']

