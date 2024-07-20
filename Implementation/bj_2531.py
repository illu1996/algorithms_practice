# bj 2531
# 회전 초밥
# 실버 1

n, d, k, c = map(int,input().split())
chobab = [int(input()) for _ in range(n)]

max_cnt = 0
# 초밥을 k만큼 자르기
for i in range(n):
    if i + k > n:
        cnt = len(set(chobab[i:n] + chobab[:(i+k)%n] + [c]))
    else:
        cnt = len(set(chobab[i:i+k] + [c]))
    
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)