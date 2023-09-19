print("Choose the option 1. Square \n 2. Circle \n 3. Reactangle. Just enter the number")
shape = int(input())
if shape == 1:
    print("Enter lenght or Breath of Square")
    squareside = int(input())
    areaofsquare = squareside*squareside
    print("Area of Square is:",areaofsquare)
elif shape == 2:
    print("Enter size of Radius of Circle.")
    radius = int(input())
    pi = 3.14
    areaofcircle = pi*(radius*radius)
    print("Area of Circle is :",areaofcircle)
elif shape == 3:
    print("Enter Length and Breath of Rectangle.")
    length = int(input())
    breadth = int(input())
    areaofrect = length*breadth
    print("Area of Rectangle is :",areaofrect)