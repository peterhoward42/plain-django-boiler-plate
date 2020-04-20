from datetime import datetime

from ..biz_logic.govuk_fetcher import GovUKHeadingFetcher, GovUKCommodityFetcher
from ..models import Heading, Commodity

from ..biz_logic.govuk_fetcher import CommodityMetaInfo


class GovUKLoader:
    """
    Knows how to update the database with heading/commodity information fetched from
    the trade-tariff.service.gov.uk/api/v2/headings api.
    """

    def __init__(self, heading: str):
        self.heading = heading

    def load_heading_from_govuk_api_call(self) -> None:

        heading_info = GovUKHeadingFetcher.fetch_from_api(self.heading)

        data = heading_info.full_json["data"]
        attributes = data["attributes"]
        desc = attributes["formatted_description"]

        # Build the heading object.
        heading = Heading(
            heading_digits=self.heading, description=desc, last_updated=datetime.now(),
        )
        heading.save()

        # Build and attach the commodity(s) that belong to the heading.
        self._load_child_commodities(heading, heading_info.commodity_info)

    def _load_child_commodities(
        self, heading: Heading, commodity_infos: [CommodityMetaInfo]
    ):
        for a_commodity in commodity_infos:
            self._load_commodity(heading, a_commodity)

    def _load_commodity(self, heading: Heading, commodity_meta: CommodityMetaInfo):
        # First initialise a Commodity based only the meta info that has come
        # from the heading api call.

        desc = commodity_meta.desc
        code = commodity_meta.goods_nomenclature_item_id

        commodity = Commodity(
            remaining_digits=code[3:], belongs_to=heading, description=desc,
        )
        # For leaf commodities, we need more info from the commodity api endpoint.
        if commodity_meta.is_leaf:
            commodity_json = GovUKCommodityFetcher.fetch_from_api(
                commodity_meta.goods_nomenclature_item_id
            )

            attr = commodity_json["data"]["attributes"]

            commodity.num_indents = attr["number_indents"]
            commodity.duty = attr[
                "basic_duty_rate"
            ]  # this is a string forming an HTML span!
            a = 42

        commodity.save()
