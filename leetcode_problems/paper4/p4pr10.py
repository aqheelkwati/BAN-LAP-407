# 10.Generate a dictionary from the two given lists using dict function (without using for loops) and calculate the sum of all the values in the dictionary using reduce and anonymous concepts
# L1 = [“a”,”b”]	L2 = [1,2]

# Expected Output :

# data = {“a'.1, “b'.2} sum = 3
from functools import reduce

l1=['a','b']
l2=[1,2]
d=dict(zip(l1,l2))
# sum=reduce(lambda x,y : x+y, d.values())
print('data =',d,'\n','sum=',sum)
l=list(d.values())
print(l)
print(sum(l))