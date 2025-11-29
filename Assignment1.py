# Assignment 1
#python basic concept
#Task perform basic mathematical operation

# 2.Mathematical operation

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

#1.Input from the user
a = int(input("Enter the first number:"))

b = int(input("Enter the second number:"))

print(f"The result \n Addition:{addition(a,b)}\n Subtraction:{subtraction(a,b)}\n Multiplication:{multiplication(a,b)}\n Division:{division(a,b)}")

#Task 2
#personalized greeting

#input from user
first_name = str(input("Enter your first name:"))
last_name = str(input("Enter your second name:"))

#Result as mentioned in the Assignment
print(f"Hello,'{first_name+last_name}',! Welcome to python program")

