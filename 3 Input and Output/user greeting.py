#Create a program that takes the user's name as input and greets them with a personalized message.

name = input("Enter your name: ")
#approch 1
print(f"Welcome '{name }' to the Python Programing. ")
#another approch
print("Welcome, " +name+ " to the Python Programing.")

# Greet the user with a personalized message using string formatting
print("Hello, {}! Welcome to our program.".format(name))