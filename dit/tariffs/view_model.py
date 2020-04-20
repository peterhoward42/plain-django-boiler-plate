"""
This module contains classes that are capable of expressing the app's
view-model. I.e. the 'VM' in the MVVM pattern.
"""
from django.utils import timezone

from .models import Heading, Commodity


class ProductRow:
    """
    The view model for one row of the product/tariff table.
    """

    def __init__(
        self,
        emphasis: str,
        name: str,
        indent: int,
        vat: str,
        duty: str,
        revenue: str,
        price: str,
        volume: str,
        code: str,
    ):
        self.emphasis = emphasis
        self.product_name = name
        self.indent = indent
        self.vat = vat
        self.duty = duty
        self.revenue = revenue
        self.price = price
        self.volume = volume
        self.code = code


class ViewModel:
    """
    The top level view model.
    """

    @staticmethod
    def make_static_example(heading: str) -> dict:
        res = {}
        res['heading'] = heading
        res['rows'] = [ViewModel._make_heading_columns_row()]
        res['rows'].extend(ViewModel._make_all_static_rows())
        return res

    @staticmethod
    def make_from_heading_data_in_db(heading_digits: str) -> dict:
        heading_obj = Heading.objects.get(heading_digits=heading_digits)
        commodities = Commodity.objects.filter(belongs_to=heading_obj)

        res = {}
        res['heading'] = heading_digits
        res['minutes_old'] = ViewModel.minutes_old(heading_obj)
        res['rows'] = [ViewModel._make_heading_columns_row()]
        res['rows'].extend(ViewModel._make_all_real_rows(commodities))
        return res
        a = 42

    @staticmethod
    def minutes_old(heading_obj: Heading) -> str:
        last_updated = heading_obj.last_updated
        now = timezone.now()
        delta = now - last_updated
        minutes = delta.seconds / 60.0
        minutes = "{:.1f}".format(minutes)

        return minutes


    @staticmethod
    def _make_heading_columns_row() -> ProductRow:
        return ProductRow(
            emphasis="font-weight-bold",  # TODO don't let pure view scope creep in here (Bootstrap tag)
            name="Name",
            indent="0",
            vat="VAT",
            duty="Duty",
            revenue="Revenue / Ann",
            price="Price",
            volume="Volume",
            code="Commodity Code",
        )

    @staticmethod
    def _make_all_static_rows() -> [ProductRow]:
        rows = []
        for i in range(10):
            rows.append(ViewModel._make_one_static_row(i))
        return rows


    @staticmethod
    def _make_all_real_rows(commodities: [Commodity]) -> [ProductRow]:
        rows = []
        for commodity in commodities:
            rows.append(ViewModel._make_one_real_row(commodity))
        return rows

    @staticmethod
    def _make_one_static_row(row_index: int) -> ProductRow:
        return ProductRow(
            name=f"product_{row_index}",
            indent=str(row_index % 3),
            vat="15.0",
            duty="15%",
            revenue="4.3",
            price="3.16",
            volume="3200",
            code="20 07 68 51",
        )


    @staticmethod
    def _make_one_real_row(commodity: Commodity) -> ProductRow:
        return ProductRow(
            emphasis='',
            name=commodity.description,
            indent=str(commodity.indent),
            vat=commodity.vat,
            duty=commodity.duty,
            revenue="tbd",
            price="tbd",
            volume="tbd",
            code=commodity.remaining_digits,
        )

