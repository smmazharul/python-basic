# input = A function that prompts the user to enter data 
#        Returns the entered data as a string

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")


# Exercise 1 Rectangle Area Calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width

print(f"The area of the rectangle is: {area}")