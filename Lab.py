print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")

# Take input from the user
choice = input("Enter choice (1 or 2): ")

if choice in ('1', '2'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
else:
    print("Invalid Input")
