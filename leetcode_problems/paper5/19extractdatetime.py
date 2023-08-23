# 19. Write a Python program to extract year, month, date and time using Lambda.
# I/p:
# 2020-01-15 09:03:32.744178
# O/p :
# Year : 2020
# Month : 1
# Day : 15
# Time : 09:03:32.744178
a=lambda x: f' Year:{x[:4]}\n Month:{x[5:7]}\n Day:{x[8:10]}\n Time:{x[11:]}'

print(a('2020-01-15 09:03:32.744178'))
b=lambda x: x.split()
# x,y=b('2020-01-15 09:03:32.744178')
# print(x,'k',y)