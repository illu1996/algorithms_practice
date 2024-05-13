# 백준 2667
# 단지 번호 붙이기

#입력
n = int(input())
house = [list(map(int,input())) for _ in range(n)]
#방문 처리
visited = [[0]*n for _ in range(n)]

# 각 단지의 집
result = []

#4방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    global count
    visited[x][y] = 1
    count += 1

    for k in range(4):
        nx= x+dx[k]
        ny= y+dy[k]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and house[nx][ny] == 1:
            dfs(nx,ny)

#전체 탐색
for i in range(n):
    for j in range(n):
        if not visited[i][j] and house[i][j] == 1:
            count = 0
            dfs(i,j)
            result.append(count)
        
result = list(filter(lambda x:x!=0,result))
result.sort()

print(len(result))
for i in result:
    print(i)
    
