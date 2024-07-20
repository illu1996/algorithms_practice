# 슬라이딩윈도우

arr =  [1,2,3,4,5,6,7]
n = 7
k = 3
max_cnt = 0
for i in range(n-k+1):
    sum_  =sum(arr[i:i+k])
    print(sum_, end=' ')
print(max_cnt)
print('-------')
arr =  [1,2,3,4,5,6,7]
n = 7
k = 3


sum_ = sum(arr[:k])
max_cnt = sum_
for i in range(k,n):
    sum_ += arr[i] - arr[i-k]
    max_cnt = max(sum_,max_cnt)
    print(sum_, end=' ')
print(max_cnt)