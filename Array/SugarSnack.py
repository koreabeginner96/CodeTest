# 24min
h,w= map(int,input().split())
m=[[0]*(w+1) for _ in range(h+1)]
ans=[[0]*w for _ in range(h)]
n= int(input())
for i in range(n):
    l,d,x,y= map(int,input().split())
    for i in range(l):
        # 가로는 0, 세로는 1
        if d == 0:
            m[x][y] = 1
            y+=1
        elif d == 1:
            m[x][y] = 1
            x+=1
for i in range(1,len(m)):
    for j in range(1,len(m[0])):
        ans[i-1][j-1]=m[i][j]
for i in range(len(ans)):
    print(ans[i])
