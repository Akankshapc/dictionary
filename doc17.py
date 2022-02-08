#24
sample=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
c={}
for x in sample:
    if x["item"] not in c:
        c[x["item"]]=x["amount"]
    else:
        c[x["item"]]=x["amount"]
print(c)
