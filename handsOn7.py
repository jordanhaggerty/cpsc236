print("Tip Calculator")
print()

def meal_cost():
    while True:
        while True:
            try:
                meal_cost = float(input("Cost of Meal: "))
                if meal_cost <= 0:
                    print("Meal cost must be greater than 0!")
                else:
                    break
            except ValueError:
                print("Must be valid decimal number. Try again.")
        while True:
            try:
                tip_percent = int(input("How much would you like to tip?: "))
                if tip_percent <= 0:
                    print("Tip must be greater than 0!")
                else:
                    break
            except ValueError:
                print("Must be valid integer. Try again.")

        tip = round(meal_cost * (tip_percent / 100), 2)
        total_cost = round(meal_cost + tip, 2)

        print("------------------------")
        print(f"Cost of meal: ${meal_cost:.2f}")
        print(f"Tip percent: {tip_percent}%")
        print(f"Tip Amount: ${tip:.2f}")
        print(f"Total: ${total_cost:.2f}")
        print()
            
def main():
    meal_cost()

if __name__ == "__main__":
    main()

---------------------------------------------------------------------------------------

import random

fileName = r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\wizard_inventory.txt"

print("The Wizard Inventory Program")

try:
    with open(fileName, 'r') as file:
        inventory = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("Could not find inventory file!")
    print("Wizard is starting with no inventory.\n")
    inventory = []

def menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit Program")
    print()

def walk():
    all_items = ["a wand", "a potion", "a crossbow", "a spellbook", "a cloak"]
    random_item = random.choice(all_items)

    choice = input(f"While walking down a path, you see {random_item}. Do you want to grab it? (y/n): ")

    while choice.lower() != "y" and choice.lower() != "n":
        print("Invalid input")
        choice = input(f"While walking down a path, you see {random_item}. Do you want to grab it? (y/n): ")

    if choice.lower() == "y":
        if len(inventory) >= 4:
            print("Inventory is full.")
        else:
            inventory.append(random_item)
            print(f"You picked up {random_item}")
    else:
        print(f"You left the {random_item} behind.\n")

def show():
    if not inventory:
        print("Your inventory is empty.")
    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
    print()

def drop():
    try:
        with open(fileName, 'r') as file: 
            drop_item = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Could not find inventory file!")
        print("Wizard is starting with no inventory.")

        if len(drop_item) == 0:
            print("no items in inventory")

    while True:
        try:
            drop_index = int(input("Enter the number of the item to drop: "))
            if 1 <= drop_index <= len(inventory):
                dropped_item = inventory.pop(drop_index - 1)
                print(f"{dropped_item} has been dropped.\n")
                break
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def exit_program():
    print("Goodbye my fellow wizard. Good luck on your journey!")
    print()

def main():
    menu()
    while True:
        command = input("Command: ").lower()
        if command == "walk":
            walk()
        elif command == "show":
            show()
        elif command == "drop":
            drop()
        elif command == "exit":
            exit_program()
            break
        else:
            print("Invalid input.\n")

if __name__ == "__main__":
    main()
