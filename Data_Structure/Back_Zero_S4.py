import sys
input = sys.stdin.readline
n=int(input())
sum=[]
answer=0
for _ in range(n):
    a= int(input())
    if a == 0:
        sum.pop()
    else:
        sum.append(a)
for i in sum:
    answer+=i
print(answer)
