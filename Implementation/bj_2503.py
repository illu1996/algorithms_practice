# 검색해서 품... 조건 못찾음 다시 풀기
# bj 2503 숫자야구
# 실버 3
from itertools import permutations

n = int(input())
# 숫자야구 1~9 까지로 만들 수 있는 모든 경우의 수 만들기
baseball_lst = list(permutations(list(range(1,10)), 3))

for _ in range(n):
    num, s, b = map(int, input().split())
    tmp = []
    
    for baseball in baseball_lst:
        cnt_s = cnt_b = 0
        
        for i, str_num in enumerate(str(num)):
            if int(str_num) == baseball[i]:
                cnt_s += 1
            if int(str_num) != baseball[i] and int(str_num) in baseball:
                cnt_b += 1
        if s == cnt_s and cnt_b == b:
            tmp.append(baseball)
    baseball_lst = tmp

print(len(baseball_lst))