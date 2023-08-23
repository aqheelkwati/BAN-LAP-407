
class HDFC:
    __acc_no_rec = 100000
    branch_name = 'BTM Layout'
    bank_name = 'HDFC Bank'
    ifsc = 'HDFC0001'
    
    def __init__(self, fname, lname, age, city, deposite):
        self.__account_no = self.__get_account_no()
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city
        self.amount = deposite
        
    def __get_account_no(cls):
        cls.__acc_no_rec += 1
        return cls.__acc_no_rec
    
    def __str__(self):
        return f""" ======= Customer Details =======       
        account_no: {self.__account_no}
        name: {self.fname} {self.lname}
        age: {self.age}
        city: {self.city}
        deposite: {self.amount}
        """
    
    def display_amount(self):
        print(f"Account bal is {self.amount}")
        print()
        
    def deposite(self, bal):
        self.amount += bal
        print("Amount Deposited Successfully")
        print()
        
    def withdraw(self, bal):
        self.amount += bal
        print("Amount Withdrawn Successfully")
        print()
    
        

# a = HDFC('Prabhu', 'Panda', 23, "BBSR", 5000)
# print(a)
# b = HDFC('Prabhu', 'Panda', 23, "BBSR", 5000)
# print(b)
cust = HDFC('Prabhu', 'Panda', 23, "BBSR", 5000)
print(cust)
cust.display_amount()
cust.deposite(1000)
print(cust)
cust.display_amount()
cust.withdraw(2000)
print(cust)
cust.display_amount()