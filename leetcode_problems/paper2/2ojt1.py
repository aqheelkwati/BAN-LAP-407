# Write a program to reverse a number without using any inbuit function.

def reverse_num(n):
    op=0  #123
    while n>0:
        r=n%10
        op=(op*10)+r
        n=n//10
    return op
    # or 
    # return str(n)[::-1]
    


print(reverse_num(1243))
