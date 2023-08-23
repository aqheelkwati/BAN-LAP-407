# Define a function which returns dictionary that stores the words and it’s length from
# the given text
# text = “Be happy”
# Expected Output : {"Be":2,”happy”:5}

text='Be happy'
def func(t):
    d={}
    l=[]
    t+=' '
    x=''
    for i in t:
        if i==' ':
            l.append(x)
            x=''
        else:
            x=x+i
    for i in l:
        d[i]=len(i)

    return d
    # for i in t:
    #     if i!=' ':
    #         x=x+i
    #     else:
    #         l.append(x)
    #         x=''
    

print(func(text))
            

