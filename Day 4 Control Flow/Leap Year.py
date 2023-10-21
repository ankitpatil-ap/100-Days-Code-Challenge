#Create a program that checks if a given year is a leap year or not.

Year = int(input("Enter the Year: "))

if Year%4 == 0:
    print(Year, " is Leap Year")
else:
    print(Year, " is non Leap Year")