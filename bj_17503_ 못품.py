# bj 17503
# 맥주축제

import sys,heapq
input = sys.stdin.readline

n, m, k = map(int,input().strip().split())
drink = [list(map(int,input().strip().split())) for _ in range(k)]

#맥주 도수가 낮으면서, 선호도도 낮은 순서대로
drink.sort(key = lambda x: (x[1],x[0]))
# 만족도
happy = 0
pq= []


for i in drink:
    happy += i[0]
    heapq.heappush(pq, i[1])
    if len(pq) == n:
        if happy >= m:
            answer = i[1]
            break
        else:
            pass