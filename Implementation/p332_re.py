# 치킨 배달

from itertools import combinations
n, m  = map(int,input().split())
# 1부터 시작하므로 + 1

def sum_distance(x,y,a,b):
    sum_dis = abs(x-a) + abs(y-b)
    return sum_dis

# 최대 M개를 고르고 폐업

# max 50 , 13
city_map = [list(map(int,input().split())) for _ in range(n)]

# 0 빈칸 1 집 2 치킨집

# 조합 만들기
ch_lst = []
home_lst = []

#집이랑 치킨 좌표 추가하기
for i in range(n):
    for j in range(n):
        if city_map[i][j] == 1:
            home_lst.append((i,j))
        elif city_map[i][j] == 2:
            ch_lst.append((i,j))

# 살릴 치킨집 조합 만들기
comb_ch_lst = list(combinations(ch_lst,m))

# 살린 치킨과 집끼리의 치킨 거리 구하고 합 만들기
# 매 집마다 치킨 집과의 최소값 다 구하기

total_dis = 1e9
for i in range(len(comb_ch_lst)):
    sum_dis = 0
    for x,y in home_lst:
        min_dis = 1e9
        for a,b in comb_ch_lst[i]:
            dis = sum_distance(x,y,a,b)
                
            min_dis = min(min_dis, dis)
        sum_dis += min_dis
    total_dis = min(total_dis,sum_dis)
            
print(total_dis)