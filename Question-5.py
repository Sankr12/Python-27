# Write a python script to handle multiple exception in one try

a = 34

try:
    b = int(input("Enter a number: "))
    c = a/b
except ValueError:
    print("Abe gadhe number print karo!")
except ZeroDivisionError:
    print("You can't divide a number by 0")
except exception:
    print("Invalid Entry!")
finally:
    print("Program finish")