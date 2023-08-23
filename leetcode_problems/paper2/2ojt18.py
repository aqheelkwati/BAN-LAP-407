# Print the below rohmbus pattern according to the given number
# for eg: given number is 4 then 
# o/p will be 
#   1
#  212
# 32123
# 4321234
# 32123 
#  212 
#   1

n=int(input())
s=n-1
pat=''
for num in range(1,n+1):
    if pat=='':
        pat+=str(num)
    else:
        pat=pat+str(num)
        pat=str(num)+pat
    # for j in range(s):
    #     print(' ',end='')
    print(s*' ',end='')
    print(pat)
    s-=1
s=1
for i in range(n-1):
    pat=pat[1:-1]
    for j in range(s):
        print(' ',end='')
    print(pat)
    s+=1
