# pg 1844
# 게임 맵 최단거리

from collections import deque

def bfs(maps,x,y,visit):
    direct = [(0,1), (0,-1), (1,0), (-1,0)]
    
    q = deque([])
    q.append((x,y))
    visit[x][y] = 1
    n = len(maps)
    m = len(maps[0])
    

    while q:
        now_x, now_y = q.popleft()
        for dx,dy in direct:
            nx = now_x + dx
            ny = now_y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and maps[nx][ny] == 1:
                visit[nx][ny] = visit[now_x][now_y] + 1
                q.append((nx,ny))
                
def solution(maps):
    visit = [[0] * (len(maps[0])) for _ in range(len(maps))]

    bfs(maps,0,0,visit)
    
    return -1 if visit[len(maps)-1][len(maps[0])-1] == 0 else  visit[len(maps)-1][len(maps[0])-1]