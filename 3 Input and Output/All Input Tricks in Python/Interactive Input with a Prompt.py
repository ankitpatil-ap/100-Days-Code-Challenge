#Creating Interactife input with a prompt and default Values.

# Real-Life Problem: User Registration Greeting

# Default name for guests
default_name = "Guest"

# Prompt the user for input
user_name = input(f"Hello! Please enter your name [{default_name}]: ") or default_name

# Greet the user with their name (or default name)
print("Welcome, " + user_name + "! Thank you for signing up.")
