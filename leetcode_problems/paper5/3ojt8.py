# 8.Write Row class that accepts any keyword arguments given to it and stores these arguments as attributes.

# Ex. >>> row = Row(a=1, b=2)
# >>> row.a 1
# >>> row.b 2
class Row:
    def __init__(self,**kwargs) -> None:
        self.__dict__.update(kwargs)

    def method1(self):
        print(self.__dict__)

x=Row(a=10,b=20)
x.method1()
print(x.a)



# "---------------OR-----------"
# class Row:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)