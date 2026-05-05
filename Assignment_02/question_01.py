'''Q1. Write a program that takes salary as input. Using conditionals tatements,calculate the fixed rate tax based on these rules:
1. Ifsalary<30,000→5%
2. Ifsalaryis30,000–70,000→15%
3. Ifsalary>70,000→25%'''

salary = int(input("Enter your Salary: "))
if salary<30000:
    tax = (5/100)*salary
    print("Your tax deducted is :",tax)
elif salary>30000 and salary<70000:
    tax = (15/100)*salary
    print("Your tax deducted is :",tax)
elif salary>70000:
    tax = (25/100)*salary
    print("Your tax deducted is :",tax)
