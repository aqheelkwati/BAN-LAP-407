# 5. From given list of numbers, create a list of square of prime numbers .
# l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]
def is_prime(num):
    if num <= 2:
        return False
    # To check if num is divisible by any number b/w 2 & sqrt of that number
    for i in range(2,int(num**2)+1):
        if num % i==0:
            return False
    return True

def Prime_squares(l):
    l2=[]
    for i in l:
        if is_prime(i):
            l2.append(i**2)
    print(l2)
l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]