# 이코테 p360
# 안테나

n = int(input())
home = [list(map(int,input().split()))]

home.sort()

print(home[(n-1) // 2])