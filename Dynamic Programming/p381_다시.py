# 이코테 p381
# 못생긴 수

n=int(input())

dp = [0] * n
dp[0] = 1
i2,i3,i5 = 0,0,0
n2, n3, n5 = 2,3,5

for k in range(1,n):
    dp[k] = min(n2,n3,n5)
    if dp[k] == n2:
        i2 += 1
        n2 = dp[i2] * 2
    if dp[k] == n3:
        i3 += 1
        n3 = dp[i3] * 3
    if dp[k] == n5:
        i5 += 1
        n5 = dp[i5] * 5

