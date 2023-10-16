#Utilizing list comprehensions for quick input procesing.

numbers = [int(x) for x in input("enter the numbers: ").split()]
print(numbers)


#output
'''
enter the numbers: 1 2 3 4
[1, 2, 3, 4]
'''