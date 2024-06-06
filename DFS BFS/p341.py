# 이코테 p341
# 연구소

n,m = map(int,input().split())
bio_map = [list(map(int,input().split())) for _ in range(n)]



dx = [1,0,-1,0]
dy = [0,1,0,-1]


# 바이러스 퍼지기
def virus(bio_map, x,y):
    for k in range(4):
        nx = x+ dx[k] 
        ny = y+ dy[k]
        if 0<= nx < n and 0<= ny < m and bio_map[nx][ny] == 0:
            bio_map[nx][ny] = 2
            virus(bio_map,nx,ny)

# 안전구역 세기
def safe_area(bio_map):
    count = 0
    for i in range(n):
        for j in range(m):
            if bio_map[i][j] == 0:
                count += 1
    return count

# 연구소 모든 조합 만들기
from itertools import combinations
from copy import deepcopy
# 벽 위치 리스트 만들기
block_list = []
for i in range(n):
    for j in range(m):
        if bio_map[i][j] == 0:
            block_list.append((i,j))

bulid_block_list = list(combinations(block_list,3))

max_value = 0

# 모든 조합별 확인
for i in bulid_block_list:
    # 조합별 안전구역 최대값

    bio_map_copy = deepcopy(bio_map)
    # 조합 확인 후 벽 세우기
    for x,y in list(i):
        bio_map_copy[x][y] = 1
    #바이러스 감염
    for j in range(n):
        for k in range(m):
            if bio_map_copy[j][k] == 2:
                virus(bio_map_copy, j,k)
    # 수 세기
    max_value = max(max_value,safe_area(bio_map_copy))
        
        
print(max_value)
