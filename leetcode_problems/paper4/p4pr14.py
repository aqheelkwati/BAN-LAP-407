import json

with open('a.json','rb') as j:
    # print(type(j.read()))
    x=json.load(j)
    print(x,type(x))