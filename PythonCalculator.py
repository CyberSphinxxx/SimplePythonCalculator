
choice = input("Enter Math Mode: ")
separator = "------------------------------"

if choice == '+':
    print(separator)
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

elif choice == '-':
    print(separator)
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    sum = num1 - num2
    print(f"{num1} - {num2} = {sum}")

elif choice == '*':
    print(separator)
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    sum = num1 * num2
    print(f"{num1} * {num2} = {sum}")

elif choice == '/':
    print(separator)
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    sum = num1 / num2
    print(f"{num1} / {num2} = {sum}")

else:
    print(separator)
    print("Invalid Input")
    print("Math Modes Are: + - * /")
