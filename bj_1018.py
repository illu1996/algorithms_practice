n, m = map(int,input().split())
#체스판
zech = [list(input()) for _ in range(n)]

# 칠하는 최소값
minV = 64

# 모든 체스판의 w칸과 b칸의 값이 같다.
# 8*8 이면 32칸은 W이고 32 칸은 B이다
# 그러므로 주어진 체스판을 8*8로 자른 값을 모두 다 확인하면서 W,B 칸의 차이가
# 최소값인걸 찾아 답 지정한다.
for a in range(n-7):
    for b in range(m-7):
        white = 0
        black = 0
        
        for i in range(a,a+8):
            for j in range(b, b+8):
                # 시작이 w일때
                if (i+j) % 2 == 0:
                    if zech[i][j] != 'W':
                        white +=1
                    if zech[i][j] != 'B':
                        black += 1
                # 시작이 b일때
                else:
                    if zech[i][j] != 'B':
                        white +=1
                    if zech[i][j] != 'W':
                        black += 1
        # 블랙과 화이트 중의 최소값과 지금까지의 최소값 비교
        if minV >(min(white,black)):
            minV = min(white,black)
print(minV)
