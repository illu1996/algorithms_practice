# 성적이 낮은 순서로 학생 출력하기

n = int(input())
lst = [tuple(input().split()) for _ in range(n)]

lst.sort(key=lambda x: x[1])

for name,sum in lst:
    print(name, end=" ")
