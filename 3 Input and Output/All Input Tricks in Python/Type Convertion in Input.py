#Converting the input to a specific data type like int , float.

num = int(input("Enter the Number or an Integer: "))

#if we enter string here it will give this error so you must enter number after specifiy int

#Enter the Number or an Integer: A
#Traceback (most recent call last):
#  File "c:\Users\ankit\OneDrive\Desktop\100 Days Code Challenge\100-Days-Code-Challenge\Input and Output\All Input Tricks in Python\Type Convertion in Input.py", line 3, in <module>
#    num = int(input("Enter the Number or an Integer: "))
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#ValueError: invalid literal for int() with base 10: 'A' 



num2 = float(input("Enter you percent in decimal format: "))
#Output
'''
Enter the Number or an Integer: 10
Enter you percent in decimal format: 99.99
'''