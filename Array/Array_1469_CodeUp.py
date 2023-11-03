#3:44~3:50
n=int(input())
o=1
k=o
ans=[]
temp=[]

for i in range(1,n+1):
    if i%2 == 1:
        o+=n
        for j in range(n):
            o-=1
            temp.append(o)
    elif i%2 == 0:
        o+=n
        for j in range(n):
            temp.append(o)
            o += 1
    ans.append(temp)
    temp=[]
for i in range(len(ans)):
    #point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])