#exceptions = An event that interupts the flow of a program
#             (Zero division error, TypeError, ValueError)
#             1. try, 2. except, 3. finaly


try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cant divide by zero")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")