from datetime import datetime, timedelta
from week_06.product import Product
from week_09.perishableproduct import PerishableProduct


def main():
    p1 = Product("Phone", 356.4, True)
    print(p1)
    p2 = Product("Chicken", 29)
    print(p2)

    now = datetime.now().date()
    later = now + timedelta(14)
    p3 = PerishableProduct(later, name="Milk", price=4.15)
    print(p3)

    products = [p1, p2, p3]
    for product in products:
        product.put_on_sale(12)
        print(product)


if __name__ == '__main__':
    main()
