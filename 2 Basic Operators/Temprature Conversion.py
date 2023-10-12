#Temperature Converter: Write a program that converts a temperature in Celsius to Fahrenheit and vice versa.
Choice = input("Enter your Choice : \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius: \n")

if Choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit} °F")

    '''
print(): This is the standard Python function used to output text to the console.
f": The f before the opening quotation mark indicates the start of an f-string.
"Temperature in Fahrenheit: {fahrenheit} °F": This is the f-string itself. Inside the f-string,
curly braces {} are used to insert expressions or variables. 
In this case, {fahrenheit} is a
placeholder for the value of the fahrenheit variable.
{fahrenheit}: This is an expression inside the f-string that will be evaluated and replaced 
with the value of the fahrenheit variable when the string is formatted.
°F: This is a literal part of the string and will be displayed as is.
    '''
elif Choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius: {celsius} °C")
else:
    print("Invalid choice. Please choose 1 or 2.")

#Output

'''
 1. Celsius to Fahrenheit
 2. Fahrenheit to Celsius:
1
Enter temperature in Celsius: 100
Temperature in Fahrenheit: 212.0 °F
'''