# 이코테 p359

# 국영수

N = int(input())
grade = [input().split() for _ in range(N)]

grade.sort(key=lambda x: (-int(x[1]), int(x[2]), -(int(x[2])), x[0]) )

for i in range(N):
    print(grade[i][0])