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
    print(bi_se(num_list, i, 0, n-1))