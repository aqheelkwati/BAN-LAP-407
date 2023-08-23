# Write a program to extract the words starting with lowercase letter present in the list. 
# [‘Nissan’,‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]
cars=['Nissan','maruti','hyundai','Volkswagen','audi','honda']
# l=[x for x in cars if ord('a')<=ord(x[0])<=ord('z')]
l=[x for x in cars if x[0].islower()]
# l=[x if x[0].islower() for x in cars]  # can use this syntax only with else part
print(l)