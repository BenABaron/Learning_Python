
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Error! " + str(err))
except ValueError:
    print("Invalid input")

