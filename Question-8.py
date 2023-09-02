# Write a python script to implement try except and else block for division

try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a/b
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid Entry")
except exception as e:
    print("An unexpected error:",e)
else:
    print("Result:",result)