import sys
input= sys.stdin.readline
n=int(input())
answer=[]
l=[i for i in range(2,n+1)]
a= [0]+list(map(int, input().split()))
answer.append(1)
index=0
m=a[1]
while 1 != len(a):
    index+=m
    if len(a)<index:
        index=index//m
    b=l.pop(index)
    answer.append(b)
    m=a[index]
print(answer)