3#### Operations

### Loop operation
while True:

        # Operations
    print(" CHOOSE YOUR OPERATION METHOD")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Mulitply")
    print("4. Division")
    print("5. EXIT")

    operation = input()

    if operation == "1":
        num1=input("Enter First Number: ")
        num2=input("Enter Second Number")        ### Addition
        print("Your sum is " + str(int(num1 )+ int(num2)))
    elif operation == "2":
        num1=input("Enter First Number: ")
        num2=input("Enter Second Number")
        print("Your sum is " + str(int(num1) - int(num2)))
    elif operation == "3":
        num1=input("Enter First Number: ")
        num2=input("Enter Second Number")
        print("Your sum is " + str(int(num1) * int(num2)))
    elif operation == "4":
        num1=input("Enter First Number: ")
        num2=input("Enter Second Number")
        print("Your sum is " + str(int(num1) / int(num2)))
    elif operation == "5":
        print("Exiting the calculator... Goodbye")
        break
    else:
        print("Entry was invaild")
