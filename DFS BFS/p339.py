# 이코테 # p339
# 특정 거리의 도시 찾기

import sys,collections
input = sys.stdin.readline
n, m, k, x = map(int,input().strip().split())

G = [[] for _ in range(n+1)]
visited = [0]*(n+1)
distance = [0]*(n+1)
for i in range(m):
    a, b = map(int,input().strip().split())
    G[a].append(b)

def bfs(G, x):
    visited[x] = 1
    q = collections.deque([x])
    while q:
        now = q.popleft()
        for i in G[now]:
            if not visited[i]:
                visited[i] = 1
                distance[i] = distance[now] + 1
                q.append(i)
    
bfs(G,x)

city = []
for i in range(1,len(distance)):
    if distance[i] == k:
        city.append(i)

city.sort()
if len(city) == 0:
    print(-1)
else:
    for i in city:
        print(i)

        