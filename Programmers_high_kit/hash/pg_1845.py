# pg 1845
# 포켓몬

def solution(nums):
    answer = 0
    mons = {}
    
    # 누적합
    for i in nums:
        if i not in mons:
            mons[i] = 1
        else:
            mons[i] += 1
    n = len(nums)//2
    answer = len(mons) if len(mons) < n else n
    return answer