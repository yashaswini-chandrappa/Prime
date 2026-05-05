'''Q10. Letʼs create a “Number Guessing Game”. Given a secret number (already decided by you), write a program that asks the user to guess it and prints: 
• if the guess is above the number "Too high" 
• if the guess is below "Too low" 
• if the guess matches "Congratulations! You guessed it right!"'''


print("Welcome to Number guessing game !!!")
number = 103
print("I have decided my number, You can start guessing it")
while True:
    user_input = int(input("Enter your number: "))
    if (user_input == number):
        print("Congratulations! You guessed it right!")
        break
    elif (user_input > number):
        print("Too High")
    elif (user_input < number):
        print("Too Low")

