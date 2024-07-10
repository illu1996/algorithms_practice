# pg 42840
# 모의고사

def solution(answers):
    answer = []
    N1 = [1,2,3,4,5,1,2,3,4,5] * 1000
    N2 = [2,1,2,3,2,4,2,5,2,1] * 1000
    N3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    n1_cnt, n2_cnt, n3_cnt = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == N1[i]:
            n1_cnt += 1
        if answers[i] == N2[i]:
            n2_cnt += 1
        if answers[i] == N3[i]:
            n3_cnt += 1
    
    solved = [n1_cnt ,n2_cnt,n3_cnt]
    
    # 맥스값 찾기
    max_cnt = max(solved)
    for i in range(len(solved)):
        if max_cnt == solved[i]:
            answer.append(i+1)
    
    return answer

