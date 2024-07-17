# pg 42587
# 프로세스
# 레벨 2

from collections import deque

def solution(priorities, location):
    q = deque([])
    for i,j in enumerate(priorities):
        q.append((i,j))
    answer = []
    
    while q:
        idx, prior = q.popleft()
        for i,j in q:
            if prior < j:
                q.append((idx, prior))
                break
        else:
            answer.append(idx)    
    
    return answer.index(location) + 1