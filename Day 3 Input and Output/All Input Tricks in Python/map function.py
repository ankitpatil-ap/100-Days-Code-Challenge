
name, age = input("Enter your Name, Age: ").split()
#map function
input_values = input("Weight and Height in m (separated by space): ").split()
weight, height = map(float, input_values)


#Logic 
BMI = weight/(height*height)

print(f"Hello {name} your BMI is: {BMI:.2f}")

'''
The map() function in Python is a built-in function that applies a specified function to each 
item in an iterable (like a list, tuple, etc.) and returns an iterator that yields the results 
of applying the function.

Here's the syntax of the map() function:
'''

#map(function, iterable)
'''
function: The function to apply to each item in the iterable.
iterable: An iterable (e.g., a list, tuple) whose items will be processed by the function.
Usage and Purpose:

map() is useful when you want to apply the same function to every element in an iterable, avoiding the need for explicit loops.
It's a way to efficiently transform data without writing repetitive loop code.
'''