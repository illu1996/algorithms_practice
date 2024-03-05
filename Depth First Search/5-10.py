
# 이것이 취업을 위한 코딩 테스트다

# 음료수 얼려 먹기 p149

n,m = map(int,input().split())


ice_map = [list(map(int, input())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

x,y = 0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

count = 0

for i in range(n):
    for j in range(m):
        for k in range(4):   
            if ice_map[x][y] == 0 and visited[x][y] == 0 :
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0<=ny<m:
                    visited[x][y] = 1
                    x = nx
                    y = ny
                    continue
                
    else:
        count += 1
print(count)
                    
