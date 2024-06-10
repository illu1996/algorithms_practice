# 이코테 p376
# 정수삼각형

n = int(input())
num_list = []
dp =[]
for _ in range(n):
    a = list(map(int,input().split()))
    num_list.append(a)
    dp.append(a)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = num_list[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = num_list[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = num_list[i][j] + max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[n-1]))