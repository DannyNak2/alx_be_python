# Define the Variables to get user input for first and second number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Define the Variabel to get user input for the operaton
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result:.2f}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result:.2f}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result:.2f}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result:.2f}.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")

        git add .
        git commit -m"add the name second"
        git push origin main