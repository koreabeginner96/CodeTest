#3:26~3:35
n=int(input())
ans=[]
temp=[]
o=n
k=o
for i in range(n):
    for j in range(n):
        temp.append(o)
        o+=n
    ans.append(temp)
    k-=1
    o=k
    temp=[]
for i in range(len(ans)):
    #point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])