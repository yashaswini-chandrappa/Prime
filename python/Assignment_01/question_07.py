'''Q7 Ask the user for a temperature in Celsius (string input). Convert it to float,
then calculate and print temperature in Fahrenheit.
Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) +
32
'''

Celsius_Temp = input("Enter the value of the temperature in Celsius : ")
Fahrenheit_Temp = (float(Celsius_Temp)*(9/5)+32)
print(f"For the given Celsisus, the temperature in fahrenheit is : {Fahrenheit_Temp}")