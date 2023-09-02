# Write a python script to raise a ValueError.

try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if  b == 0:
        raise ValueError
    result = a/b
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid Entry")
except exception as e:
    print("An unexpected error:",e)
else:
    print("Result:",result)