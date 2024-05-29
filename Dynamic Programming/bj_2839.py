# 백준 2839
# 설탕 배달
n = int(input())

d = [5001] * n
d.insert(0,0)

k_g = [3,5]

for i in range(2):
    for j in range(k_g[i],n+1):
        d[j] = min(d[j], d[j - k_g[i]]+1)

if d[n] == 5001:
    print(-1)
else:
    print(d[n])