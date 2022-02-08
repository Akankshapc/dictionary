#26
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print("c1","c2","c3")
a=my_dict.get("C1")
b=my_dict.get("C2")
c=my_dict.get("C3")
i=0
while i<len(my_dict):
    print(a[i],"",b[i],"",c[i])
    i=i+1
