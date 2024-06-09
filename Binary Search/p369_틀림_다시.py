# 이코테 p369
# 공유기 설치

# 집개수 n 공유기 개수 c
n, c =map(int,input().split())
home = [int(input()) for _ in range(n)]

home.sort()

max_value = 0
install_home = [home[0],home[-1]]

def dist(x,y,z):
    return abs(abs(x-y)-abs(y-z))


# 최대값이 되는 인덱스 반환
def bi_se(home,s,e,max_value,max_mid):
    if s>e:
        return
    mid = (s+e) // 2
    # 설치 조건
    if dist(s,e,home[mid])> max_value:
        max_value = dist(s,e,home[mid])
        max_mid = mid
    bi_se(home,s,mid-1,max_value,max_mid)
    bi_se(home,mid+1,e,max_value,max_mid)
    return max_mid
    
count = 2
# c개 까지 설치
while count <= c:
    max_mid = -1
    max_value = 0
    # 찾아서 설치하기
    install_home.append(home[bi_se(home,0,n-1,max_value,max_mid)])
    count += 1

install_home.sort()
min_val = 1e9

for i in range(1,len(install_home)):
    if abs(install_home[i]- install_home[i-1]):
        min_val = min(min_val,abs(install_home[i] - install_home[i-1]))
print(min_val)