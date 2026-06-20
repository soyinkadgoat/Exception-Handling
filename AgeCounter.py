try:

    age = int(input("Enter your age: "))

    if age % 2 == 0:
        print("Your age is an even number")
    else:
        print("Your age is an odd number")

except ValueError as error:
    print("the error is:", error)