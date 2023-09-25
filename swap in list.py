def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [23,45,67,88,104]
pos1,pos2 = 1, 3