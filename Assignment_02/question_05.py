'''Q5. Write a function to return sum of the digits of a number n.'''

n = int(input("Enter a digit: "))
sum = 0
while n>0:
    last_digit = n%10
    sum += last_digit
    n=n//10
print("The sum of the digit is:", sum)