# 문자열 압축

def solution(s):
    lenS = len(s)
    half = lenS // 2
    min_len = 1e19
    
    # 한글자인 경우
    if lenS==1:
        answer = 1
        return answer
    
    # 절반 이상은 확인 필요 없다
    for i in range(1,half + 1):

        # 비교할 문자열
        alpha = s[0:i]
        # 개수
        cnt = 1
        # 완성본
        rst = ''
        
        # 몇개 같은지 확인
        for j in range(i,lenS+1,i):
            # 같으면 개수 증가
            if s[j:j+i] == alpha:
                cnt += 1
                
            # 다르면 여태까지 반복된 수  추가 후 초기화
            else:
                # 1이면 숫자 추가 하지 않음
                if cnt != 1:
                    rst += str(cnt)
                rst += alpha
                alpha= s[j:j+i]
                cnt = 1
            # 딱 떨어지지 않으면 나머지 만큼 추가하기
        if lenS%i != 0:
            rst += s[len(rst):len(rst) + lenS%i]

        #과반수 넘으면 그냥 추가해주기
        min_len = min(len(rst),min_len)

    
    answer = min_len
    return answer


# print(solution("a"))
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
