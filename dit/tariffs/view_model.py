"""
This module contains classes that are capable of expressing the app's
view-model. I.e. the 'VM' in the MVVM pattern.
"""


class ProductRow:
    """
    The view model for one row of the product/tariff table.
    """

    def __init__(self, name: str, indent: int, vat: str, govuk_duty: str, overidden_duty: str,
                 revenue: str, price: str, volume: str, code: str):
        self.product_name = name
        self.indent = indent
        self.vat = vat
        self.govuk_duty = govuk_duty
        self.overidden_duty = overidden_duty
        self.revenue = revenue
        self.price = price
        self.volume = volume
        self.code = code


class ViewModel:
    """
    The top level view model.
    """
    def __init__(self):
        self.data = {}


def _make_heading_columns_row() -> ProductRow:
    return ProductRow(
        name='Name',
        indent='0',
        vat='VAT',
        govuk_duty='Duty (official)',
        overidden_duty='Duty (override)',
        revenue='Revenue / Ann',
        price='Price (EUR)',
        volume='Volume',
        code='Commodity Code',
    )


def _make_static_row(row_index: int) -> ProductRow:
    return ProductRow(
        name=f'product_{row_index}',
        indent=str(row_index % 3),
        vat='15.0',
        govuk_duty='15%',
        overidden_duty='9% + 26 EUR / Kg',
        revenue='4.3M/ann',
        price='3.16/Kg',
        volume='3200 tonne/ann',
        code='20 07 68 51',
    )


def make_static_example(heading:str) -> ViewModel:
    mdl = ViewModel()
    mdl.data["heading"] = heading

    rows = [_make_heading_columns_row()]
    rows.extend(_make_all_static_rows())
    mdl.data['rows'] = rows

    return mdl


def _make_all_static_rows() -> [ProductRow]:
    rows = []
    for i in range(10):
        rows.append(_make_one_static_row(i))
    return rows


def _make_one_static_row(row_index: int) -> ProductRow:
    return ProductRow(
        name=f'product_{row_index}',
        indent=str(row_index % 3),
        vat='15.0',
        govuk_duty='15%',
        overidden_duty='9% + 26 EUR / Kg',
        revenue='EUR 4.3M/ann',
        price='EUR 3.16/Kg',
        volume='3200 tonne/ann',
        code='20 07 68 51',
    )


