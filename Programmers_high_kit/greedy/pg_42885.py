# pg 42885
# 구명보트

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q = deque(people)
    
    while q:

        now = q.popleft()
        if q and now + q[-1] <= limit:
            q.pop()

        answer += 1
        
    return answer