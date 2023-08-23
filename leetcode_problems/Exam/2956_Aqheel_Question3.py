x="Nittin and his mom went to park last friday Nittin's mom observed that the weather was too cool If we reverse the number 1331 then we aslo get 1331"
#x =input()
d={}
x=x.split(' ')
for word in x:
    word=''.join(i.lower() for i in word if i.isalnum())
    # print(word)
    if word==word[::-1] and len(word)>1:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
print(sum(d.values()),d)

# #....................TO GET EXACT OUTPUT AS SHOWN IN QUESTION..................
# t=[]
# for key,value in d.items():
#     t.append(f'{key}- {value} time')
# print(sum(d.values()),tuple(t))    