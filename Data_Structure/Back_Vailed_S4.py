import sys
input= sys.stdin.readline
n=int(input())
for _ in range(n):
    a= input()
    cnt=0
    stack=[]
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                cnt+=1
                break
            else:
                stack.pop()
    if stack or cnt > 0:
        print("NO")
    else:
        print("YES")