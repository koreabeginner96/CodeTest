n,m= map(int,input().split())
cnt=1
ans=[[0]*m for _ in range(n)]
for k in range(n+m-1):
    x=-1
    y=0
    while x!=n and y!=m:
        x+=1
        if x+y==k:
            ans[x][y]=cnt
            cnt+=1
        if x==n-1:
            y+=1
            x=-1
for i in range(n):
    print(*ans[i])