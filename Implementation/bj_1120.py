# 백준 1120
# 문자열 실버4
from copy import deepcopy
a,b = input().split()

lst_a = list(a)
lst_b = list(b)
min_cnt = 51

# 차이 개수 판별 함수
def count_char(a,b):
    cnt = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

# 틀림!!!!!!!
# # 종료 조건
# if len(a) == len(b) :
#     min_cnt = count_char(lst_a,lst_b)
# # 들어 있으면 0으로 
# elif a in b:
#     min_cnt = 0

# else:
#     lenA = len(lst_a)
#     lenB = len(lst_b)
#     # 뒤에 추가
#     testa = deepcopy(lst_a)
#     testa.extend(lst_b[lenA:lenB])
#     res = count_char(testa,lst_b)
#     if res < min_cnt:
#         min_cnt = res
    
#     # 앞에 추가
#     testa = deepcopy(lst_a)
#     testa = lst_b[0:lenB-lenA] + testa
#     res = count_char(testa,lst_b)
#     if res < min_cnt:
#         min_cnt = res
    
# print(min_cnt)

# b의 각 자리별 슬라이딩 윈도우 했을때 차이값 확인하기

# 종료 조건
if len(a) == len(b) :
    min_cnt = count_char(lst_a,lst_b)
# 들어 있으면 0으로 
elif a in b:
    min_cnt = 0
else:
    for i in range(0,len(b) - len(a) + 1):
        sliding = b[i:i+len(a)]
        res = count_char(a,sliding)
        if res < min_cnt:
            min_cnt = res
print(min_cnt)