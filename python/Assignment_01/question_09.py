'''Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
compute simple interest:
SI = (P ∗ R ∗ T)/100
'''
principal = float(input("Enter the principal amount : "))
rate = float(input("Enter rate : "))
time = float(input("Enter time : "))
simple_interest = (principal*rate*time)/100
print(f"The Simple interest is {simple_interest}")