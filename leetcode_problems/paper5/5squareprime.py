# From given list of numbers, create a list of square of prime numbers .
# l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]

l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]
# l1=[x for x in range(100)]

def primesquare(l):
    p=[]
    for i in l:
        c=0
        if i==1 or i==0:
            continue
        for j in range(2,(i//2)+1):
            if i%j==0:
                c+=1
                break
        if not c:
            p.append(i**2)
    print(p)
primesquare(l1)