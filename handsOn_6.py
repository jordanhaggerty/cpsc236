file_name = r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\world_cup_champions.txt"

def read_champions(file_name):
    champions = {}
    
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 2:
                continue
            year, country = parts[0], parts[1]
            if country not in champions:
                champions[country] = []
            champions[country].append(year)
    
    return champions

def display_champions(champions):
    print("Country       Wins      Years")
    print("=======       ====      =====")
    for country in sorted(champions):
        years = ", ".join(champions[country])
        print(f"{country:<15}{len(champions[country])}\t{years}")

def main():
    champions = read_champions(file_name)
    display_champions(champions)

if __name__ == "__main__":
    main()

-------------------------------------------------------------------------------------------


file_path = r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\monthly_sales.txt"

def menu():
    print("Monthly Sales program")
    print()
    print("COMMAND MENU")
    print("view - View sales for specified month")
    print("edit - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit - Exit program")
    print()

def load_sales():
    sales = {}
    with open(file_path, 'r') as file:
        for line in file:
            lines = line.strip().split()
            if len(lines) == 2:
                month, amount = lines
                sales[month.lower()] = float(amount)
    return sales

def view(sales):
    month = input("Three-letter Month: ").lower
    if month in sales:
        print(f"Sales amount for {month} is {sales[month]}.")
    else:
        print("Invalid three-letter month.")


def edit(sales):
    month = input("Three-letter Month: ").lower()
    if month in sales:
        amount = float(input("Sales Amount: "))
        sales[month] = amount
        with open(file_path, 'w') as file:
            for sale in sales:
                file.write(f"{sale} {sales[sale]}\n")
        print(f"Sales amount for {month.capitalize()} is {amount}.")
    else:
        print("Invalid three-letter month.")


def totals(sales):
    total = sum(sales.values())
    average = total / len(sales)
    print(f"Yearly total: {total}")
    print(f"Monthly average: {average}")

def exit():
    print("Bye!")
    pass

def main():
    sales = load_sales()
    while True:
        menu()
        command = input("Command: ").lower()
        if command == "view":
            view(sales)
        elif command == "edit":
            edit(sales)
        elif command == "totals":
            totals(sales)
        elif command == "exit":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()

