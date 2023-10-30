num1 = int(input())
num2 = int(input())


#By Euclidean Algoritham

'''
1. Suppose 2 numbers are their 48 and 18

step 1 divide 48 by 18 mark r and q here r becames 12 and q is 2
step 2 as r is not 0 so untill it became 0 we need to continue this step
step 3 now num1 became r and num2 became q now divie 12 by 2 here we get q as 6 and r as 0
step 4 so as r is 0 so 6 is the gcd of 48 and 18'''


while num2!=0:
   
    num1, num2 = num2, num1%num2   #both operation excuted simulentiouly as python supports it.
    

print(num1)
