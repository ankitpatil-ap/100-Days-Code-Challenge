x = 5
y = "Hello World"

try:
    z = x + y
except TypeError:
    print("Error: cannot be added string and number")