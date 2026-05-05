'''Q6. Write a program to swap values of two numbers entered by the user'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#by using temp variable 
temp_value = num2
num2 = num1
num1 = temp_value
print(f"The swapped values are num1 = {num1}, num2 = {num2}")

#Without using temp variable
num1 , num2 = num2 , num1
print(f"The reswapped values are num1 = {num1}, num2 = {num2}")