# 12. Write a Python Program to Reverse the Content of a File.
# Input :-
# I am
# new to this
# world of
# Python. Output :- Python.world of
# new to this
# I am
f=open('f2.txt','r')
l=f.readlines()
f.close()
l=l[::-1]
# print(l)
f=open('f2.txt','w')
for i in l:
    f.write(i)
f.close()
# with open('f2.txt','r') as f:
#     x=f.readlines()
# print(x)