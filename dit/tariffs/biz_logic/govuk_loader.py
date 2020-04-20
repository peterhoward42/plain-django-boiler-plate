from django.utils import timezone

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

        # Build a new heading object that will replace the old one, if it
        # already exists because the heading_digits is the primary key.
        heading = Heading(
            heading_digits=self.heading,
            description=desc,
            last_updated=timezone.now()
        )
        heading.save()

        # Build (or update), and attach the commodity(s) that belong to the heading.
        self._load_child_commodities(heading, heading_info.commodity_info)

    def _load_child_commodities(
        self, heading: Heading, commodity_infos: [CommodityMetaInfo]
    ):
        for a_commodity in commodity_infos:
            self._load_commodity(heading, a_commodity)

    def _load_commodity(self, heading: Heading, commodity_meta: CommodityMetaInfo):

        desc = commodity_meta.desc
        code = commodity_meta.goods_nomenclature_item_id

        # Create (or retrieve) the commodity and set the fields that can be
        # just from the info provided in commodity_meta. This is all you
        # are going to get for non-leaf rows.
        commodity, created = Commodity.objects.update_or_create(
            remaining_digits=code[3:], belongs_to=heading, description=desc
        )

        # For leaf commodities, we fetch more info from the commodity api endpoint.
        if commodity_meta.is_leaf:
            commodity_json = GovUKCommodityFetcher.fetch_from_api(
                commodity_meta.goods_nomenclature_item_id
            )

            attr = commodity_json["data"]["attributes"]

            commodity.num_indents = attr["number_indents"]
            commodity.duty = attr[
                "basic_duty_rate"
            ]  # this is a string forming an HTML span!

        commodity.save()
