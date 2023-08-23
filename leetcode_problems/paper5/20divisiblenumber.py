# 20. Use a nested list comprehension to find all of the numbers from 1-1000 that are
# divisible by any single digit besides 1 (2-9)


num=[x for x in range(1,10) if  any (x%divisor==0 for divisor in range(2,10))]
print(num)
# n=[x if any(x%divisor==0 for divisor in range(2,10)) else 'Na' for x in range(1,10)]
# print(n)