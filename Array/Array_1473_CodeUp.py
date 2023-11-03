#4:44~4:47
n,m = map(int,input().split())
s=n*m+1
k=s
ans=[]
temp=[]
for i in range(1,n+1):
    if i%2==1:
        s-=m
        for j in range(m):
            temp.append(s)
            s+=1
    elif i%2 ==0:
        s-=m
        k=s
        for j in range(m):
            s -= 1
            temp.append(s)
    ans.append(temp)
    temp=[]
for i in range(len(ans)):
# point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])