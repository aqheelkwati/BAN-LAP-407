# 25.Define a logic to print the combinations from the two the below input data Input :

# 'Department“. ['Bakkt’, 'Cisco'],

# ’Team’	: [’Red’, ’Yellow’, ’Black’]

# Output :

# { ’Department“. ‘Bakkt’, ’Team“. ’Red’},

# { ’Department“. ‘Bakkt’, 'Team“. ’Yellow’}

# { ’Department“. ‘Bakkt’, 'Team“. ’Block’}

# { ’Department“. ‘Cisco’, ’Team“. ’Red’}

# { ’Department“. ‘Cisco’, ’Team“. ’Block’}

# { ’Department“. ‘Cisco’, ’Team': ’Yellow’}

department=['Bakkt', 'Cisco']
team=['Red','Yelow','Black']
d={}
for i in department:
    
    for j in team:
        d['department']=i
        d['team']=j
        print(d)