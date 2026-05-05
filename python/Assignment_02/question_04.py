'''Q4. Write a function to count and return the number of digits in a number n,.'''

n = int(input("Enter a digit: "))
count = 0
while n>0:
    count +=1
    n = n//10
print("The number of digits in the number is: ",count)