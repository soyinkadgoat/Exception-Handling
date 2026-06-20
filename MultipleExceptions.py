try:

    num1, num2 = eval(input("Enter two numbers, seperated by a comma: "))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter number like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")


finally:
    print("This will execute no matter what")


"""
1, 2

num 1 = 1
num2 = 2

result = 1/2

result is 0.5

wrong input

comma is missing

num1 = 0
num2 = 5

division by zro i error

"""