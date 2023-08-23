# 7 .Reverse the below string without changing the 
# position of special characters . s = "adfw$vf&yvy*ugv%uy" 
s = "adfw$vf&yvy*ugv%uy" 
# l=[]
# op=[]
# for i,ele in enumerate(s):
#     if ele.isalpha():
#         op.append(ele)
#     else:
#         l.extend([i,ele])
# op=op[::-1]
# for i in range(0,len(l),2):
#     op.insert(l[i],l[i+1])
# op=''.join(op)
# print(s)
# print(op)

#................OR..............
print(s)
s=list(s)
left=0
right=len(s)-1
while left<right:
    if not s[left].isalpha():
        left+=1
    elif not s[right].isalpha():
        right-=1
    else:
        s[right],s[left]=s[left],s[right]
        left+=1
        right-=1
print(''.join(s))

# ------
# s = "adfw$vf&yvy*ugv%uy"
# s=list(s) 
# l=0
# r=len(s)-1
# while l<r:
#     if not s[l].isalnum():
#         l+=1
#     elif not s[r].isalnum():
#         r-=1
#     else:
#         s[l],s[r]=s[r],s[l]
#         l+=1
#         r-=1
# print(''.join(s))