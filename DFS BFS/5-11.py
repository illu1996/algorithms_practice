# 이코테
# 미로 탈출 p149

n,m = map(int,input().split())

maze  = [list(map(int,input())) for _ in range(n)]

#4방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque

def bfs(x,y):
    q = deque([(x,y)])
    # 출발 위치 수 세기
    maze[x][y] = 1
    while q:
        x,y = q.popleft()
        #4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #벗어나면 넘어감
            if 0 > nx or n <= nx or 0 > ny or ny >= m:
                continue
            # 벽이면 걍넘어감
            if maze[nx][ny] == 0:
                continue
            # 처음 도착이면
            if maze[nx][ny] == 1:
                maze[nx][ny] += maze[x][y]
                q.append((nx,ny))
    return maze[n-1][m-1]
            
print(bfs(0,0))
