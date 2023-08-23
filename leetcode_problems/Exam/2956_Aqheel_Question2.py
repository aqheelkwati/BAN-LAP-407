class Numbers:
    def add_digits(self,num):
        num=str(num)
        
        while len(num)>1:
            l=[int(i) for i in num]
            x=sum(l)
            num=str(x)
            
        return num
x=Numbers()
print(x.add_digits(68))
# print(x.add_digits(1245))