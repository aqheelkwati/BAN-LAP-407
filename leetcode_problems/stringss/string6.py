#P6. write a program to sort the characters of the string as first alphabet symbols followed by numeric values

x='aassw23<4/?5#$R>DE#$R,D#$1.3'
a=''
n=''
s=''
for i in x:
    if i.isalpha(): # or {64<ord(i)<91 or 96<ord(i)<123}
        a=a+i
    elif i.isnumeric():
        n=n+i
    else:
        s=s+i
print(a+n+s)

