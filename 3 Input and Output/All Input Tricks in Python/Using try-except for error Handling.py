#Adding error handling for invalid inputs:

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please Enter a valid number.")


#output
'''
Enter a number: 10
PS C:\Users\ankit\OneDrive\Desktop\100 Days Code Challenge> python -u "c:\Users\ankit\OneDrive\Desktop\100 Days Code Challenge\100-Days-Code-Challenge\3 Input and Output\All Input Tricks in Python\Using try-except for error Handling.py"
Enter a number: q
Invalid input. Please Enter a valid number.
'''