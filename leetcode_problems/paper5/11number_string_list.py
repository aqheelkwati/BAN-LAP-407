# 11. From the given list, check if the element is an integer then return square of that
# element and if element is a string then return the same string 2 times. Output should
# be in list format. a = [8,9,10,"f",5,8,"d"]
# Output should be : [64, 81, 100, 'ff', 25, 64, 'dd']
a = [8,9,10,'f',5,8,'d']

def func(l):
    ls=[]
    for i in l:
        if type(i) is int:
            ls.append(i*i)
        else:
            ls.append(i*2)
    return ls

print(func(a))
#OR
print([x**2 if type(x) is int else x*2 for x in a] )