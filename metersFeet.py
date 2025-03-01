def user_input():
    print("Conversions Menu:")
    print()
    print("a.   Feet to Meters")
    print("b.   Meters to Feet")
    selection = input(str("Select a Conversion (a/b): "))
    return selection

def conversion(selection):
    if selection == 'a':
        feet = float(input("Enter feet: "))
        feetConv = feet * 0.3048
        print(f"{round(feetConv, 2)} meters")
    elif selection == 'b':
        meters = float(input("Enter meters: "))
        metersConv = meters / 0.3048
        print(f"{round(metersConv, 2)} feet")