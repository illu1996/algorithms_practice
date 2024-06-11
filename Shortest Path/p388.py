# 이코테 #p388
# 화성 탐사
import heapq
def dijkstra(value,x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = []
    heapq.heappush(q,(value,x,y))
    distance[x][y] = value
    while q:
        dist,x,y = heapq.heappop(q)
        
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx <n and 0<=ny < n:
                cost = cost_map[nx][ny] + dist
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))
INF = 1e9
t = int(input())
for _ in range(t):
    n = int(input())

    cost_map = [list(map(int,input().split())) for _ in range(n)]

    distance = [[INF]*n for _ in range(n)]

    dijkstra(cost_map[0][0],0,0)
    print(distance[n-1][n-1])