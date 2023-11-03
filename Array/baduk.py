l=[[0]*20 for _ in range(20)]
ans=[[0]*19 for _ in range(19)]
n=int(input())
for i in range(n):
    a,b= map(int,input().split())
    l[a][b]=1
for i in range(1,len(l)):
    for j in range(1,len(l[0])):
        ans[i-1][j-1]=l[i][j]
for i in range(len(ans)):
    print(ans[i])