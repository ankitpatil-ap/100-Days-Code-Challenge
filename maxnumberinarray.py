#Program to find max number in array
def maxnum(array):            
    maxnumber = array[0]    #maxnumber is the number which we need to find out so here we assume arrays 0 position as max number
    size = len(array)       #len function will give us exact size of array

    for i in range(size):      #this loop will iterate till the size of array
        if (array[i]>maxnumber):   #this condition checks if index of array element is greather than the max number which we assume
            maxnumber= array[i]     #if the number is greater then and only then this statement will update the index of maxnumber
    return maxnumber               #after all iterations we will get max number which will we be store in maxnumber varible.


array = [10,33,42,55,223,13,666,7777,10000,2,1]
print(maxnum(array))