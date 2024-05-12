import random
ls=[9,-3,5,2,6,8,-6,1,3]
def sort(ls,pv):
    newpv=pv[:]
    for x in newpv:
        pvt=ls[x]
        less=[]
        more=[]
        pvtls=[]
        for y in ls:
            if y<pvt:
                less.append(y)
            elif y>pvt:
                more.append(y)
            else:
                pvtls.append(y)
        ls=less+pvtls+more
        pv.append(len(less)-1)
    return [ls,pv]
def call(ls,pv):
    st=sort(ls,pv)
    ls=st[0]
    pv=st[1]
    if not check(ls):
        ls=call(ls,pv)
    return(ls)
def check(ls):
    check=True
    for i in range(len(ls)-2):
        if ls[i]>ls[i+1]:
            check=False
    return check

print(call(ls,[-1]))
ls=[]
for i in range(30):
    ls.append(random.randint(-20,20))
print(ls)
print(call(ls,[-1]))
