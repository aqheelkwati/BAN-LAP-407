#  Create a dictionary where the key is an even number from the given list and the value
# will be the occurrence of that element in the list. input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]

x={}
input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]
input=sorted(input)
for i in input:
    if i in x:
        continue
    else:
        if i%2==0:
            x.update({i:0})
# print(x)

for key in x:
    x[key]=input.count(key)

# withot built in...........................................................
# for key in x:
#     count=0
#     for i in range(len(input)):
#         if input[i]==key:
#             count+=1
#         if input[i]==key+1:
#             break
#     x[key]=count

print(x)
