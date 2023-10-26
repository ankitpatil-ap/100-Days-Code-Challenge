class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []   #create empty list to store alternate letters
        i, j = 0, 0  #pointer initialize now as 0

        while i < len(word1) and j < len(word2):    #i will iterate upte lenght of word1 same with j and will run simultensiouly.
            merged.append(word1[i])    # it will keeps appending until the word1 lenght is over
            i = i + 1                   #increment pointer to access and fetch current item as location
            merged.append(word2[j])  #same like above
            j = j + 1

        while i < len(word1):                     #now this will ensure if any keywrods reamining that will be attached to back side of it
            merged.append(word1[i])
            i = i + 1                              #icrement by 1

        while j < len(word2):
            merged.append(word2[j])                #it will apend remaining letter from stirngs.
            j = j + 1                               #increment by 1

        return (''.join(merged))          #it returns proper string which is joined as requied


word1 = input()
word2 = input()

solution = Solution()
merged_string = solution.mergeAlternately(word1,word2)
print(merged_string)


#solution using lambda function 
'''
merge_alternately = lambda word1, word2: ''.join(
    c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue='')
)

from itertools import zip_longest

word1 = input()
word2 = input()
merged_string = merge_alternately(word1, word2)
print(merged_string)'''
