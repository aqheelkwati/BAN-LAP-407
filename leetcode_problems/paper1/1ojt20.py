# Write a python program for sort the given below list 
# based last character of each word names_list = ['Prabhu', Rahul', 'Arunesh, 'Sonali', 'Rakshit']

l=['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']
# d={}   
# for i in range(len(l)):
#     d.update({l[i][-1]:l[i]})  #This makes d={'u': 'Prabhu', 'l': 'Rahul', 'h': 'Arunesh', 'i': 'Sonali', 't': 'Rakshit'}
#     l[i]=l[i][-1] # This makes l=['u', 'l', 'h', 'i', 't']
# l.sort()
# for i in range(len(l)):
#     l[i]=d[l[i]]
# print(l[::-1])
print(sorted(l,key=lambda x:x[-1]))