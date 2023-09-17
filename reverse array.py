array = [10,221,21,443,55,64,67]
size = len(array)
for i in range(size,-1):
    temp = array[i]
    array[i] = array[i + 1]
    array[i]