'''Q7. Write a program that takes a string from the user and prints the number of spaces in the string.'''

given_string  = input("Provide a String : ")
count = 0
for i in given_string:
    if i == " ":
        count +=1
print("The number of spaces in the string is : ",count)