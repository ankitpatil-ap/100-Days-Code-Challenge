#Simple Interest Calculator: Calculate and print the simple interest when principal, rate, and time are provided as input.

principal = int(input("Enter the Principal Amount: "))
rate = float(input("Enter Rate of Intrest: "))
Time = int(input("Enter Time is Years: "))

#Logic for Simple Intrest

Simple_Intrest = (principal*rate*Time)/100

print("Simple Intrest of Given Principal is: ",Simple_Intrest)

#Output
'''
Enter the Principal Amount: 100000
Enter Rate of Intrest: 10
Enter Time is Years: 2
Simple Intrest of Given Principal is:  20000.0
'''