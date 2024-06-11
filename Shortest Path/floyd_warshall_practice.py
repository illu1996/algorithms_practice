
INF = 1e9

n,m = map(int,input().split())

G = [[INF] *(n+1) for _ in range(n+1)]

# 자기 자신 거리 0
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j:
            G[i][j] = 0

#각 간선 정보 입력
for _ in range(m):
    a, b, c = map(int,input().split())
    G[a][b] = c

#플로이드 수행
for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])