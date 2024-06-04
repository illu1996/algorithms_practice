# 이코테 p314
# 만들 수 없는 금액

from itertools import combinations

n = int(input())
cent_list = list(map(int,input().split()))

make_list = [0] * (max(cent_list)+1)

min_value = len(make_list)

for i in range(1,n):
    for j in combinations(cent_list,i):
        if sum(list(j)) < len(make_list):
            make_list[sum(list(j))] += 1
            
for i in range(1,len(make_list)):
    if make_list[i] == 0:
        print(i)
        break



