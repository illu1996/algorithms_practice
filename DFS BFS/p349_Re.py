# 이코테 p349
# 연산자 끼워넣기

from collections import deque
from itertools import permutations

n = int(input())
num_list = list(map(int,input().split()))

# 연산자 리스트
pl = list(map(int,input().split()))

pl_list = []
for i in range(4):
    if pl[i] != 0:
        for j in range(pl[i]):
            pl_list.append(i)
perm_list = list(permutations(pl_list,n-1))

max_value = 0
min_value = 1e9

# 숫자 계산 함수
def cal_num(num_list, pl_list):
    result = num_list[0]
    
    s = 0
    while s < n-1:
        if pl_list[s]==0:
            result += num_list[s+1]
        elif pl_list[s]==1:
            result -= num_list[s+1]
        elif pl_list[s]==2:
            result *= num_list[s+1]
        elif pl_list[s]==3:
            if result>0:
                result //= num_list[s+1]
            else:
                result = (result*-1) //num_list[s+1]
        s += 1
    return result

# 각 조합별 계산
for i in perm_list:
    
    max_value = max(max_value,cal_num(num_list, list(i)))
    min_value = min(min_value,cal_num(num_list, list(i)))

print(max_value)
print(min_value)
        
    
