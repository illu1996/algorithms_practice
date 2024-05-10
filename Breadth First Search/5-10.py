# 음료수 얼려먹기
# bfs 로 풀기

from collections import deque
n,m = map(int,input().split())

ice = [list(map(int,input())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    if ice[x][y] == 1:
        return False
        
    while queue:
        x,y = queue.popleft()
        ice[x][y] =1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if   0<=nx <n and 0<=ny <m and ice[nx][ny]==0:
                queue.append((nx,ny))
    return True            
count =0 

for i in range(n):
    for j in range(m):
        if bfs(i,j) == True:
            count +=1
            
print(count)