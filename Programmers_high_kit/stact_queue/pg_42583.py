# pg 42583
# 다리를 지나는 트럭
# 레벨 2

from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 경과시간
    sec = 0
    # 다리를 건너는 트럭
    q = deque(truck_weights)
    
    #현재 다리위에 있는 트럭
    bridge = deque([0] * bridge_length)
    #다리위 트럭의 무게
    kg = 0
    while bridge:
        cplt = bridge.popleft()
        kg -= cplt
        
        if q and kg + q[0] <= weight:
            now = q.popleft()
            kg += now
            bridge.append(now)
        elif q:
            bridge.append(0)

        sec += 1
    
    return sec

print(solution(2, 10, [7,4,5,6]))

#2, 10, [7,4,5,6]
#10, 12, [4,4,4,2,2,1,1,1,1]
#10, 12, [1,1,1,1,2,2,4,4,4]