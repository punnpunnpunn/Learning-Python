matrix=[]
for y in range(10):
    list=[]
    for x in range(10):
        list.append(x+(y*10))
    matrix.append(list)
print(matrix)