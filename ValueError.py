try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as error:
    print("The error is:", error)