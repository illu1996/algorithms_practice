# 이코테 p386
# 정확한 순위

n, m =map(int,input().split())
INF = 1e9
G = [[INF] *(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    G[a][b] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            G[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

# for i in range(n+1):
#     for j in range(n+1):
#         if G[i][j] == INF:
#             G[i][j] = 0

# print(G)
result = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if G[i][j] != INF or G[j][i] != INF:
            count += 1
    if count == n:
        result +=1
print(result)
