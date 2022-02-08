#36
x={'key1': 1, 'key2': 3, 'key3': 2} 
y={'key1': 1, 'key2': 2}
for i  in x.items():
    for j in y.items():
        if i==j:
            print(i,"presnet in both")