#!/usr/bin/env python3
'''Description: This program will output "hello world" to the screen.'''

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

print('Hello world')


def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

print("1. Convert inches -> cm")
print("2. Convert cm -> inches")

choice = input("Make your selection (1,2): ")

if choice == "1":
    inches = int(input("Enter inches: "))
    print("Number of cm:", inches_to_cm(inches))
elif choice == "2":
    cm = int(input("Enter cm: "))
    print("Number of inches:", cm_to_inches(cm))
else:
    print("Invalid entry")
