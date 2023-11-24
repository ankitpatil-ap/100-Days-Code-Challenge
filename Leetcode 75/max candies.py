kids = int(input())
candies = [int(input()) for _ in range(kids)]
#print(candies)
result = []

maxi = max(candies)
extraCandies = int(input())

for kidscandies in candies:
    if kidscandies + extraCandies>=maxi:
        result.append(True)
    else: 
        result.append(False)
    
print(result)