import sys
input = sys.stdin.readline
n = int(input())

arr = []
for i in range(n):
	x, y = map(int,input().split())
	arr.append((x,y))
	
arr.sort(key=lambda x:(x[0],x[1]))
# print(arr)
# 출력
for j in arr:
	print(j[0], j[1])