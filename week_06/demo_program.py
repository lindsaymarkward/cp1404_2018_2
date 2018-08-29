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

PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"

def main():
    print(MENU_STRING)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "L":
            print("list")
        elif choice == "S":
            print("swap")
        else:
            print("Invalid")

        print(MENU_STRING)
        choice = input(">").upper()
    print("Finished")

main()
