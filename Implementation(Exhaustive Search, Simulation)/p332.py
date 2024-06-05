#이코테 p332
# 치킨 배달
from itertools import combinations,permutations

n, m = map(int,input().split())

city = [list(map(int,input().split())) for _ in range(n)]

# 집의 위치, 치킨집 위치 구하기
home_stack = []
ch_stack = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home_stack.append((i,j))
        elif city[i][j] == 2:
            ch_stack.append((i,j))

distance = []
# 조합별 만ㄷ르기
comb_list = list(combinations(ch_stack,m))
print(comb_list)
# 각 집별 최소 m 개의 치킨값과의 최소 거리           
for i in home_stack:
    sum_dis = 0
    temp = 1e9
    for j in comb_list:
        #각 집별 최소거리 더하기
        temp = min(temp,abs(i[0]-j[0]))+abs(i[1]-j[1])
    sum_dis += temp
    distance.append(sum_dis)
print(min(distance))
            
        