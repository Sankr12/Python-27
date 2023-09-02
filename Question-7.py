# Write a python script to add a finally block for the above script 

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError("Division by Zero is not allowed")
    return a/b

try:
    print("Enter your choice: [Add/Subtract/Multiply/Divide]")
    choice = input().strip().lower()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter Second number: "))

    if choice == 'add':
        result = add(num1,num2)
    elif choice == 'subtract':
        result = sub(num1,num2)
    elif choice == 'multiply':
        result = multiply(num1,num2)
    elif choice == 'divide':
        if num2 == 0:
            raise ZeroDivisionError
        result = divide(num1,num2)
    else:
        raise ValueError("Invalid Choice")
    
    print("Result:",result)

except ZeroDivisionError:
    print("Error: Division by Zero is not allowed")
except ValueError:
    print("Invalid Input Entered")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program Complete")