# 이코테 p259
# 미래도시
import sys

input = sys.stdin.readline
INF=int(1e9)
    
n, m  = map(int,input().strip().split())
G = [[INF]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            G[a][b] = 0

for i in range(m):
    a,b = map(int,input().strip().split())
    G[a][b] = 1
    G[b][a] = 1


X, K =map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            G[a][b] = min(G[a][b],G[a][k]+G[k][b])

result = G[1][K] + G[K][X]
if result >= INF:
    print('-1')
else:
    print(result)

