import sys
input= sys.stdin.readline
stack=[]
n=int(input())
def stack_1(num):
    if num[0]==1:
        stack.append(num[1])
    if num[0]==2:
        if stack :
            a=stack.pop()
            print(a)
        else:
            print(-1)
    elif num[0]==3:
        print(len(stack))
    elif num[0]==4:
        if not stack:
            print(1)
        else:
            print(0)
    elif num[0]==5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
for _ in range(n):
    a=list(map(int,input().split()))
    stack_1(a)

