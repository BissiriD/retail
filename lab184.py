import os
import retail
import datetime

today = datetime.datetime.now()
print(today.strftime("%x %X"))
def main():
    item1 = retail.retailItem("Jacket", 12, 59.95)
    item2 = retail.retailItem("Designer Jeans", 40, 34.95)
    item3 = retail.retailItem("Shirt", 20, 24.95)

    for count, item in enumerate([item1, item2, item3], 1):
        print(f"Retail Item {count}")
        print(f"Discreption: {item.get_desc()}")
        print(f"Units in Inventory: {item.get_units()}")
        print(f"Price: {item.get_price()}\n")

main()