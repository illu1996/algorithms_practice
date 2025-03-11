# 백준 양 3184
# 실버 1


# 모든 울타리로 둘려싸여 있는 면적 확인한 후 늑대와 양의 수 비교하기
r,c = map(int,input().split())

maps = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
#살아남은 양과 늑대의 수
all_s = 0
all_w = 0

# bfs
from collections import deque

q= deque([(0,0)])
dx = [0,1,0,-1]
dy = [1,0,-1,0]


# 너비 우선 탐색
def bfs(visit,maps,x,y):
    q = deque([(x,y)])
    visit[x][y] = 1
    # 양의 수, 늑대의 수
    s = 0
    w = 0
    while q:
        x,y = q.pop()
        
        if maps[x][y] == 'v' :
            w += 1
        elif maps[x][y] == 'o' :
            
            s += 1
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 유효 값
            if 0<= nx < r and 0 <= ny < c and not visit[nx][ny] and maps[nx][ny] != '#':
                visit[nx][ny] = 1
                q.append((nx,ny))
    # 함수 리턴
    return [s,w]

# 완전 탐색 시작
for i in range(r):
    for j in range(c):
        # 유효값
        if not visit[i][j] and maps[i][j] != '#':
            k = bfs(visit,maps,i,j)
            
            # 양이나 늑대가 한마리라도 존재한다면 값 비교
            if k[0] or k[1]:
                if k[0] > k[1]:
                    all_s += k[0]
                elif k[0] <= k[1]:
                    all_w += k[1]
print(all_s, all_w)

