INF = int(1e9)

n = int(input())
m = int(input())

G = [[INF] *(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            G[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    G[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            G[a][b] = min(G[a][b],G[a][k] + G[k][b])
            
for a in range(1, n+1):
    for b in range(1,n+1):
        if G[a][b] == INF:
            print(000, end='')
        else:
            print(G[a][b], end ='')
    print()

# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2