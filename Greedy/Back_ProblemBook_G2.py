import sys
import heapq
n,m=map(int,input().split())
heap=[]
graph=[[] for _ in range(n+1)]
visited=[0] * (n+1)
res=[]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    visited[a]+=1
for i in range(n+1):
    if visited[i]==0:
        heapq.heappush(heap,i)
bfs()
print()