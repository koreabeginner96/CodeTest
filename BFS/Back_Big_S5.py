import sys
input= sys.stdin.readline
n=int(input())
rank=[1] * n
i=[]
for _ in range(n):
    a,b= map(int,input().split())
    i.append((a,b))
for o in range(len(i)):
    for j in range(len(i)):
     if i[o][0] <i[j][0]:
         if i[o][1] <i[j][1]:
             rank[o]+=1
print(*rank)