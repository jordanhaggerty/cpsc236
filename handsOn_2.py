#Letter Grade Converter

gradeAgain = "y"

while gradeAgain.lower() == "y": 
    grade = int(input("Enter numerical grade: "))

    if grade >= 88:
        print("Letter Grade: A")
    elif grade >= 80:
        print("Letter Grade: B")
    elif grade >= 67:
        print("Letter Grade: C")
    elif grade >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")
    
    gradeAgain = input("Continue (y/n): ")
    print()

print("Bye!")


#Tip Calculator

mealCost = int(input("Cost of meal:     "))

for tip in range(15 , 30, 5):
    tipConv = tip / 100
    total = tip + tipConv
    print(tip, "%")
    print("Tip Amount:      ", round(mealCost * tipConv, 2))
    print("Total Amount:    ", total)


#Change Calculator

calculateAgain = "y"

while calculateAgain.lower() == "y":
    change = int(input("Enter number of cents 0-99: "))

    quarters = change // 25
    print("Quarters:", quarters)
    remainingChange = change % 25
    dimes = remainingChange // 10
    print("Dimes:   ", dimes)
    remainingChange = remainingChange % 10
    nickels = remainingChange // 5
    print("Nickels: ", nickels)
    remainingChange = remainingChange % 5
    pennies = remainingChange // 1
    print("Pennies: ", pennies)
    calculateAgain = input("Continue (y/n): ")
    print()

print("Bye!")

#Table of Powers

while True:
    start = int(input("Start number: "))
    stop = int(input("Stop number: "))
    if start < stop:
        break
    else:
        print("Error: Start number MUST BE less than Stop number")

print("Number   Squared   Cubed")
print("======   =======   =====")
for calculation in range(start, stop):
    print(calculation + 1,"     ", calculation ** 2,"    ", calculation ** 3)
   