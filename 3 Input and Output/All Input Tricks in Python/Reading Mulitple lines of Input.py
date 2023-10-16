#Reading Multiple lines of input(until a specific condition) and storing them in a list.

lines = []

while True:

    line = input("Enter the data or press 'q' to exit. ")
    if line=='q':
        break
    lines.append(line)

print(lines)

    #Output
'''
Enter the data or press 'q' to exit. 1
Enter the data or press 'q' to exit. 2
Enter the data or press 'q' to exit. 3
Enter the data or press 'q' to exit. 4
Enter the data or press 'q' to exit. 5
Enter the data or press 'q' to exit. q
['1', '2', '3', '4', '5']
    '''
