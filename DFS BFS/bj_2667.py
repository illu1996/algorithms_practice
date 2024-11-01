# 백준 2667
# 단지 번호 붙이기

### dfs 풀이
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
    
# 백준 2667 단지번호 붙이기
# 실버 1


### bfs 풀이
n = int(input())

#각 단지별로 그냥 숫자 추가
ans = []
maps = [list(map(int,input())) for _ in range(n)]
# 방문 중복처리
visit = [[0]*n for _ in range(n)]

from collections import deque
# 4방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(maps, visit, x,y):
    q = deque([(x,y)])
    visit[x][y] = 1
    
    # 한개의 단지별 집의 개수
    house = 0
    while q:
        x,y = q.pop()
        # 집이라면 개수 추가
        if maps[x][y] == 1:
            house += 1
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 유효값이면 큐에 추가
            if 0<= nx < n and 0 <= ny < n and not visit[nx][ny] and maps[nx][ny] != 0:
                q.append((nx,ny))
                visit[nx][ny] = 1
    return house

# 다 탐색
for i in range(n):
    for j in range(n):
        # 유효범위
        if not visit[i][j] and maps[i][j] == 1:
            cnt = bfs(maps,visit,i,j)
            # cnt가 0이 아니면 답에 추가
            if cnt:
                ans.append(cnt) 

# 오름차순 정렬
ans.sort()

#출력
print(len(ans))
for i in ans:
    print(i)