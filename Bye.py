valid = False

while not valid:
    try:

        while n%2 == 0:

            print("bye")
        
        valid = True
    
    except ValueError:
        print("Invalid")

    except NameError:
        print("n is not a value")
        break