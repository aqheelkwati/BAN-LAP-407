# l=[4,3,2,8,5,4511,4,5,9,0,9,7,1,6]
# max,sec_max=0,0
# for i in l:
#     if i>max:
#         sec_max=max
#         max=i
#     else:
#         if i>sec_max:
#             sec_max=i
# print(sec_max)
# print(sorted(l))
#...............................................................................................
field=["Place ","Food ","price(per plate) ","ratings(out of 10) "]
rows=[['blore ','bisibele bath ','200 ','4.5 ',],
        ['blore ','bisibele bath ','200 ','4.5 ']
        ]
with open('practice.txt','w+') as f:
    f.writelines(field)
    f.write('\n')
    for l in rows:
        f.writelines(l)
        f.write('\n')
with open('practice.txt','r') as f:
    print(f.read())
