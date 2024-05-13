# 백준 1946
# 신입사원

#입력
t = int(input())
#테스트 케이스 만큼 실행
for _ in range(t):
    #사원 수
    person = int(input())
    #성적
    grade = []
    #성적 입력
    for i in range(person):
        a,b = map(int,input().split())
        grade.append((a,b))
    #합격자 수
    count = 1
    #정렬
    result1 = sorted(grade)
    
    max_ = result1[0][1]
    
    for i in range(1,person):
        if max_ > result1[i][1]:
            count += 1
            max_ = result1[i][1]
    print(count)
        

