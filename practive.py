from collections import deque
home = [1,6,8,9,11]
def bi_se(home,s,e,max_value,max_mid):
    if s>e:
        return
    mid = (s+e) // 2
    # 설치 조건
    if dist(s,e,home[mid])> max_value:
        max_value = dist(s,e,home[mid])
        max_mid = mid
    bi_se(home,s,mid-1,max_value,max_mid)
    bi_se(home,mid+1,e,max_value,max_mid)
    return max_mid
    