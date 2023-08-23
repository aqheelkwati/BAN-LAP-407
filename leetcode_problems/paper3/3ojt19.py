# # 19.Write a function that takes two strings representing dates and returns the string that
# #  represents the earliest point in time ? Ex. get_earliest("01/27/1832", "01/27/1756") 
# #  return '01/27/1756'.

# def get_earliest(s1,s2):
#     l1=s1.split('/')[::-1]
#     l2=s2.split('/')[::-1]
    
#     for i in range(len(l1)):
#         if int(l1[i])>int(l2[i]):
#             return s2
#         elif int(l1[i])<int(l2[i]):
#             return s1
#         else:
#             continue
#     # return "Both are same date"
# print(get_earliest("01/27/1832", "01/27/1756"))
# print(get_earliest("01/17/1756", "01/28/1756"))
# print(get_earliest("05/28/1756", "01/28/1756"))
# print(get_earliest("01/28/1756", "01/28/1756"))

from datetime import datetime
def get_earliest(s1,s2):
    s1=datetime.strptime(s1,"%m/%d/%Y")
    s2=datetime.strptime(s2,"%m/%d/%Y")
    if s1<s2:
        return s1
    else:
        return s2

print(get_earliest("01/27/1832", "01/27/1756"))
print(get_earliest("01/17/1756", "01/28/1756"))
print(get_earliest("05/28/1756", "01/28/1756"))
print(get_earliest("01/28/1756", "01/28/1756"))