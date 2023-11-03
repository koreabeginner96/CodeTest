#3:47~3:50
n,m = map(int,input().split())
s=n*m
ans=[]
temp=[]
o=(s+1)-m
k=o

for i in range(n):
    for j in range(m):
        temp.append(o)
        o+=1
    ans.append(temp)
    k-=m
    o=k
    temp=[]
for i in range(len(ans)):
    #point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])