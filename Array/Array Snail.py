n=int(input())
ans=[[0]*n for _ in range(n)]
cx=int(n//2)
cy=int(n//2)
cnt=0
k=1
temp=[(cx,cy)]
tx, ty = 0, 0
while cnt<n*n:
    cnt+=1
    x,y=temp.pop()
    ans[x][y]=cnt
    if k%2 == 1:
        if ty==-k and tx==-k:
            k+=1
            temp.append((x,y+1))
            tx=0
            ty=1
            continue
        if ty==-k:
            tx-=1
            x-=1
            temp.append((x,y))
        else:
            ty-=1
            y-=1
            temp.append((x,y))
    if k % 2 == 0:
        if ty == k and tx == k:
            k += 1
            temp.append((x, y-1))
            tx = 0
            ty = -1
            continue
        if ty == k:
            tx += 1
            x += 1
            temp.append((x, y))
        else:
            ty += 1
            y += 1
            temp.append((x, y))
for i in range(len(ans)):
    print(*ans[i])