'''Q9. Write a function is_prime(n)that returns True if n is a prime number and False otherwise, using a loop.'''

def is_prime(n):
    for i in range(2,n//2):
        if n%i==0:
            print(f"{n} is not a prime number")
            return
    print(f"{n} is a prime number")
            

n = int(input("Enter a number: "))
is_prime(n)
