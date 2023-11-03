from collections import deque
def solution(grid:list):
    n=len(grid)
    m=len(grid[0])
    visited=[[False]*m for _ in range(n)]
    cnt=0
    cx=[-1,1,0,0]
    cy=[0,0,-1,1]
    def bfs(n,m,x,y,grid,visited,cx,cy):
        queue=deque()
        visited[x][y] = True
        grid[x][y]=0
        queue.append((x,y))
        while queue:
            nx,ny=queue.popleft()
            for i in range(4):
                fx=nx+cx[i]
                fy=ny+cy[i]
                if fx >-1 and fx < n and fy >-1 and fy < m :
                    if grid[fx][fy] == '1':
                        if visited[fx][fy]==False:
                            queue.append((fx,fy))
                            visited[fx][fy]= True
                            grid[fx][fy]= 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='1':
                bfs(n,m,i,j,grid,visited,cx,cy)
                cnt+=1
    return cnt
print(solution(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))