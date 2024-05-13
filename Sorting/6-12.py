# 이코테 6-12 p182
# 두 배열의 원소교체

n,k = map(int,input().split())
for _ in range(1):
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2,reverse=True)

result = arr2[0:k] +arr1[k:len(arr2)+1]
print(result)
print(sum(result))
    