# 이코테 6-11, p180
# 성적이 낮은 순서로 출력하기

n = int(input())
arr = []
for _ in range(n):
    x = input().split()
    arr.append((x[0],int(x[1])))
    
arr = sorted(arr,key = lambda s:s[1])

for i in arr:
    print(i[0])
    
    