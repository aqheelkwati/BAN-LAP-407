import random
import string

n= 10
upper=string.ascii_uppercase
lower=string.ascii_lowercase
digits=string.digits
sym=string.punctuation
print(upper,lower,digits,sym)
all=upper+lower+digits+sym
for i in range(10):
    op=random.sample(all,n)      # doesnt take combination of all, just selects any character
    print(''.join(op))
# s={upper,lower,digits,sym}
# print(s)