# 이코테 p311
# 모험가 길드

n = int(input())
people = list(map(int,input().split()))

count = 0
people.sort(reverse=True)

whole = len(people)

start = 0
while whole > 0 and whole >= people[start]:
    
    count += 1
    whole -= people[start]
    start = people[start]

print(count)