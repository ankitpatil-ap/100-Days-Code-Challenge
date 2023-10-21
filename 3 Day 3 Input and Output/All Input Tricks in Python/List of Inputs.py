#Accepting a list of inputs and converting them to a list.

number = [int(x) for x in input("Enter the Number seprate by space: ").split()]
print(number)

#Output
'''
Enter the Number seprate by space: 1 2 3 4 5 6 7 8 9 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''