# 이코테 p327
# 뱀


n= int(input())
# 빈공간 0 뱀 1 사과 2
map_list = [[0]*n for _ in range(n)]
k = int(input())
# 사과 지정
for _ in range(k):
    x,y  =map(int,input().split())
    map_list[x][y] = 2

# 초
time = 0
map_list[0][0] = 1

l = int(input())
move = [tuple(input().split()) for _ in range(l)]

dir = [(0,1), (1,0), (0,-1), (-1,0)]
# 처음 이동방향
dir_num = 0
x,y = 0,0
# 게임시작
while True:
    # 뱀 이동
    for i in range(l):
        if time == int(move[i][0]):
            if move[i][1] == "L":
                if dir_num==0:
                    dir_num = 3
                else:
                    dir_num = dir_num -1
            elif move[i][1] == "D":
                if dir_num == 3:
                    dir_num = 0
                else:
                    dir_num = dir_num + 1
                    
    nx = x + dir[dir_num][0]
    ny = y + dir[dir_num][1]
    if 0 <= nx < n and 0 <= ny < n :
        if map_list[nx][ny] == 2:
            map_list[nx][ny] = 1
            x = nx
            y = ny
            
        elif map_list[nx][ny] == 0:
            map_list[nx][ny] = 1
            map_list[x][y] = 0
            x = nx
            y = ny
            
        elif map_list[nx][ny] == 1:
            time += 1
            break
        
    else:
        time += 1
        break

    time += 1
print(time)