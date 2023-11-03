#이문제는 스택을 넣었을때 동작이 어떻게 하는지 와 큐를 넣었을때 어떻게 하는지 문제이다
#스택은 넣고 바로 빠지므로 큐만 정리하면된다.
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
sequence_A = list(map(int, input().split())) ## queue == 0, stack == 1
sequence_B = list(map(int, input().split())) ## i번 자료구조에 들어있는 원소
M = int(input())                             ## 삽입할 수열의 길이
sequence_C = list(map(int, input().split())) ## 삽입할 수열

## 스택은 무시하고 큐만 deque에 추가하기
queue = deque([])
for i in range(N):
    if sequence_A[i]==0:
        queue.appendleft(sequence_B[i])
else:
    if len(queue)== 0:
        print(*sequence_C)
        sys.exit()
for i in range(M):
    queue.append(sequence_C[i])
    print(queue.popleft(),end=" ")