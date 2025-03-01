def item_cost():
    print("Enter items (ENTER 0 TO END): ")
    itemCost = 1
    x = 0
    while itemCost != 0:
        itemCost = float(input("Item cost: $"))
        x += itemCost
    return x

def tax(x):
    tax_amount = x * .06
    total = x + tax_amount
    print(f"Sales Tax: ${round(tax_amount,2)}")
    print(f"Total after tax: ${round(total,2)}")
    print()