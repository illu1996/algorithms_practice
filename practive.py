from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 경과시간
    cnt = 0
    # 다리를 건너는 트럭
    q = deque(truck_weights)
    
    #현재 다리위에 있는 트럭
    origin = [0] * bridge_length
    bridge = deque(origin)
    
    while bridge:
        
        # 무게를 초과하지 않는다면
        if q and sum(bridge) + q[0] <= weight:
            bridge.popleft()
            bridge.append(q.popleft())
        else:
            if q:
                if sum(bridge) - bridge[0] + q[0] <= weight:
                    bridge.popleft()
                    bridge.append(q.popleft())
                else:
                    bridge.popleft()
                    bridge.append(0)
            else:
                bridge.popleft()
        cnt += 1
        print(bridge, cnt)
    
    return cnt

print(solution(2, 10, [7,4,5,6]))

#2, 10, [7,4,5,6]
#10, 12, [4,4,4,2,2,1,1,1,1]
#10, 12, [1,1,1,1,2,2,4,4,4]