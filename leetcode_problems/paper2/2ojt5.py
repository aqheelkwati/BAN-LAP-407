# 5. Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’,
# ‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values 
# associated with keys in alphabetically sorted order.

Company={'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan',
 'Wipro':'Thierry Delaporte'}

l=sorted(Company.values(),reverse=1)
print(l)