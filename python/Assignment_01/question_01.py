'''Q1. Write a program that asks the user for their name and age, then prints a
sentence like:
    Hello Shradha, you are 21 years old!'''

user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age:"))
print("Hello ",user_name,", you are ",user_age,"years old!")
#o/p = Hello  yash , you are  24 years old!
#Why this exact output?
#"Hello " already has a space at the end
#print() adds another space between arguments
#", you are " has spaces before and after
#Same happens around user_age'''
print(f"Hello {user_name}, you are {user_age} years old!")




