#Data Type Detection: Create a program that takes an input and prints the data type of the input.

a = input("Enter the Value : ")
b = int(input("Enter the Value : "))
c = float(input("Enter the Value : "))

#logic to check data type
datatype1 = type(a)
datatype2 = type(b)
datatype3 = type(c)
print("Data type of Given Value is: ",datatype1)
print("Data type of Given Value is: ",datatype2)
print("Data type of Given Value is: ",datatype3)


#output
"""Enter the Value : Ankit
Enter the Value : 21
Enter the Value : 100.00
Data type of Given Value is:  <class 'str'>
Data type of Given Value is:  <class 'int'>
Data type of Given Value is:  <class 'float'>"""

#Python does not really have a syntax for multiline comments.
#Since Python will ignore string literals that are not assigned to a variable, 
#you can add a multiline string (triple quotes) in your code, and place your comment inside it