# Find the palindrome words with the count value from the given string.Output should be in 
# form of dict. key will be palidrome word and value will be number of occurence.
# i/p given a string - 'Nittin & his mom went to a park last friday. His Mom observed that the weather
# was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331.'
# o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}
s='''Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. 
Nittin also met his sis. If we reverse the number 1331 then we also get 1331.'''
l=s.split()
# l.append('nittin')
# print(l)
d={}
for word in l:
    # word=word.lower()
    word=''.join(x.lower() for x in word if x.isalnum() )
    if word.isalnum() and len(word)>1:
        if word in d:
            d[word]+=1
            
        else:
            # print(word)
            if word[::-1]==word:
                d[word]=1
print(d)
