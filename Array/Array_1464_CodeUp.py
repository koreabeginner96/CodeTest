#3:40 ~ 3:44
n,m = map(int,input().split())
s=n*m
ans=[]
temp=[]
o=s

for i in range(n):
    for j in range(m):
        temp.append(o)
        o-=1
    ans.append(temp)
    temp=[]
for i in range(len(ans)):
    #point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])