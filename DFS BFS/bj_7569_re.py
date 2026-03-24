# 백준 7569
# 토마토
# 골드 5

m, n, h = map(int, input().split())
f_tomato = [[] for _ in range(h)]
visit = [[] for _ in range(h)]


for i in range(h):
    for j in range(n):
        f_tomato[i].append(list(map(int, input().split())))
        visit[i].append([0] * m)

direct = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
from collections import deque


def bfs(visit, sr, sc, sh):
    visit[sh][sr][sc] = 1
    q = deque([(sh, sr, sc)])
    while q:
        th, tr, tc = q.pop()
        for dh, dr, dc in direct:
            nh, nr, nc = th + dh, tr + dr, tc + dc
            if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m and not visit[nh][nr][nc]:

                if f_tomato[nh][nr][nc] == 0:
                    visit[nh][nr][nc] = visit[th][tr][tc] + 1
                    q.append((nh, nr, nc))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if f_tomato[i][j][k] == 1:
                bfs(visit, j, k, i)
print(visit)
