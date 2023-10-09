#Create a basic calculator program.
a = int(input())
b = int(input())
c = input()

if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
elif c == '%':
    print(a%b)
else:
    print("Invalid Number")