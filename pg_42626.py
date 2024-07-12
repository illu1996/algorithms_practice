# pg 42626
# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    
    # 우선순위 만들기
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        
        # 첫번째거 먼저 꺼내기
        first = heapq.heappop(scoville)
        
        # 작다면 하나 더 꺼내서 다시 넣어주기
        if first < K:
            second = heapq.heappop(scoville)
            answer += 1
            heapq.heappush(scoville, first + second * 2)
        
        #크다면 추가하기
        else:
            break
    
    # scoville 2개 짜리 반례
    if scoville[0] < K:
        return -1
    
    return answer