# 백준 1432
# 시리얼 번호 실버3

n = int(input())

# 받을때, 각 자리수의 합도 추가해주기
arr = [[input(),0] for _ in range(n)]

print(arr)
# 각 자리수의 합 구해주기
for i in range(len(arr)):
    for j in arr[i][0]:
        if j.isdigit():
            arr[i][1] += int(j)
print(arr)
# 정렬순서 : 길이, 각자리의 합, 사전순
arr.sort(key = lambda x:(len(x[0]),x[1],x[0]))

for i in arr:
    print(i[0])
    