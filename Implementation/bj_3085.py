# 백준 3085 사탕게임
# 실버 2

# CNT 함수 안에 max() 함수보다 if 문이 시간을 덜 잡아 먹는다
import sys
input = sys.stdin.readline
n = int(input())
candy = [list(input()) for _ in range(n)]

ans = 0

def cnt(arr,n):
    max_cnt = 1
    for i in range(n):
        row_count = 1
        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]  :
                row_count += 1
            else:
                row_count = 1
            max_cnt = max(max_cnt,row_count)
            # if max_cnt < row_count:
            #     max_cnt = row_count
        count = 1
        for k in range(1,n):
            if arr[k][i] == arr[k-1][i]  :
                count += 1
            else:
                count = 1
            max_cnt = max(max_cnt,count)
                
            # if max_cnt < count:
            #     max_cnt = count
    return max_cnt
    
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            # 가로줄  바꾸기
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            ans = max(ans,cnt(candy,n))
            
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        if i + 1 < n:
            # 세로줄 바꾸기
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            ans = max(ans,cnt(candy,n))

            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
print(ans)