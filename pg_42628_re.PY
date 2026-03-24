# pg 42628
# 이중우선순위큐
# 레벨 3

# 내풀이
# pop으로 불가능

import heapq
def solution(operations):
    q = []
    heapq.heapify(q)
    for i in operations:
        if i[0] == 'I':
            n, num = i.split(' ')
            heapq.heappush(q,int(num))
        else:
            if i == 'D 1' and len(q) != 0 :
                q.pop()

            elif i == 'D -1' and len(q) != 0:
                heapq.heappop(q)

    if len(q) == 0:
        answer = [0, 0]
    elif len(q) ==1:
        answer = [q[0], q[0]]
    else:
        answer = [q.pop(), heapq.heappop(q)]
    return answer

# 다른사람 풀이

# min max q 만들기

class MaxMinQueue() :
    # 큐, 맥스인덱스, 민인덱스 선언
    def __init__(self):
        self.queue = []
        self.maxIdx = None
        self.minIdx = None
    
    # 비었을때
    def isEmpty(self):
        return not self.queue
    
    def enqueue(self, data=None):
        # 비어있다면
        if self.isEmpty():
            self.maxIdx = 0
            self.minIdx = 0
            self.queue.append(data)
            return
         
        # 비어있지 않다면
        # 넣은 데이터가 큰값이면 max인덱스를 마지막 값으로
        if data > self.queue[self.maxIdx]:
            self.maxIdx = len(self.queue)
        
        # 작은 값이면
        # 넣은 데이터가 작은값이면 min인덱스를 마지막 값으로
        if data < self.queue[self.minIdx]:
            self.minIdx = len(self.queue)
        self.queue.append(data)
    
    def delmax(self):
        if self.isEmpty():
            return
        self.queue.pop(self.maxIdx)
        if self.maxIdx < self.minIdx:
            self.minIdx  -=1
        if self.isEmpty():
            self.maxIdx = None
            self.minIdx = None
            return
        self.maxIdx = self.queue.index(max(self.queue))
    
    def delmin(self):
        if self.isEmpty():
            return
        self.queue.pop(self.minIdx)
        if self.minIdx < self.maxIdx:
            self.maxIdx -= 1
        if self.isEmpty():
            self.maxIdx = None
            self.minIdx = None
            return
        self.mixIdx = self.queue.index(min(self.queue))

def solution(operations):
    Structure = MaxMinQueue()
    
    for oper in operations:
        deter = oper[0]
        
        if deter == 'I':
            Structure.enqueue(int(oper[2:]))
        else:
            if oper[2:] == '1':
                Structure.delmax()
            elif oper[2:] == '-1':
                Structure.delmin()
            else:
                return -1
    if Structure.isEmpty():
        return [0,0]
    else:
        return [Structure.queue[Structure.maxIdx],Structure.queue[Structure.minIdx]]