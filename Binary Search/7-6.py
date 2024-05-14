# 이코테 7-6, p201
# 떡볶이 떡 만들기

# 순차탐색 ... for 문 2번이면 2천만 곱하기 백만..... 2억 곱하기 10만개를 찾아봐야 한다 시간 초과 백프로

# 이진탐색... 파라메트릭 서치 == 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제

# 떡의개수 n, 손님이 요청 길이 m
n, m = map(int,input().split())

# 떡의 길이 리스트
rice_list = list(map(int,input().split()))
# 자를 높이의 리스트
h_list = list(range(1,max(rice_list)+1))
ans = 0

# 순차 탐색
# #자를 떡의 리스트 더해주기
# #떡을 반복문 돌면서 #큰값부터 
# for i in range(len(h_list)-1,-1,-1):

#     sum = 0
#     for j in rice_list:
#         if j - h_list[i] > 0:
#             sum += j - h_list[i]
#     if sum == m:
#         ans = h_list[i]
#         break

# print(ans)

# 이진 탐색
start = 0
end = max(rice_list)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # 떡 자르기
    for i in rice_list:
        if i > mid:
            total += i - mid
    # 떡의 총 길이가 손님 요청보다 작은경우 
    if total == m:
        result = mid   
    if total < m:
        end = mid - 1
    else:
        start = mid +1

print(result)
        