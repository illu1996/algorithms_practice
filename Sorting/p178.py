#위에서 아래로
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
    
lst.sort(reverse=True)
for j in lst:
    print(j,end=" ")