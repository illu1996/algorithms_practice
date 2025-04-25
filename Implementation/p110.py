# 예제 4-1 상하 좌우
# 난이도 1

# 시간제한 1초
# 메모리 제한 128MB

# n by n map
n = int(input())
map = [[0] * n for _ in range(n)]
# 이동 계획서
move_plan = list((input().split()))

# L R U D 왼 오 위 아
def moveDir(dir):
    coodi = ""
    if dir == 'L':
        coodi = (-1,0)
    if dir == 'R':
        coodi = (1,0)
    if dir == 'U':
        coodi = (0,-1)
    if dir == 'D':
        coodi = (0,1)
    return coodi

# 현재 위치
x,y = 0,0

# 이동 계획서에 따른 이동
for i in range(len(move_plan)):
    dx,dy = moveDir(move_plan[i])
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 :
        continue
    else:
        x = nx
        y = ny
print(ny + 1, nx + 1)
    