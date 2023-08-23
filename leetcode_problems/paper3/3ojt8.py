# 8.Write Row class that accepts any keyword arguments given to it and stores these arguments as attributes.

# Ex. >>> row = Row(a=1, b=2)
# >>> row.a 1
# >>> row.b 2
class Row:
    def __init__(self,a,b):
        # self.__dict__.update(kwargs)
        self.a=a
        self.b=b

    def method1(self):
        print(self.__dict__)

class column(Row):
    def __init__(self, a, b):
        super().__init__(a, b)

# x=Row(a=10,b=20)
y=column(12,14)
y.method1()
print(y.a)



"---------------OR-----------"
class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)