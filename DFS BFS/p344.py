# 이코테 p344
# 경쟁적 전염
from collections import deque


n, k = map(int,input().split())
virus_map = [list(map(int,input().split())) for _ in range(n)]

s,end_x,end_y = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0] 

virus_num = []
# 처음 바이러스 위치 찾기
for i in range(n):
    for j in range(n):
        if virus_map[i][j] != 0:
            virus_num.append((virus_map[i][j],0,i,j))
            
#바이러스 퍼지기
virus_num.sort()
q = deque(virus_num)
    
while q:
    order, second, x, y = q.popleft()
    if second  == s:
        break
    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0 <= nx < n and 0 <= ny < n and virus_map[nx][ny] == 0:
            virus_map[nx][ny] = virus_map[x][y]
            q.append((virus_map[x][y], second+1 , nx, ny))
    
print(virus_map[end_x-1][end_y-1])