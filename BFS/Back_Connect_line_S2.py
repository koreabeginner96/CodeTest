import sys
from collections import deque
input= sys.stdin.readline

def bfs(start):
    queue =deque([start])
    visited=[start]=True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not vistied[i]:
                visited[i] = True
                queue.append(i)
n,m = map(int,input().split())
graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)
count=0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    if not visited[i]:
        if graph[i]:
            count+=1
        else:
            bfs(i)
            count+=1
print(count)