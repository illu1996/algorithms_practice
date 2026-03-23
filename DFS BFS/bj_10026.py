# 적록색약
# 백준 10026
# 골드 5
from collections import deque

n = int(input())
RGB_map = list(list(input()) for _ in range(n))

normal_cnt = 0
special_cnt = 0

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

normal_visit = list([0] * n for _ in range(n))
special_visit = list([0] * n for _ in range(n))


def dfs(now_r, now_c, now_color, visit):
    stack = []
    visit[now_r][now_c] = 1
    stack.append((now_r, now_c))
    while stack:
        now_r, now_c = stack.pop()
        for dr, dc in direct:
            new_r, new_c = dr + now_r, dc + now_c
            if (
                0 <= new_r <= n - 1
                and 0 <= new_c <= n - 1
                and not visit[new_r][new_c]
                and RGB_map[new_r][new_c] == now_color
            ):
                stack.append((new_r, new_c))
                visit[new_r][new_c] = 1


def special_dfs(now_r, now_c, now_color, visit):
    visit[now_r][now_c] = 1
    stack = []
    stack.append((now_r, now_c))
    while stack:
        now_r, now_c = stack.pop()

        for dr, dc in direct:
            new_r, new_c = dr + now_r, dc + now_c
            if 0 <= new_r <= n - 1 and 0 <= new_c <= n - 1 and not visit[new_r][new_c]:
                if now_color == "R" or now_color == "G":
                    if RGB_map[new_r][new_c] == "R" or RGB_map[new_r][new_c] == "G":
                        stack.append((new_r, new_c))
                        visit[new_r][new_c] = 1
                elif now_color == "B":
                    if RGB_map[new_r][new_c] == "B":
                        stack.append((new_r, new_c))
                        visit[new_r][new_c] = 1


for i in range(n):
    for j in range(n):
        if not normal_visit[i][j]:
            dfs(i, j, RGB_map[i][j], normal_visit)
            normal_cnt += 1

for i in range(n):
    for j in range(n):
        if not special_visit[i][j]:
            special_dfs(i, j, RGB_map[i][j], special_visit)
            special_cnt += 1


print(normal_cnt, special_cnt)
