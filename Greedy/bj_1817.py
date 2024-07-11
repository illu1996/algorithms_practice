# bj 1817
# 짐챙기는 숌

n,m = map(int,input().split())
if not n:
    pass
else:
    book_list = list(map(int,input().split()))

# 가방의 개수
cnt = 0
# 북리스트 접근
index = 0

while index < n :
    # 책을 담은 가방의 무게
    weight = 0
    while index < n :
        weight += book_list[index]
        if weight > m:
            break
        index += 1
    cnt += 1

print(cnt)