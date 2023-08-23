import pickle
dct={111:'eric'}

with open('18.txt','wb') as f:
    pickle.dump(dct,f)

with open('18.txt','rb') as f:
    d=pickle.load(f)
print(d)