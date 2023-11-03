#3:55~3:57
n,m = map(int,input().split())
s=n*m
ans=[]
temp=[]
o=s
k=o

for i in range(n):
    for j in range(m):
        temp.append(o)
        o-=n
    ans.append(temp)
    k-=1
    o=k
    temp=[]
for i in range(len(ans)):
    #point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])