# 백준 2294 동전 2
# 실버 5

n,k = map(int,input().split())


cent = [int(input()) for _ in range(n)]
n_list = [0] * 300001
for i in cent:
    n_list[i] = 1

for i in range(len(n_list)):
    for j in cent:
        if i % j ==0:
            n_list[i] = i // j
    
for i in range(max(cent),len(n_list)):
    n_list[i] = m