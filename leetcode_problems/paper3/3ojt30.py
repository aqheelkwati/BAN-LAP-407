# 30.Convert each list element to a key-value pair. ex:
# Input : test_list = [2323, 82, 129388, 95]
# Output : {23: 23, 8: 2, 129: 388, 9: 5}
test_list = [2323, 82, 129388, 95]
def ListToDict(l):
    d={}
    
    for item in l:
        item=str(item)
        n=len(item)//2
        d[int(item[:n])]=int(item[n:])
    print(d)
ListToDict(test_list)