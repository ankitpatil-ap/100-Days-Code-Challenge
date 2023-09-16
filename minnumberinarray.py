
def minnum(array):
    minnumber = array[0]
    size = len(array)
    for i in range(size):
        
        if (array[i] < minnumber):
            minnumber = array[i]
    return minnumber
array = [22,1,2,3,4,4,555,3,223,44]
print(minnum(array))
