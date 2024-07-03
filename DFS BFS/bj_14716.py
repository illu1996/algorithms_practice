# bj 14716
# 현수막

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().strip().split())
str_map = [list(map(int,input().strip().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]


def bfs(x,y):

    q =deque([])
    q.append((x,y))
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and str_map[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx,ny))
    
    return 

#글자 개수
count = 0
# 완전 탐색
for i in range(n):
    for j in range(m):
        # 방문 안한 곳만 방문
        if not visit[i][j] and str_map[i][j] == 1:
            bfs(i,j)
            count += 1
                
print(count)