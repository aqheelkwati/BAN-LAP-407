# def is_iterator(l):
#     try:
#         next(l)
#         return True
#     except:
#         return False
# print(is_iterator(iter([1,2])))
# print(is_iterator([1,2,3]))
x=iter([])
y=[]
print(dir(x))
if '__iter__' in dir(x) and '__next__' in dir(x):
    print(True)
if '__iter__' in dir(y) and '__next__' in dir(y):
    print(True)
else:
    print(False)


