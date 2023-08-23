# 11.Write a function, last_lines, which returns lines in a given ASCII text file in reverse 
# order.
# For example, given the following file, my_file.txt:
#     This is a file 
#     This is line 2 
#     And this is line 3
# The last_lines function should work like this:

# >>> for line in last_lines('my_file.txt'):
# ...	print(line, end='')
# ...
#     And this is line 3  
#     This is line 2 
#     This is a file
def last_lines(f):
    with open(f'{f}','r') as f:
        x=f.read().splitlines() 
        x=x[::-1]
        return x
for line in last_lines('3ojt11.txt'):
    print(line)