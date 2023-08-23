# 12.Write a function called parse_ranges, which accepts a string containing ranges of numbers 
# and returns an iterable of those numbers.
# Ex: >>> parse_ranges('1-2,4-4,8-13') [1, 2, 4, 8, 9, 10, 11, 12, 13]
def parse_ranges(s):
    op=[] 
    ranges=s.split(',') #['1-2']
    print(ranges)
    for r in ranges:
        # digits=r.split('-')
        # for dig in range(int(digits[0]),int(digits[1])+1):
        start,end=r.split('-')
        for dig in range(int(start),int(end)+1):
            op.append(dig)

    print(op)
parse_ranges('1-2,4-4,8-13')