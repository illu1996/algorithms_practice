# 미로탐색
# 백준 2178
# 실버 1

from collections import deque

n, m = map(int, input().split())
data = []
for i in range(n):
    lst = list(map(int, input()))
    data.append(lst)

visit = list([0] * m for _ in range(n))
cnt_map = list([10000] * m for _ in range(n))
sr, sc = 0, 0
er, ec = n - 1, m - 1
q = deque([])
visit[sr][sc] = 1
cnt_map[sr][sc] = 1
q.append((sr, sc))

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while q:
    now_r, now_c = q.popleft()
    cnt = cnt_map[now_r][now_c]
    for dr, dc in direct:
        new_r, new_c = now_r + dr, now_c + dc
        if (
            0 <= new_r <= er
            and 0 <= new_c <= ec
            and not visit[new_r][new_c]
            and data[new_r][new_c] == 1
        ):
            visit[new_r][new_c] = 1
            q.append((new_r, new_c))
            if cnt_map[new_r][new_c] > cnt + 1:
                cnt_map[new_r][new_c] = cnt + 1

print(cnt_map[er][ec])
