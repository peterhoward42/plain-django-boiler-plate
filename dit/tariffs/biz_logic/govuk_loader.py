import json
import pprint

import requests
from requests import HTTPError

from ..biz_logic.govuk_fetcher import GovUKFetcher


class GovUKLoader:
    """
    Knows how to update the database with tariff information fetched from
    the trade-tariff.service.gov.uk/api/v2/headings api.
    """

    def __init__(self, heading:str):
        self.heading = heading

    def load_db_from_govUK_api_call(self) -> None:
        fetcher = GovUKFetcher(self.heading)
        data_dict = fetcher.fetch()



