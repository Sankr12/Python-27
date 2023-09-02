# Write a python script to implemented a nested Try except block

try:
    # Outer try block
    num1 = int(input("Enter a dividend: "))
    num2 = int(input("Enter a divisor: "))

    try:
        # Inner try block
        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Division by zero is not allowed in the inner block.")

except ValueError:
    print("Invalid input. Please enter valid integers in the outer block.")

except Exception as e:
    print("An error occurred:", str(e))

print("Program continues after handling exceptions.")
