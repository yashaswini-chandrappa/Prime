'''Take a decimal number as input (like 45.78 ) and output its:
• integer part - 45
• fractional part - .78'''

int1 = float(input("Enter a decimal number : "))
integer_part = int(int1)
fractional_part = int1 - integer_part
print(f"The Value entered is {int1}\n Integer part is {integer_part}\n Fractional part is {fractional_part}")
