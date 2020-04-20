"""
This module contains classes that are capable of expressing the app's
view-model. I.e. the 'VM' in the MVVM pattern.
"""
from .models import Heading, Commodity


class ProductRow:
    """
    The view model for one row of the product/tariff table.
    """

    def __init__(
        self,
        name: str,
        indent: int,
        vat: str,
        duty: str,
        revenue: str,
        price: str,
        volume: str,
        code: str,
    ):
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
        heading_obj = Heading.objects.filter(heading_digits=heading_digits)
        commodities = heading_obj.commodity_set
        commodities = Commodity.objects.filter(belongs_to=heading_obj)

        res = {}
        res['heading'] = heading_digits
        res['rows'] = [ViewModel._make_heading_columns_row()]
        res['rows'].extend(ViewModel._make_all_real_rows(commodities))
        return res
        a = 42

    @staticmethod
    def _make_heading_columns_row() -> ProductRow:
        return ProductRow(
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
            name='forget name',
            indent=str(commodity.indent),
            vat=commodity.vat,
            duty=commodity.duty,
            revenue="tbd",
            price="tbd",
            volume="tbd",
            code=commodity.remaining_digits,
        )

