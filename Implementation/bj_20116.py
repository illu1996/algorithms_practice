# bj 20116
# 상자의 균형
# 실버 3

n,l = map(int,input().split())
x_list = list(map(int,input().split()))
sum_x = 0

for i in range(n-1,0,-1):
    sum_x += x_list[i]
    kg_avr = sum_x / (n-i)
    if  not x_list[i-1] - l < kg_avr < x_list[i-1] + l:
        print('unstable')
        break
else:
    print('stable')
