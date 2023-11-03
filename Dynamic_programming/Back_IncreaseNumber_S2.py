#dp는 점화식으로 생각하면된다. 이중for문을 사용하여 문제를 풀어보자
import sys
input=sys.stdin.readline
n=int(input())
dp=[1]*n
A=list(map(int,input().split()))
for i in range(1,n):
    for j in range(i):
        if A[i]>A[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))