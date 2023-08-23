# You are given a string and width. Your task is to wrap the string into paragraph of width in 
# reverse order. Blank spaces should be ignored.
# for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this 
# organisation.
#  the second line conatins the width - 4
#  o/p
# lleH
# ew,o
# mocl
# tote
# osih
# nagr
# tasi
# .noi

def func(s,n):
    i=0
    x=''
    for char in s:
        if char==' ':
            continue
        else:
            x+=char
            i+=1
            if i==n:
                print(x[::-1])
                x=''
                i=0
func('Hello, welcome to this organisation.',5)
             