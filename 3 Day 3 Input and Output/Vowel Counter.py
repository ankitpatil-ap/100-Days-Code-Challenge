#Vowel Counter: Write a program that counts and prints the number of vowels in a given string.

# Get the input string from the user
user_input = input("Enter a string: ")

# Count the number of vowels using list comprehension and count() method
num_vowels = sum(user_input.count(vowel) for vowel in 'aeiouAEIOU')

# Print the number of vowels
print("Number of vowels:", num_vowels)


#this program will print only vowels and 
# #

###other letters will be ignored.
