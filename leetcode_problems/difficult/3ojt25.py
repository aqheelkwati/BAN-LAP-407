# # roman to numeric
# def get_romon(num, ints):
#     if not num:
#         return ''
    
#     for i in reversed(ints):    
#         if i <= num:
#             num = num - i
#             return romons[i] + get_romon(num, ints)

# romons = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 
#           40: 'IL', 50: 'L', 90: 'IC', 100: 'C', 400: 'ID', 500: 'D', 900: 'IM', 1000: 'M'}
# num = 1
# # num = 11
# # num = 9
# # num = 51
# num = 1002
# num = 2345

# print(get_romon(num, romons.keys()))
def int_to_roman(n):
    symlist=[['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100],
    ['CD',400],['D',500],['CM',900],['M',1000]]  
    s=''
    for sym,val in reversed(symlist):
        if n//val:
            count=n//val
            s+=count*sym
            n=n%val
    print(s)
int_to_roman(1500)