'''Q3. Write a function that prints digits of a number n.
 For eg:,n = 312, there are 3 digits in it 3,1 and 2 & we need to print them'''

n = int(input("Enter a digit: ")) #n =123
print("The digits in number",n,"are : ")
while n>0:
    last_digit = n%10 
    print(last_digit,end=" ")
    n = n//10 