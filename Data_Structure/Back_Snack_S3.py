#굳이 dequeue 안썻어도 됨 하나씩 먼저 비교 안맞는건 전부 stack에 집어넣고
#deque 다끝나면 pop으로 끝내서 stack의유무를 확인하면 된다.
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
m=1
o= list(map(int,input().split()))
b=deque(o)
stack=[]
while(b):
    x=b.popleft()
    if x<m and stack[-1] < m:
        break
    elif m==x:
        m+=1
    elif not stack:
        stack.append(x)
    elif x> m :
        stack.append(x)
    while stack and stack[-1] == m:
        stack.pop()
        m+=1
if n==(m-1):
    print("Nice")
else:
    print("Sad")