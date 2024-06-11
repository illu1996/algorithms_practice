import heapq, sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().strip().split())
s = int(input())

distance = [INF]*(n+1)
G = [[] for _ in range(n+1)]

for _ in range(n+1):
    a,b,c= map(int,input().split())
    G[a].append((b,c))

def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in G[now]:
            cost = dist + i[0]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))