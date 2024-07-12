# pg 42578
# 의상

def solution(clothes):
    answer = 1
    cloth = {}
    cnt = []
    
    # 해시 만들어서 추가하기
    for i in range(len(clothes)):
            
            if clothes[i][1] in cloth:
                cloth[clothes[i][1]].append(clothes[i][0])
            else:
                cloth[clothes[i][1]] = [clothes[i][0]]
    
    # 경우의 수 = 모든 값 곱하기,
    # 조건 안입은 경우의수 있으니 각 개수의 +1, 전체 안입는 경우는 없으니 전체에서 1 빼기
    for i in cloth:
        cnt.append(len(cloth[i])+1)
    
    for i in cnt:
        answer *= i
    answer -=1

    return answer