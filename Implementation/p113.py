## 예제 4-1 상하 좌우
# 난이도 1

# 시간제한 1초
# 메모리 제한 128MB

# 00 : 00 : 00 부터 n : 59 : 59 까지 3 이 하나라도 포함되면 세어야 함

# 입력 시간
n = int(input())

h = list(range(0,n+1))
m = list(range(0,60))
s = list(range(0,60))

# "3"을 찾는 함수

def find_three(str):
    if "3" in str:
        return True
    return False

# 3이 포함된 카운트
cnt = 0
# 3중 포문
for i in range(len(h)):
    for j in range(len(m)):
        for k in range(len(s)):
            now = str(h[i])+str(m[j])+str(s[k])

            if find_three(now):
                cnt += 1

print(cnt)
