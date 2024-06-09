# 이코테 # p368
# 고정점 찾기

n = int(input())
num = list(map(int,input().split()))

def binary_search(num, s, e):
    while s<=e:
        mid = (s+e)//2
        if num[mid] == mid:
            return mid
        if num[mid] >mid:
            e = mid -1
        else:
            s = mid +1
    return -1
    
print(binary_search(num, 0, n-1))