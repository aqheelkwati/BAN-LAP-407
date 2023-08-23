# 19.Define a generator to print the numbers between o to n (including) 
# which are divisible by 5 and should be even
def gen(n):
    i=1
    while i<n+1:
        if i%5==0 and i%2==0 :
            yield i
        i+=1

g=gen(40)
# print(list(g))
for i in g:
    print(i)