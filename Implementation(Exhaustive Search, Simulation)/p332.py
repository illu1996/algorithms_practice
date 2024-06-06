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

# 조합별 만ㄷ르기
comb_list = list(combinations(ch_stack,m))

# 각 집별 최소 m 개의 치킨값과의 최소 거리 구하기
distance = []

for j in comb_list:
    result = 0
    # 모든 집에서
    for hx,hy in home_stack:
        temp = 1e9
        #각 치킨집까지의 최소거리
        for cx,cy in j:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    distance.append(result)

print(min(distance))    