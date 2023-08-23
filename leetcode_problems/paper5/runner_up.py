n=5
l=[-1,-2, -2,-3, 8, 9]
l=list(set(l))
h=float('-inf')
sh=float('-inf')
for i in l:
    # print(i)
    if i>h:
        # print(h,sh)
        sh=h
        h=i
    else:
        if i>sh:
            sh=i
print(sh)

