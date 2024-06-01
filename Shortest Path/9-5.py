# 이코테 p262
# 전보

import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int,input().strip().split())
G = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    s,e,d = map(int,input().strip().split())
    G[s].append((e,d))
    
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in G[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(c)
        
count = 0
max_time = 0
for i in range(1,n+1):
    if 0 < distance[i] < INF:
        count += 1
        if max_time < distance[i]:
            max_time = distance[i]
print(count, max_time)