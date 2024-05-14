# 이코테 7-5 p197
# 부품 찾기

# 리스트 내부에서 특정값을 찾는일
# in 으로 찾는 것보다 훨씬 빠르다
# 리스트의 크기에 따라 시간의 차이가 크다

import sys
import random
import math
import time


input = sys.stdin.readline

def bi_se(arr, target, start, end):
    if start > end:
        print('no', end=" ")
        return
    mid = (start + end) // 2
    if arr[mid] == target:
        print('yes', end=" ")
    elif arr[mid] > target:
        return bi_se(arr, target, start, mid -1)
    else:
        return bi_se(arr, target, mid +1 , end)
    
# n = int(input())
# owner_list = list(map(int,input().strip().split()))
# m = int(input())
# customer_list = list(map(int,input().strip().split()))

# owner_list.sort()



sorted_list = list(range(1,1000000))
random_list = list(range(1,1000000))
random.shuffle(random_list)

n = 20

choice_list = list(random.sample(sorted_list,n))
choice_list.append(10000001)
choice_list.insert(3,10000002)

print(choice_list)

start = time.time()
for i in choice_list:
    bi_se(sorted_list, i, 0, len(sorted_list)-1)
end = time.time()
print(f"{end - start:.10f} sec")

start1 = time.time()
for i in choice_list:
    if i in random_list:
        print('yes', end= " ")
    else:
        print('no', end=" ")
end1 = time.time()
print(f"{end1 - start1:.10f} sec")
