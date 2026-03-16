from utils import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute

while True:
    operación = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

    if operación == "exit":
        break

    elif operación == "add":
        num1= float(input("Enter the first number:\n"))
        num2= float(input("Enter the second number:\n"))
        result= add(num1, num2)
        print("The result is:", result)

    elif operación == "subtract":
        num1= float(input("Enter the first number:\n"))
        num2= float(input("Enter the second number:\n"))
        result= sub(num1, num2)
        print("The result is:", result)

    elif operación == "multiply":
        num1= float(input("Enter the first number:\n"))
        num2= float(input("Enter the second number:\n"))
        result= multiply(num1, num2)
        print("The result is:", result)

    elif operación == "divide":
        num1= float(input("Enter the first number:\n"))
        num2= float(input("Enter the second number:\n"))
        result= divide(num1, num2)

        if isinstance(result, str):
            print(result)
        else:
            print("The result is:", result)

    elif operación == "exponent":
        num1= float(input("Enter the first number:\n"))
        num2= float(input("Enter the second number:\n"))
        result= exponent(num1, num2)
        print("The result is:", result)

    elif operación == "modulo":
        num1= float(input("Enter the first number:\n"))
        num2= float(input("Enter the second number:\n"))
        result = modulo(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print("The result is:", result)

    elif operación == "floor_divide":
        num1= float(input("Enter the first number:\n"))
        num2= float(input("Enter the second number:\n"))
        result= floor_divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print("The result is:", result)

    elif operación == "absolute":
        num= float(input("Enter the number:\n"))
        result= absolute(num)
        print("The result is:", result)

    else:
        print("Invalid option!")