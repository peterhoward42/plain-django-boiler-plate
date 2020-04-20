
from datetime import datetime

from ..biz_logic.govuk_fetcher import GovUKFetcher
from ..models import Heading, Commodity


class GovUKLoader:
    """
    Knows how to update the database with heading/commodity information fetched from
    the trade-tariff.service.gov.uk/api/v2/headings api.
    """

    def __init__(self, heading:str):
        self.heading = heading

    def load_heading_from_govuk_api_call(self) -> None:
        fetcher = GovUKFetcher(self.heading)
        fetched = fetcher.fetch()

        attributes = fetched['attributes']
        desc = attributes['formatted_description']

        # Build the heading object.
        heading = Heading(
            heading_digits=self.heading,
            description=desc,
            last_updated=datetime.now(),
        )
        heading.save()

        # Build and attach the commodity(s) that belong to the heading.
        self._load_child_commodities(heading, attributes)

    def _load_child_commodities(self, heading: Heading, attributes: dict):
        included_items = attributes['included']
        commodities = []
        for item in included_items:
            its_type = item.get('type', None)
            if its_type is 'commodity':
                self._load_commodity(heading, item)

    def _load_commodity(self, heading: Heading, commodity_item: dict):
        desc = commodity_item['formatted_description']
        indent = commodity_item['number_indents']
        code = commodity_item['goods_nomenclature_item_id']
        leaf = commodity_item['leaf']

        commodity = Commodity(
            remaining_digits=code[3:],
            belongs_to=heading,
            description=desc,
            indent=indent,
        )
        commodity.save()


