class ViewModel:

    def __init__(self, heading: str):
        self.data = {
            "heading": heading,
            "rows": []
        }
        for row in range(10):
            row = {
                "product_name": f'product-{row}',
                "indent": row % 3,
            }
            self.data["rows"].append(row)