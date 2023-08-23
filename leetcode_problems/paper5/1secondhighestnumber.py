l=[4,3,2,8,5,4511,4,5,9,0,9,7,1,6]
s=list(set(l)) # To remove Duplicat elements from list

#Using any sorting algorithm to sort
for i in range(len(s)-1):
    for j in range(len(s)-1):
        if s[j+1]<s[j]:
            s[j],s[j+1]=s[j+1],s[j]
# print(s)

print(f"The second highest element of the list is {s[-2]}")

#...................OR..........
l=[4,3,2,8,5,4511,4,5,9,0,9,7,1,6]
second=maximum=0
for num in l:
    if num>maximum:
        second=maximum
        maximum=num
    else:
        if num>second:
            second=num
print(second)










