# 3 Define logic for identifying the even numbers and odd numbers from the given list and
# generate a dictionary as follows
# numbers = [4,5,7,2,9,8]
# result = {“even”:[4,2,8],"odd":[5,7,9]}
n = [4,5,7,2,9,8]
# def separator(n):
#     d={'even':[],'odd':[]}
#     for i in n:
#         if i%2==0:
#             d['even'].append(i)
#         else:
#             d['odd'].append(i)
#     return d

def separator(n):
    d={}
    for i in n:
        if i%2==0:
            if 'even' in d:
                d['even'].append(i)
            else:
                d['even']=[i]
        else:
            if 'odd' in d:
                d['odd'].append(i)
            else:
                d['odd']=[i]
    return d
print('result = ',separator(n))
print({'even':[i for i in n if i%2==0],'odd':[i for i in n if i%2!=0]})