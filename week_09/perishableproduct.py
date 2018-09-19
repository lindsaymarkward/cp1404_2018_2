from week_06.product import Product


class PerishableProduct(Product):
    def __init__(self, expiry_date, **kwargs):
        super().__init__(**kwargs)
        self.expiry_date = expiry_date

    def __str__(self):
        return "{} ({})".format(super().__str__(), self.expiry_date)
