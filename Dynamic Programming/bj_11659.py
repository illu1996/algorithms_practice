# bj 11659
# 구간합 구하기 4
# 실버 3
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
num = list(map(int,input().split()))
dp = [0]* (n+1)
for i in range(n):
    dp[i+1] = dp[i] + num[i]

for i in range(m):
    a,b = map(int,input().split())
    print(dp[b]-dp[a-1])