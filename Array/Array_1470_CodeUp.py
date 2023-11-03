#3:52 ~ 4:16
n=int(input())
o=1
l=0
k=o
p=0
ans=[[]*n for i in range(n)]
#0
ans[l].append(1)
for i in range(2,(n*n)+1):
    if i % n == 1:
        p+=1
        ans[l].append(i)
        continue
    if p%2 == 0:
        #1
        l += 1
        ans[l].append(i)
    elif p%2 == 1:
        l -= 1
        ans[l].append(i)
for i in range(len(ans)):
    #point *을 사용하면 괄호를 없앨 수있다.
    print(*ans[i])