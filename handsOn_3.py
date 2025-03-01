# print("Even or Odd Checker")
# print()
# def user_input():
#         num = int(input("Enter an integer: "))
#         return num

# def even_odd(num):
#     if num % 2 == 0:
#         print("This is an even number")
#     elif num % 2 !=0:
#         print("This is an odd number")
#     else:
#         print("invalid input")
    

# def main():
#     num = user_input()
#     even_odd(num)

# main() 

import metersFeet as conv

print("Feet and Meters Converter")
print()
    
def main():
    selectagain = "y"
    while selectagain.lower() == "y":
        selection = conv.user_input()
        conv.conversion(selection)
        selectagain = input("Would you like to perform another conversion? (y/n): ")
        if selectagain.lower() == "y":
            pass
    print("Bye!")

if __name__ == "__main__":
    main()

# import taxes as tax

# print("Sale Tax Calculator")
# print()

# def main():
#     runagain = "y"
#     while runagain.lower()  == "y":
#         x = tax.item_cost()
#         print(f"Total: $ {round(x,2)}")
#         tax.tax(x)
#         runagain = input("Again? (y/n): ")
#         print()
#         pass
#     print("Thanks, bye!")
   
# if __name__ == "__main__":
#     main()

# print("Prime number checker")
# print()

# def user_input():
#     num = int(input("Please enter a number between 1 and 5000: "))
#     if num <= 1 or num > 5000:
#         print("invalid integer. Please try again")
#     else:
#         pass
#     return num

# def prime(num):
#     counter = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             counter += 1
#     if counter == 2:
#         print(num, "is a prime number.")
#     else:
#         print(num, "Is not a prime number.")
#         print(f"It has {counter} factors.")

        


# def main():
#     input_again = "y"
#     while input_again.lower() == "y":
#         num = user_input()
#         prime(num)
#         input_again = input("Try Again? (y/n): ")
#         print()
#         pass
#     print("Bye!")

# main()