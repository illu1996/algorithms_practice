#이코테 8-6, p220
# 개미전사

n = int(input())
food = list(map(int,input().split()))
food.insert(0,0)
print(food)
d = [0]* (n+2)

d[1] = food[1]
d[2] = food[2]
for i in range(3,n+2):
    d[i] = max(d[i-2]+food[i-1],d[i-3]+food[i-1] )
print(d)
    
print(d[-1]) 