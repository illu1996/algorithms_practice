# 이코테 p385
# 플로이드

n = int(input())
m = int(input())
INF = 1e9

G = [[INF] * (n+1) for _ in range(n+1)]


# 같은 거리 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            G[i][j] = 0
for _ in range(m):
    a, b, c = map(int,input().split())
    G[a][b] = min(G[a][b], c)

#플로이드 워셜 실행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            G[i][j] = min(G[i][j], G[i][k]+G[k][j])

# 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if G[i][j] == INF:
            print(0, end=' ')
        else:
            print(G[i][j], end= ' ')
    print()