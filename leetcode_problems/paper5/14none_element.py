# 14. In the given list, check if the element is None, replace it with the recent value .
# l = [1,None,None,3,None,4]
# Output should be : [1,1,1,3,3,4]
l = [1,None,None,3,None,4]
for i in range(len(l)):
    if not l[i]:
        l[i]=l[i-1]
print(l)