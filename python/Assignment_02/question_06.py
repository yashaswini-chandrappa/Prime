'''Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.'''

print("The Numbers divisible by both 3 and 5 in the range of 1 to 100 is :")
for i in range (1,101):
    if (i%3==0) and(i%5==0):
        print(i,end =" ")