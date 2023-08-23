l=[4,3,2,8,5,4511,4,5,9,0,9,7,1,1,6,3,6]
# l=[0,0,0,1,1,1,2,2,2,3,3,3,9]

# 1st way: Using typecasting
# l=list(set(l))
# print(l)

#2nd way: Using for loop & extra list
s=[]
for i in l:
    if i not in s:
        s+=[i]
print(s)

#3rd way: without using extra list

i=0
while i<len(l):
    while( l[i] in l[i+1::]):  #if condition checks only once thus removing single duplicate 
        l.remove(l[i])
    i+=1
print(sorted(l))