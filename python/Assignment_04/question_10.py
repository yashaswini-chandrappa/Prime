'''Q10. Ask the user for a string and print:
All unique characters
•The count of unique characters '''


user_input = input("Enter a string : ")
unique = " "
count = 0
for i in user_input:
    if i not in unique:
        unique += i
        count +=1
print(user_input)
print(unique)
print(count)

