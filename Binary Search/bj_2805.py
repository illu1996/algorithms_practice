# 백준 2805
# 나무자르기

import sys
input = sys.stdin.readline

# 입력
n, m = map(int,input().strip().split())
tree_list = list(map(int,input().strip().split()))

# 자르는 높이
# 시작 0
# 끝 max(tree_list)
s = 0
e = max(tree_list)
result = 0


while s<= e:
    mid = (s+e) // 2
    h = 0
    for i in tree_list:
        if mid < i:
            h += i - mid
    # 총합이 목표값보다 큰 경우 나무를 더 작게 잘라야하므로 오른쪽 탐색
    if h < m:
        e = mid -1
    # 여기서 if 문의 순서가 중요한 것은 가져가는 나무의 길이와
    # m 이 같은 경우를 생각해야한다
    else:
        result = mid
        s = mid + 1

print(result)