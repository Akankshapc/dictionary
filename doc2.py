#doc2
b="w3resources"
a={}
count={}
for i in b:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for key in count:
    if count[key]>=1:
        a[key]=count[key]
print(a)
 