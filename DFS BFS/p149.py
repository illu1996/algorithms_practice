# 음료수 얼려 먹기

n, m = map(int,input().split())

ice = [list(map(int,input())) for _ in range(n)]
cnt = 0

visited = [[0]* m for _ in range(n)]
dir = [(0,1), (0,-1),(1,0), (-1,0)]

cnt = 0

def dfs(x,y):
    global cnt
    
    for dirx, diry in dir:
        nx = x + dirx
        ny = y + diry
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and ice[nx][ny] == 0:
            visited[nx][ny] = cnt
            dfs(nx,ny)
    
                    
for i in range(n):
    for j in range(m):
        if ice[i][j] == 0 and not visited[i][j]:
            cnt += 1
            visited[i][j] = cnt
            dfs(i,j)

print(visited)
print(ice)
print(cnt)