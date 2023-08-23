# 3.Write a function called interleave which accepts two iterables of any type and returns a 
# new iterable with each of the given items "interleaved" (item 0 from iterable 1, then item 0 
# from iterable 2, then item 1 from iterable 1, and so on).
# An assumption here that both iterables contain the same number of elements.
# def interleave(l1,l2):
#     l3=[]
#     if len(l1)!=len(l2):
#         return 'The given lists are of different sizes'
#     for i in range(len(l1)):
#         l3.extend([l1[i],l2[i]])
#     return l3

# l1=[1,2,3,4] 
# l2=['a','b','c']
# print(interleave(l1,l2))

def interleave(iterable1, iterable2):
    return [val for pair in zip(iterable1, iterable2) for val in pair]
l1=[1,2,3] 
l2=['a','b','c']
print(interleave(l1,l2))

# print(list(zip(l1,l2)))
# print({x:x for pair in zip(l1,l2) for x in pair})