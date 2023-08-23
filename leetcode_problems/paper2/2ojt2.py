# Given a list of first 10 natural numbers, write a program to find the square of all even
# numbers and cube of all odd numbers and store them in another list

l=[1,2,3,4,5,6,7,8,9,10]
# def func(l):
#     op=[]
#     for i in l:
#         if i%2==0:
#             op.append(i**2)
#         else:
#             op.append(i**3)
#     return op

# print(func(l))
print([x**2 if x%2==0 else x**3 for x in l])