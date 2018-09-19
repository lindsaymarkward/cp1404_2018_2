class Product:
    GST_RATE = 0.1  # 10%

    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        sale_status = ' (on sale!!)' if self.is_on_sale else ''
        return "{} ${:.2f}{}".format(self.name, self.price, sale_status)

    def __repr__(self):
        return str(self)

    def put_on_sale(self, percentage):
        self.is_on_sale = True
        self.price *= (1 - percentage / 100)
