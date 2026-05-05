'''Q8. Lets create a simple calculator that performs arithmetic operations. Create a function calculator(a,b,operation)that performs addition, subtraction, multiplication, or division based on the parameter. 
{ operation [parameter can have values '+', '-', '*', '/'] '''

def calculator(a,b,operation):
    match operation:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "%":
            return a%b 
        
a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
operation = input("Enter the operation: ")
output = calculator(a,b,operation)
print (f"{a} {operation} {b} = {output}")