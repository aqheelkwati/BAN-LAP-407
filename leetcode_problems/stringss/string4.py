
#P4. Write a program to reverse internal content of each word:
# s = "MSys Technologies Software Company"
#output = "sySM seigolonhceT erawtfoS ynapmoC"

s = "MSys Technologies Software Company"
l=s.split(' ')
for i in range(len(l)):
    l[i]=l[i][::-1]
op=' '.join(l)
print(op)