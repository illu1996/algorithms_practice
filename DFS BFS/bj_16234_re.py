# bj 16234
# 인구 이동
# 골드 4

n, l, r = map(int, input().split())
person = []
for i in range(n):
    person.append(list(map(int, input().split())))

visit = list([0] * n for _ in range(n))
union = []
date = 0
