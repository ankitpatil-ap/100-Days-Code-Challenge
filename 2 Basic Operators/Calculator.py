#Arithmetic Calculator: Build a simple calculator that can perform addition, subtraction, multiplication, and division.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operation = input("Choose the Operation +,-,*,/: ")

#logic for calculator

if (operation == '+'):
    print("Addition of given Numbers is: ", num1+num2)
elif (operation == '-'):
    print("Substraction of Given Numbers is: ", num1-num2)
elif (operation == '*'):
    print("Multiplication of Given Numbers is: ", num1*num2)
elif (operation == '/'):
    print("Division of Given Numbers is: ", num1/num2)
else:
    print("Invalid Number. ")


#Output
'''
Enter First Number: 100
Enter Second Number: 1
Choose the Operation +,-,*,/: /
Division of Given Numbers is:  100.0'''