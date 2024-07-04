# pg 42586
# 기능개발
from collections import deque

def solution(pg, sp):
    answer = []
    qpg = deque(pg)
    qs = deque(sp)

    # qpg 다 끝날때 까지
    while qpg:
        # 작업량 추가하기
        for i in range(len(qpg)):
            qpg[i] += qs[i]
        
        cnt = 0
        while qpg and qpg[0] >= 100:
            # 앞에가 100 될때마다 cnt ++ and 제거
            qpg.popleft()
            qs.popleft()
            cnt += 1
        # 전체횟수 추가
        if cnt:
            answer.append(cnt)
        
    return answer