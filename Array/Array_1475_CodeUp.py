#3:28~4:12
n,m= map(int,input().split())
s=0
l=0
p=1
x=0
y=m-1
ans=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        s+=1
        if s==1:
            ans[x][y]=s
            continue
        elif s%n==1:
            y-=1
            p+=1
            ans[x][y]=s
            continue
        if p%2 == 1:
            x+=1
            ans[x][y]=s
        elif p%2 ==0:
            x-=1
            ans[x][y]=s
for i in range(len(ans)):
    #point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])