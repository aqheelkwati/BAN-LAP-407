# 13.Write a function that accepts a string containing lines of numbers and returns a list of
#  lists of numbers. Ex. matrix_from_string("3 4 5")
# [[3.0, 4.0, 5.0]]

def matrix_from_string(s):
    op=[]
    for char in s:
        if char.isnumeric():
               op.append(float(char))
    return [op]
print(matrix_from_string("3 4 5"))