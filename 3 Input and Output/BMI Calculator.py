#BMI Calculator: Calculate and print the Body Mass Index (BMI) of a person when height and weight are given as input.

name, age = input("Enter your Name, Age: ").split()
input_values = input("Weight and Height in m (separated by space): ").split()
weight, height = map(float, input_values)


#Logic 
BMI = weight/(height*height)

print(f"Hello {name} your BMI is: {BMI:.2f}")