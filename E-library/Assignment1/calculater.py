
first = float(input("Enter the 1st number: "))
operator = input("Enter an operator (+, -, *, /): ")
second = float(input("Enter the 2nd number: "))

if operator == "+":
    print("Result:", first + second)
elif operator == "-":
    print("Result:", first - second)
elif operator == "*":
    print("Result:", first * second)
elif operator == "/":
    if second == 0:
        print("Cannot divide by zero.")
    else:
        print("Result:", first / second)
else:
    print("Invalid operator.")