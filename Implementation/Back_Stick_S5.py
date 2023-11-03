import sys
input= sys.stdin.readline
x=[64,32,16,8,4,2,1]
b=int(input())
cnt=0
for i in range(len(x)):
    if b >= x[i]:
        cnt+=1
        b-=x[i]
    if b==0:
        break
print(cnt)