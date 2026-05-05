'''Q2. Write a function that takes two integers a and b and prints all even 
numbers between them(inclusive).'''

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("The even numbers between",a,"and",b, "is: ")
for i in range(a,b):
    if i%2==0:
        print(i,end=" ")