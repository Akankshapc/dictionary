#max1,max2,max3#
my_dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20
}
max1=0
max2=0
max3=0
for i in my_dict:
    for j in my_dict:
        if my_dict [i]>max1:
            max1=my_dict[i]
            temp1=i
        elif max1>my_dict[j] and max2<my_dict[j]:
            max2=my_dict[j]
            temp2=j
        elif max2>my_dict[j] and max3<my_dict[j]:
            max3=my_dict[j]
            temp3=j
print("max1",temp1,max1)
print("max2",temp2,max2)
print("max3",temp3,max3)