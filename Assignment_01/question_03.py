'''Q3. Ask the user to enter two integers and one float. Convert them all to floats
and print their average.
'''

int_1 = int(input("Enter an integer: "))
int_2 = int(input("Enter another integer: "))
float_1 = float(input("Enter a float value: "))
avg = (float(int_1)+float(int_2)+float_1)/3
print(f"The average is : {avg}")