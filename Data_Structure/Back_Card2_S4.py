import sys
from collections import deque
input=sys.stdin.readline
c=[]
c=deque(c)
n=int(input())
for i in range(1,n+1):
    c.append(i)
while len(c)!=1:
    a=c.popleft()
    b=c.popleft()
    c.append(b)
print(*c)