a=[-3,1,2,-2,5,6]
ans=[]
for i in range(len(a)):
    m=min(a)
    j=a.index(m)
    ans.append(m)
    a.pop(j)
b=ans.pop()
c=ans.pop()
d=ans.pop()
r=int(b*c*d)
print(r)