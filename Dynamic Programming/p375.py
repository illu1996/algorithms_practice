# 이코테 p 375
# 금광
T= int(input())
for _ in range(T):
    n, m = map(int,input().split())
    gold_map = list(map(int,input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(gold_map[index:index+m])
        index += m
    
    
    # 새로운 그래프 만들어주기
    for j in range(1,m):
        for i in range(n):
            if i==0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left,left_down, left_up)

    result = 0
    for i in range(n):
        result = max(result, dp[i][-1])
    print(result)