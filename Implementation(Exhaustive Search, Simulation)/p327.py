# 이코테 p327
# 뱀


n= int(input())

apple_map= [[0]*n for _ in range(n)]

# 사과의 위치 2로 표시
apple = int(input())

for i in range(apple):
    a, b = map(int,input().split())
    apple_map[a][b] = 2

# 뱀의 방향 전환
change_dir = []
change_input = int(input())
for i in range(change_input):
    a,b = map(str,input().split())
    change_dir.append((a,b))
# 방향전환
direct = ['R','D','L','U']
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 시작 위치
x,y = 0,0
second = 0
crash = False
apple_map[x][y] = 1
snake_direct = 0

while apple:
        # 충돌시 종료
    if crash == True:
        break
    
    # 이동 방향 결정
    for i in range(len(change_dir)):
        if int(change_dir[i][0]) == second:
            if change_dir[i][1] == 'L':
                snake_direct = (snake_direct-1)%4
            else:
                snake_direct = (snake_direct+1)%4

    for k in range(4):
        if direct[snake_direct] == direct[k]:
            nx = x + dx[k]    
            ny = y + dy[k]
            if 0<= nx < n and 0<= ny < n and apple_map[nx][ny] != 1:
                # 이동시 사과가 있을때
                if apple_map[nx][ny] ==2:
                    apple_map[nx][ny] = 1
                    apple -= 1
                    x,y = nx,ny
                # 이동시 사과가 없을때
                else:
                    apple_map[nx][ny] = 1
                    apple_map[x][y] = 0
                    x,y = nx,ny
            else:
                crash = True
        else:
            continue

    second += 1

print(second)