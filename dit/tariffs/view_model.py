"""
This module contains classes that are capable of expressing the app's
view-model. I.e. the 'VM' in the MVVM pattern.
"""


class ProductRow:
    """
    The view model for one row of the product/tariff table.
    """

    def __init__(self, name: str, indent: int, vat: str, duty: str,
                 revenue: str, price: str, volume: str, code: str):
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
    def __init__(self):
        self.data = {}


def _make_heading_columns_row() -> ProductRow:
    return ProductRow(
        name='Name',
        indent='0',
        vat='VAT',
        duty='Duty',
        revenue='Revenue / Ann',
        price='Price',
        volume='Volume',
        code='Commodity Code',
    )


def _make_static_row(row_index: int) -> ProductRow:
    return ProductRow(
        name=f'product_{row_index}',
        indent=str(row_index % 3),
        vat='15.0',
        duty='15%',
        revenue='4.3',
        price='3.16',
        volume='3200',
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
        duty='15%',
        revenue='4.3',
        price='3.16',
        volume='3200',
        code='20 07 68 51',
    )


