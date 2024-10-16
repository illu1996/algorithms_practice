# bj 1051 실버3
# 숫자 정사각형

# 크기가 1부터 50까지 모든 정사각형을 확인후
# 꼭지점이 다 같다면 배열에 제곱수를 추가
# 이후 가장 큰 크기 반환

n,m = map(int,input().split())
num= [list(map(int,input())) for _ in range(n)]
ans = []

i,j = 0,0
size = m if n >=m else n

while size > 0:

    # 4 꼭지가 모두 같을때,
    if num[i][j] == num[i + size - 1][j] == num[i][j + size -1] == num[i + size -1][j + size -1]:
        ans.append(size ** 2)
        
    j += 1
    
    # j(열) 가 범위를 넘어가면 행을 1 키우기
    if j + size -1 >= m:
        j = 0
        i += 1
    # 행의 범위 넘으면 사이즈 줄여가며 확인
    if i + size -1 >= n:
        size -= 1
        i,j=0,0

print(max(ans))
        