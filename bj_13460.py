# 구슬 탈출 2
# 골드 1
# 풀이 시작 시간 260224 10:05

n, m = map(int, input().split())

board = [list(map(str, input())) for i in range(n)]

visit = [[0] * m for _ in range(n)]

min_count = 9999999

temp_red = (0, 0)
temp_blue = (0, 0)

for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            temp_red = (i, j)
        elif board[i][j] == "B":
            temp_blue = (i, j)

rot = [
    "L",
    "R",
    "T",
    "B",
]
rot_1 = [(0, -1), (0, 1), (1, 0), (-1, 0)]
