# Write a python script to create a ArithmeticError

numerator = 10
denominator = 0
try:
    result = numerator / denominator  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    pass
finally:
    raise ArithmeticError