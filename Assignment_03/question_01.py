'''Q1. Ask the user for a string and check whether it is a palindrome or not.
 A is a string which is same when we read it forward & backward. Eg- "madam", "racecar" etc'''

word = input("Enter a word : ")
reverse_word = word[-1::-1]
print(word, reverse_word)
if word == reverse_word:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

