# 실전문제 게임게발
# 난이도 2

# n by m map
# land or sea

# a,b location

# 메뉴얼
# 1. 현재 위치에서 왼쪽(반시계) 부터 갈 곳을 정한다
# 2. 왼쪽 방향에 안가본 곳이 존재한다면 왼쪽으로 회전하고 한칸 전진
# 없다면 회전만 한다
# 3. 모두 가본 곳이거나 바다로 되어 있는 경우 바라보는 방향을 유지하고
# 뒤로 간다. 이때 뒤가 바다라면 움직임을 멈춘다.


n,m = map(int,input().split())
a, b, cha_dir = map(int,input().split())

dir = [(-1,0), (0,1), (1,0), (0,-1)]

game_map = [list(map(int,input().split())) for _ in range(n)]
game_map[a][b] = 2
#방문한 칸 수
visit = 1

#방향 전환 한 수
cnt = 0

while True:
    # 종료 조건
    if cnt == 4:
        #뒤로 갈 수 있으면 이동하기
        if game_map[a-dir[new_dir][0]][b-dir[new_dir][1]] == 0:
            a = a- dir[new_dir][0]
            b = b - dir[new_dir][1]
            cnt = 0
        else:
            break
    else:
        # 방향 틀기
        new_dir = (cha_dir + 1) % 4
        na = a + dir[new_dir][0]
        nb = b + dir[new_dir][1]
        # 가본곳 안가본곳 판단하기
        if game_map[na][nb] == 0:
            game_map[na][nb] = 2
            a = na
            b= nb
            cha_dir = new_dir
            cnt = 0
            visit += 1
            continue
        else:
            cha_dir = new_dir
            cnt += 1
print(visit)
            
    