# 6.Write a function to_percent which accepts a number representing a ratio and returns 
# a string representing the percentage representation of the number to one decimal place.

def to_percent(r):
    return f'{r*100:.1f}'

print(to_percent(0.7512356))
print(to_percent(3.3/12))