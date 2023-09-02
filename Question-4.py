# Write a python script to handle the ValueError

a = 'dfg'

try:
    b=int(a)
except ValueError:
    print("You cannot change letters into integer")