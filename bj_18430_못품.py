# bj 18430
# 무기 공학
from collections import deque
n, m = map(int,input().split())

tree = [list(map(int,input().split())) for _ in range(n)]


dx = [[0,1],[-1,0],[-1,0],[0,1]]
dy = [[-1,0],[0,-1],[0,1],[1,0]]

# 부메랑이 가능한지 확인하고 강도 더 해주는 함수
def check(x,y):
    for i in range(4):
        
        nx_1 = dx[i][0] + x
        ny_1 = dy[i][0] + y
        nx_2 = dx[i][1] + x
        ny_2 = dy[i][1] + y
        
        if 0 <= nx_1 < n and 0 <= ny_1 < n and not visit[nx_1][ny_1] and 0 <= nx_2 < n and 0 <= ny_2 < n and not visit[nx_2][ny_2]:
            return True

# bfs 함수
def bfs(x,y,cnt,visit):
    q = deque([])
    q.append((x,y))
    
    while q:
        qx, qy = q.popleft()
        if check(qx,qy):
            pass

            
for i in range(n):
    for j in range(m):
        cnt = 0
        visit = [[0] * m for _ in range(n)]
        bfs(i,j,cnt,visit)