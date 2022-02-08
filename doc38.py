#38
dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
c=0
d={}
for key in dic:
    if c==2:
        break
    else:
        d[key]=dic[key]
        c=c+1
print(d)