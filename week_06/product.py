class Product:
    GST_RATE = 0.1  # 10%

    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        sale_status = 'y' if self.is_on_sale else 'n'
        return "{} ${:.2f} ({})".format(self.name, self.price, sale_status)


p1 = Product("Phone", 356.4, True)
print(p1)
p2 = Product("Chicken", 29)
print(p2)

# p1.name = "Phone"
# print(p1.name, p1.price)
# print(p1.GST_RATE)
# p1.dummy(5)
# Product.dummy(p1)
