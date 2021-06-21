import random
x=10
list=[]
while x>0:
    a=random.randint(0,100)
    list.append(a)
    x=x-1
print(list)
def sort(list):
    r=len(list)
    while r>0:
        x=0
        y=1
        while y<len(list):
            a=list[x]
            b=list[y]
            if a>b:
                list[x]=b
                list[y]=a
            else:
                list[x]=a
            x=x+1
            y=y+1
        r=r-1
    print(list)
sort(list)