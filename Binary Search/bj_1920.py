# 백준 1920
# 수찾기

import sys
input = sys.stdin.readline

#입력
n = int(input().strip())
num_list = list(map(int,input().strip().split()))
m = int(input().strip())
find_list = list(map(int,input().strip().split()))

#이진탐색은 
#무조건 정렬 !!!!
num_list.sort()
def bi_se(arr, target, s, e):
    if s > e:
        return 0
    mid = (s + e) //2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return bi_se(arr,target, s, mid-1)
    else:
        return bi_se(arr,target, mid+1, e)
    
for i in find_list:
    print(bi_se(num_list, i, -n+1, n-1))

#### 자료 구조 이용 ####    
# bj 1920
# 수 찾기
# 실버 4

# n = int(input())

# n_list = list(map(int,input().split()))

# m = int(input())

# m_list = list(map(int,input().split()))
n = 100000

n_list = list(range(1,100000))

m = 100000

m_list = list(range(1,100000))

res = False

# key:value 매칭해주기
n_map = {}

for i in n_list:
    n_map[i] = 1

# 있으면 1 출력 없으면 0 출력

for j in m_list:
    if j in n_map:
        print(1)
    else:
        print(0)
        