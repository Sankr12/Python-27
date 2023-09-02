# Write a python script to handle the ArithmeticError

numerator = 10
denominator = 0
try:
    result = numerator / denominator  # This will raise a ZeroDivisionError
except ArithmeticError:
    print("You cannot divide a number by 0")