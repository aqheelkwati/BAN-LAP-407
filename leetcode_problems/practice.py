# class person:
#     # citezen='india'
#     def __init__(self):
#         self.name='mub'
#         self.age=25
    
#     def details(self):
#         print(f'The Name and age of the person is {self.name} and {self.age}')

# class employee(person):
#     def __init__(self,empid):
#         super().__init__()
#         # person.__init__(self)
#         self.empid=empid
    
#     def details(self):
#         print(self.name,self.age,self.empid)

# class student(employee):
#     def __init__(self, empid,stdid):
#         # super().__init__(empid)
#         employee.__init__(self,empid)
#         self.stdid=stdid
# # p1=person('mubashir','25')
# # p1.details()
# p2=employee(2956)
# p2.details() 
# p3=student(2956,12)
# p3.details()

symlist=[['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100],
    ['CD',400],['D',500],['CM',900],['M',1000]] 
n=int(input())
s=''
for sym,val in reversed(symlist):
    count=n//val
    if count:
        s+=count*sym
        n=n%val
print(s)