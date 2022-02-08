#40
a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
lst=[]
dic2={}
for i in range(len(a)):
    dic1={}
    dic1[b[i]]=c[i]
    dic2[a[i]]=dic1
lst.append(dic2)
print(lst)
