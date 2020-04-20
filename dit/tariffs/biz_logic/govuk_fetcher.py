import requests
from requests import HTTPError

URL_ROOT = f"https://www.trade-tariff.service.gov.uk/api/v2"


class CommodityMetaInfo:
    """
    Sparse info about commodities returned by the *headings* api call.
    """

    def __init__(self, desc: str, goods_nomenclature_item_id: str, is_leaf: bool):
        self.desc = desc
        self.goods_nomenclature_item_id = goods_nomenclature_item_id
        self.is_leaf = is_leaf


class FetchedHeadingData:
    def __init__(self, full_json: str):
        self.full_json = full_json
        self.commodity_info = []  # Of CommodityMetaInfo


class GovUKHeadingFetcher:
    """
    Knows how to call the GovUK public API to fetch information about
    a heading.
    """

    @staticmethod
    def fetch_from_api(heading: str) -> FetchedHeadingData:
        url = f"{URL_ROOT}/headings/{heading}"
        # TODO For now, let real exceptions be propagated.
        response = requests.get(url)
        # But we need to check explicitly for failure codes.
        response.raise_for_status()
        json_response = response.json()

        fetched_heading_data = FetchedHeadingData(json_response)

        included = json_response["included"]
        for item in included:
            its_type = item.get("type", None)
            if its_type == "commodity":
                goods_nomenclature_item_id = item["attributes"][
                    "goods_nomenclature_item_id"
                ]
                desc = item["attributes"]["formatted_description"]
                is_leaf = item["attributes"]["leaf"]

                info = CommodityMetaInfo(desc, goods_nomenclature_item_id, is_leaf)
                fetched_heading_data.commodity_info.append(info)

        return fetched_heading_data


class GovUKCommodityFetcher:
    """
    Knows how to call the GovUK public API to fetch information about
    a commodity.
    """

    @staticmethod
    def fetch_from_api(commodity_id: str) -> dict:
        url = f"{URL_ROOT}/commodities/{commodity_id}"
        # TODO For now, let real exceptions be propagated.
        response = requests.get(url)
        # But we need to check explicitly for failure codes.
        response.raise_for_status()
        json_response = response.json()

        return json_response
