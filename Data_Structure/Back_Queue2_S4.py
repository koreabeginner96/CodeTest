import sys
from collections import deque
input=sys.stdin.readline
n= int(input())
stack=[]
stack=deque(stack)
def cal(order):
    if order[0] == "push":
       stack.append(order[1])
    elif order[0] == "pop":
        if stack:
            a=stack.popleft()
            print(a)
        else:
            print(-1)
    elif order[0]=="size":
        print(len(stack))
    elif order[0]=="empty":
        if stack:
            print(0)
        else:
            print(1)
    elif order[0]=="front":
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif order[0]=="back":
        if stack:
            print(stack[-1])
        else:
            print(-1)
for i in range(n):
    a=list(input().split())
    cal(a)