import random

print("The Wizard Inventory Program")

def menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit Program")
    print()

def walk():
    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\wizard_all_items.txt", "r") as file:
        all_items = [line.strip() for line in file if line.strip()]

    random_item = random.choice(all_items)

    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\wizard_inventory.txt", 'r') as file:
        current_inventory = [line.strip() for line in file if line.strip()]

    choice = input(f"While walking down a path, you see {random_item}. Do you want to grab it? (y/n): ")

    while choice.lower() != "y" and choice.lower() != "n":
        print("Invalid input")
        choice = input(f"While walking down a path, you see {random_item}. Do you want to grab it? (y/n): ")

    if choice.lower() == "y":
        if len(current_inventory) >= 4:
            print("Inventory is full")
        else:
            with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\wizard_inventory.txt", 'a') as file: 
                file.write(f"\n{random_item}")
                print(f"You picked up {random_item}")

    elif choice.lower() == "n":
        print(f"You have left {random_item} behind, let's hope you won't need it in the future!")
pass

def show():
    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\wizard_inventory.txt", 'r') as file:
        current_inventory = [line.strip() for line in file if line.strip()]
        for index, item in enumerate(current_inventory, start=1) :
            print(f"{index}. {item}")
    print()


def drop():
    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\wizard_inventory.txt", 'r') as file: 
        drop_item = [line.strip() for line in file if line.strip()]

        if len(drop_item) == 0:
            print("no items in inventory")
        else:
            drop_selection = int(input("Enter position of item you would like to drop: "))
            if 1 <= drop_selection <= len(drop_item):
                drop = drop_item.pop(drop_selection - 1)
                with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\wizard_inventory.txt", 'w') as file:
                    for item in drop_item:
                        file.write(item + '\n')
                print(f"{drop} has been dropped.")
            else:
                print("No item in that item slot.")
        
def exit():
    print("Goodbye my fellow wizard. Good luck on your journey!")

def main():
    menu()
    while True:
        user_input = input("Command: ")

        if user_input == "walk":
            walk()
        elif user_input == "show":
            show()
        elif user_input == "drop":
            drop()
        elif user_input == "exit":
            exit()
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()

--------------------------------------------------------------------------------------------------------

import csv

print("Monthly Sales Program")

def menu():
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly - View yearly summary")
    print("edit - Edit sales for a month")
    print("exit - Exit program")
    print()

def monthly():
    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\monthly_sales.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0] + " - " + str(row[1]))
    print()

def yearly():
    sum = 0
    counter = 0

    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\monthly_sales.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            amount = int(row[1])
            sum += amount
            counter += 1

    average = sum / counter
    print (f"Yearly total: {round(sum, 2)}")
    print(f"Monthly average: {round(average, 2)}")
    print()

def edit():
   
    month = input("Three letter month: ").title()

    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\monthly_sales.csv", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

        new_amount = int(input("Sales Amount: "))

    for row in rows:
        if row[0] == month:
            row[1] = str(new_amount)

    with open(r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\monthly_sales.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Sales amount for {month} was modified.\n")
    print()

def exit():
    print("Bye!")

def main():
    menu()
    while True:
        user_input = input("Command: ")
        print()

        if user_input == "monthly":
            monthly()
        elif user_input == "yearly":
            yearly()
        elif user_input == "edit":
            edit()
        elif user_input == "exit":
            exit()
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
