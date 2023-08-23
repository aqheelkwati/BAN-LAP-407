#You are given a string having alphabets,digits,special characters. Write three different functions 
# to extract the digits[should be in sorted order], special character & vowels[should be in reverse] 
# from the given string.
# i/p string : "abcd123bye09@8"
# o/p: digits - 012389
#  special character - @
#  vowels - ea 
def digits(s):
    d=''.join(sorted((filter(lambda x:x.isdigit(),s))))
    print(d)
def special_char(s):
    sp=''.join(filter(lambda x:not x.isalnum(),s))
    print(sp)
def vowels(s):
    v=''.join(sorted(filter(lambda x: x in 'aeiouAEIOU',s),reverse=1))
    print(v)
digits('abcd123bye09@8')
special_char('abcd123bye09@8')
vowels('abcd123bye09@8')