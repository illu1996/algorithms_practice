# 백준 10815
# 숫자 카드 실버 5

import sys
input = sys.stdin.readline
n = int(input())
# 상근 카드
sng_card = list(map(int, input().split()))
# 받은 카드
m = int(input())
num_lst = list(map(int,input().split()))
have_card = [0] * m

print(sng_card)
print(num_lst)

# # 시간초과
# for i in range(m):
#     for j in range(n):
#         if sng_card[j] == num_lst[i]:
#             have_card[i] = 1

# for i in range(m):
#     print(have_card[i], end=' ')

# # map 이용
# # 메모리 초과
# have_card = {}
# # 모든범위 map = 0 만들기
# for i in range(-10000000,10000000):
#     have_card[i] = 0
# # 가지고 있는 카드 1개 올려주기
# for i in range(n):
#     have_card[sng_card[i]] += 1
# # print(have_card)
# ans = []
# for i in range(m):
#     if have_card[num_lst[i]] == 1:
#         ans.append(1)
#     else:
#         ans.append(0)

# # for i in range(m):
# #     print(ans[i], end=' ')
    

# map 이용
have_card = {}

# 가지고 있는 카드 1개 올려주기
for i in range(n):
    if sng_card[i] not in have_card:
        have_card[sng_card[i]] = 1

# print(have_card)
ans = []
for i in range(m):
    if num_lst[i] in have_card:
        ans.append(1)
    else:
        ans.append(0)

for i in range(m):
    print(ans[i], end=' ')