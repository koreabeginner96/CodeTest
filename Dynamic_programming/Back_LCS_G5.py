import sys
input=sys.stdin.readline
# [0]더하고 값 비교하기
s1 = [0]+list(input().rstrip())
s2 = [0]+list(input().rstrip())
#추가 할떄 s2 먼저하고 s1은 뒤에하기
dp=[[0]*len(s2) for _ in range(len(s1))]
#항상 1부터 시작한다 dp
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i]==s2[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1], dp[i-1][j])
print(dp[len(s1)-1][len(s2)-1])