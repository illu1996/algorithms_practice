# bj 1620
# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int,input().strip().split())
pocket = {}
for i in range(n):
    name = input().strip()
    pocket[name] = i + 1
    pocket[str(i+1)] = name

solve = [input().strip() for _ in range(m)]

for i in solve:
    print(pocket[i])