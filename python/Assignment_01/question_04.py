'''The user enters a string containing a number (e.g., "45" ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.'''

a = input("Enter a number: ")
int_value = int(a)
float_value = float(a)
string_value = a
print(f"{int_value} - {type(int_value)}\n {float_value} - {type(float_value)}\n {string_value} - {type(a)}")