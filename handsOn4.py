print("Prime Number Checker")
print()

def user_input():
    number = int(input("Please enter an input between 1-5000: "))
    return number

def calculate(number):
    prime = []
    counter = 0
    for i in range(1,number+1):
        if number % i == 0:
            prime.append(i)
            counter += 1
    if counter == 2:
            print(number, "is a prime number!")
            print()
    else:
            print(number, "is not a prime number!")
            print(f"It has {counter} factors {prime}")
            print()
            
def main():
    tryagain = "y"
    while tryagain.lower() == "y":
        number = user_input()
        calculate(number)
        tryagain = input("Would you like to try again? (y/n): ")
        print()
        pass
    print("Bye!")

if __name__ == "__main__":
    main()

---------------------------------------------------------------------------------------

contacts = ["Jordan Haggerty", "Brooke Gart"]
emails = ["jah1052@sru.edu", "bhg1001@sru.edu"]
phone = ["814-673-4224", "814-671-3000"]

print("Contact Manager")
print()
print("COMMAND MENU")
print("list - Display all contacts")
print("view - View a contact")
print("add - Add a contact")
print("del - Delete a contact")
print("exit - Exit program")
print()

def menu():
    user_input = input("Command: ")
    return user_input

def command(user_input):
    if user_input == "list":
        for index, contact in enumerate(contacts, start=1):
            print(index, contact)
            print()
    elif user_input == "view":
            select_contact = int(input("Number: "))
            if 1 <= select_contact <= len(contacts):
                print(f"Name: {contacts[select_contact-1]}")
                print(f"Email: {emails[select_contact-1]}")
                print(f"Phone: {phone[select_contact-1]}")
                print()
            else:
                print("Invalid contact number.")
                print()
    elif user_input == "add":
        add_name = input("Name: ")
        add_email = input("Email: ")
        add_number = input("Phone: ")
        contacts.append(add_name)
        emails.append(add_email)
        phone.append(add_number)
        print(f"{add_name} has been added.")
        print()
    elif user_input == "del":
        delete_contact = int(input("Number: "))
        if 1 <= delete_contact <= len(contacts):
            name_delete = contacts.pop(delete_contact-1)
            emails.pop(delete_contact-1)
            phone.pop(delete_contact-1)
            print(f"{name_delete} has been deleted.")
        else:
            print("Invalid Contact number.")
    print()

def main():
    while True:
        user_input = menu()
        if user_input == "exit":
            print("Bye!")
            break
        command(user_input)

if __name__ == "__main__":
    main()

