# In the given String -- ‘MsYs TecHNOlogiEs iS a gREat place To woRk’ find the count of
# lowercase and uppercase letters.
s='MsYs TecHNOlogiEs iS a gREat place To woRk'
upper_count,lower_count=0,0
for char in s:
    if char.isupper():
        upper_count+=1
    elif char.islower():
        lower_count+=1
    else:
        continue
print(f'Upper Count={upper_count},Lower count={lower_count}')
        
