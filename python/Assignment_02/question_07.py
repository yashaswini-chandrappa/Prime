'''Q7. Design a program to continuously input a number from user & print if it is 
positive or negative until the user enters "Quit"'''

while True:
    user_input = input("Enter a number to check if its positive or negative or Enter quit to end the loop: ")
    if user_input.lower() == "quit":
        break
    elif user_input.lstrip('-').isdigit():
        number = int(user_input)
        if number > 0:
            print("The entered input is a positive number")
        elif number < 0:
            print("The entered input is a negative number")
        else:
            print("The entered input is zero (neither positive nor negative)")
    else:
        print("Invalid input. Only integers or 'quit' are allowed as valid inputs")

print("Program Ended. Thank you :)")