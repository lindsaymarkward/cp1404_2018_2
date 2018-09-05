"""
0. Pattern-based programming
1. Names based on the problem domain
2. Functions at the same level of abstraction (main should "look like"...)

Menu-driven product program
load products
- L_ist products
- S_wap sale status (get product number with error checking)
- Q_uit (save file)
"""

# make CSV from list of lists
# with open("products.csv", 'w') as output_file:
#     for product in products:
#         sale_status = 'y' if product[2] else 'n'
#         print("{},{},{}".format(product[0], product[1], sale_status), file=output_file)

from week_06.product import Product

ON_SALE_INDEX = 2
PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"


def main():
    products = load_products()
    print(products)
    print(MENU_STRING)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "L":
            list_products(products)
        elif choice == "S":
            swap_sale_status(products)
        elif choice == "O":
            list_on_sale_products(products)
        else:
            print("Invalid")

        print(MENU_STRING)
        choice = input(">").upper()
    save_products(products)
    print("Finished")


def load_products():
    products = []
    with open(PRODUCTS_FILE) as input_file:
        for line in input_file:
            # print(repr(line))
            parts = line.strip().split(',')
            # print(parts)
            if parts[2] == 'y':
                is_on_sale = True
            else:
                is_on_sale = False
            products.append(Product(parts[0], float(parts[1]), is_on_sale))
    # products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
    # products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
    return products


def list_products(products):
    print("list")
    for product in products:
        print(product)


def list_on_sale_products(products):
    for product in products:
        if product.is_on_sale:
            print(product)


def swap_sale_status(products):
    list_products(products)
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input("? "))
            if number < 0:
                print("Product must be >= 0")
            else:
                is_valid_input = True
        except ValueError:  # or just  except:
            print("Invalid (not an integer)")
    products[number].put_on_sale(10)
    print(products[number])


def save_products(products):
    pass


main()
