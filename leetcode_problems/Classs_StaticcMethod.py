class person:
    name="PESITMS"                      #11111111111111 Class Attribute
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def method0(self):                  # Instance Method : has access to both class & instance attributes
        print(f"Name is {self.name}")

    @classmethod                        #11111111111111 Class Method: Has access to class attributes only
    def method1(cls,name):
        print(cls)
        # print(cls.name)
        # cls.name=name
        # print("newname:", cls.name)
    @staticmethod                       # 222222222222 Static Metod: Has access to no Attributes
    def method2(name,year):
        print(f"name is {name}, year is {year}")

p1=person("adarsh",12)
p1.method0()
p1.method1("PES")
print(p1, person)
# p1.method2('akash','1999')
# OR
# person.method2('akash','1999')