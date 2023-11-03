from collections import deque
def floodFill(image, sr, sc, color):
    n=len(image)
    m=len(image[0])
    visited=[[False]*m for _ in range(n)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    s=image[sr][sc]
    def bfs (x,y,visited,image,dx,dy,n,m,c,s):
        queue = deque()
        queue.append((x,y))
        image[x][y]=c
        while queue:
            cx,cy=queue.popleft()
            visited[cx][cy]=True
            for i in range(4):
                nx = cx+dx[i]
                ny = cy+dy[i]
                if nx >-1 and nx <n and ny > -1 and ny <m:
                    if image[nx][ny] == s and visited[nx][ny] == False:
                        image[nx][ny]=c
                        visited[nx][ny]=True
                        queue.append((nx,ny))
    bfs(sr,sc,visited,image,dx,dy,n,m,color,s)
    return image
print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))