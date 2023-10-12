#Exponent Calculator: Create a program that calculates the result of raising a number to a given exponent.

#Exponent is mathematical term where we number denotes how much the the number is muliplyed by self.
#example 2^3 means 2*2*2 here 3 is an exponential and 2 is base

base = int(input("Enter the Number: "))
expo = int(input("Enter teh Exponent: "))

#logic

exponent = base ** expo

print("The Exponent Value of Given number is: ",exponent)

#output
'''
Enter the Number: 10
Enter teh Exponent: 3
The Exponent Value of Given number is:  1000'''