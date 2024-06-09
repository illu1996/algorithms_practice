# 이코테 p363
# 카드 정렬하기

import heapq
 
n = int(input())
card_set = [int(input()) for _ in range(n)]

card_set.sort()

# 합산 함수
def bfs(card):
    heapq.heapify(card)
    result = 0
    while len(card) >= 2 :
        one = heapq.heappop(card)
        two = heapq.heappop(card)
        sum_val = one + two
        result = result + sum_val
        heapq.heappush(card,sum_val)
    return result    


ans = bfs(card_set)
print(ans)