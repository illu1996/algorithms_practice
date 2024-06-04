# 이코테 p 315
# 볼링공 고르기
from itertools import combinations

n, m = map(int,input().split())
kg_list = list(map(int,input().split()))

ans = 0
for i in combinations(kg_list, 2):
    if i[0] != i[1]:
        ans +=1 
print(ans) 