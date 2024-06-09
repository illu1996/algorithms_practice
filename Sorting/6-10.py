#이코테 6-10 , p178
# 위에서 아래로

n = int(input())
num = []
for _ in range(n):
    x = int(input())
    num.append(x)

num.sort(reverse=True)
print(num)

#선택정렬 = 가장작은 인덱스 찾기 내림차순이므로 가장 큰 인덱스 찾기

for i in range(len(num)):
    min_index = i
    for j in range(i+1,len(num)):
        if num[min_index] > num[j]:
            min_index = j
    num[i],num[min_index] = num[min_index],num[i]
print(num)


#삽입 정렬
num= [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(num)):
    for j in range(i,0,-1):
        if num[j] < num[j-1]:
            num[j],num[j-1]=num[j-1],num[j]
print(num)


#퀵정렬
def q(num,s,e):
    if s >= e:
        return
    p = s
    l = s+1
    r = e
    while l <= r:
        while l <=e and num[l] <= num[p]:
            l += 1
        while r > s and num[r] >= num[p]:
            r -=1
        if l > r:
            num[p],num[r] = num[r],num[p]
        else:
            num[l],num[r] = num[r],num[l]
    q(num,s,r-1)
    q(num,r+1,e)
    
q(num,0,len(num)-1)
print(num)
        