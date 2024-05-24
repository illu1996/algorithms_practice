# 백준 13702
# 이상한 술집
import sys
imput = sys.stdin.readline

#막걸리의 개수 n, 인원수 k
n, k = map(int,input().strip().split())

#입력
alcohol_list = [ int(input()) for _ in range(n)]

answer = 0
s=1
e=max(alcohol_list)

#이분 탐색
while s<=e :
    #반례 없애려면 s를 1 로 하면 된다.
 
    mid = (s+e)//2
    sum_count = 0
    for i in alcohol_list:
        sum_count += i//mid
    if sum_count < k:
        e = mid - 1
    else:
        answer=mid
        s = mid +1
print(answer)
        
        