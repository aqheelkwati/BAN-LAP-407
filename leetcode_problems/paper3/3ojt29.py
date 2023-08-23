# Write a function called interleave which accepts two iterables of any type and returns a 
# new iterable with each of the given items "interleaved" (item 0 from iterable 1, then item 0 
# from iterable 2, then item 1 from iterable 1, and so on).

def interleave(l1, l2):
    l=[]
    i,j=0,0
    while i<len(l1) and j<len(l2):
        l.append(l1[i])
        l1.pop(i)
        l.append(l2[j])
        l2.pop(j)
    #print(l1,l2) #l1=[] l2=[9]
    if l1:
        l=l+l1
    if l2:
        l=l+l2
    return l

print(interleave(['a','b','c','d'],[5,6,7,8,9]))

# def interleave(iterable1, iterable2):
#     return [val for pair in zip(iterable1, iterable2) for val in pair]
