# 개선된 다익스트라

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().strip().split())
start = int(input())
G = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a,b,c = map(int,input().strip().split())
    G[a].append((b,c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in G[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print(000)
    else:
        print(distance[i])