# 백준 1987
# 알파벳
# 골드 4

r, c = map(int, input().split())
alpha_map = list(list(input()) for _ in range(r))
visit_map = list([0] * c for _ in range(r))
visit_alpha = [0] * 26

cnt = 1
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
from collections import deque


def dfs(visit, visit_map, now_r, now_c, alpha_map):
    cnt = 1
    max_cnt = 0
    visit[ord(alpha_map[now_r][now_c]) - ord("A")] = 1
    visit_map[now_r][now_c] = 1
    stack = [(now_r, now_c)]
    while stack:
        now_r, now_c = stack.pop()
        for dr, dc in direct:
            new_r, new_c = now_r + dr, now_c + dc
            if (
                0 <= new_r < r
                and 0 <= new_c < c
                and not visit_map[new_r][new_c]
                and not visit[ord(alpha_map[new_r][new_c]) - ord("A")]
            ):
                stack.append((new_r, new_c))
                visit[ord(alpha_map[new_r][new_c]) - ord("A")] = 1
                visit_map[new_r][new_c] = 1
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
    return cnt


result = dfs(visit_alpha, visit_map, 0, 0, alpha_map)
print(result)


# 왜 틀렸는가??
# 백트래킹이 필수이다.
