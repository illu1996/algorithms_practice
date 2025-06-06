# 왕실의 나이트
# 실전문제
# 난이도 1
# 풀이시간 20분
# 시간제한 1초
# p 115


# 제한 조건
# 8 x 8 체스판
# 나이트는 L 자 형태로만 이동
# 수평 2칸 + 수직 1칸
# 수직 2칸 + 수평 1칸

# 위치 문자열 입력
loc = input()
ox = int(ord(loc[0]))-int(ord('a'))
oy = int(loc[1])-1
dir = [(1,2), (1,-2),(-1,2),(-1,-2), (2,-1),(-2,-1),(2,1), (-2,1)]

cnt = 0

for x,y in dir:
    nx = ox + x
    ny = oy + y
    
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1

print(cnt)