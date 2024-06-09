# 이코테 p367
# 정렬된 배열에서 특정 수의 개수 구하기

n, k = map(int,input().split())
num =  list(map(int,input().split()))

def bi_search(num, s,e,k):
    global count
    if s > e:
        return
    mid = (s+e) // 2
    
    if num[mid] == k:
        count +=1 
    if num[mid] >= k:
        bi_search(num,s,mid-1,k)
    if num[mid] <= k:
        bi_search(num,mid+1,e ,k)

count = 0
bi_search(num,0,n-1,k)
if count:
    
    print(count)
else:
    print(-1)