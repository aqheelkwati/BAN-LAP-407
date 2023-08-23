class Numbers:
    def add_digits(self,num):
        num=str(num)
        sum=0
        while len(num)>1:
            for i in num:
                sum+=int(i)
            num=str(sum)
            sum=0

        return num
x=Numbers()
print(x.add_digits(68))
