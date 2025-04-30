# 기둥과 보
from copy import deepcopy


def solution1(n, build_frame):
    # 기둥 과 보를 설치되는 좌표 공간 n개 맵이니 기둥이 n+1개가 나올 수 있다
    map_lst = [[0] * (n+1) for _ in range(n+1)]
    # 기둥 1, 보 2
    # 설치 1 삭제 0
    # 벽면 벗어나면 x
    # 바당에 보 설치 x 
    # 교차점 좌표를 기준으로 보는 오른쪽 기둥은 위쪽 - > 반대로 기둥 아래로, 보 왼쪽으로
    
    for x,y,a,b in build_frame:
        # 설치
        if b == 1:
            # 기둥일때,
            if a == 0:
                # 보 이거나 바닥면 확인 필요
                if x == 0 or map_lst[x-1][y] == 1 or map_lst[x][y-1] == 2 or map_lst[x][y+1] == 2:
                    map_lst[x][y] = 1
            
            # 보일때
            elif a == 1:
                # 양 옆 기둥 확인
                if map_lst[x-1][y] == 1 or map_lst[x+1][y] == 1:
                    map_lst[x][y] = 2
                else:
                    break
        # 삭제
        else:
            # 기둥일때
                # 우측 위가 보거나 위에 기둥이 있거나 위에 보가 있으면 break
                
            # 보일때
                # 양 옆으로 기둥이 없다면 무시
            pass
    
    for i in range(n):
        for j in range(n):
            pass
            # 기둥과 보 확인해서 answer에 넣어주기
    # 정렬하기
    
    answer = [[]]
    return answer

    

def able0(x,y,lst):
    #하단이면
    if y == 0:
        return True
    #밑에 기둥 있으면
    elif [x,y-1,0] in lst:
        return True
    #밑에 보 있으면
    elif ([x-1,y,1] in lst) or ([x,y,1] in lst):
        return True
    #나머지 실패
    else:
        return False

def able1(x,y,lst):
    #한쪽이라도 기둥이 있으면
    if ([x,y-1,0] in lst) or ([x+1,y-1,0] in lst):
        return True
    #양 옆에 보가 있으면
    elif ([x-1,y,1] in lst) and ([x+1,y,1] in lst):
        return True
    #나머지 실패
    else:
        return False

def del0(x,y,lst):
    nlst = deepcopy(lst)
    nlst.remove([x,y,0])
    #위에 기둥이 있을 때 확인
    if ([x,y+1,0] in nlst) and not able0(x,y+1,nlst):
        return False
    #위에 보가 있을 때 확인
    elif ([x,y+1,1] in nlst) and not able1(x,y+1,nlst):
        return False
    #위 옆에 보가 있을 때 확인
    elif ([x-1,y+1,1] in nlst) and not able1(x-1,y+1,nlst):
        return False
    else:
        return True

def del1(x,y,lst):
    nlst = deepcopy(lst)
    nlst.remove([x,y,1])
    #이 위치에 기둥이 있을 때 확인
    if [x,y,0] in nlst and not able0(x,y,nlst):
        return False
    #오른쪽에 기둥이 있을 때
    if [x+1,y,0] in nlst and not able0(x+1,y,nlst):
        return False
    #왼쪽에 보 있을 때 확인
    elif [x-1,y,1] in nlst and not able1(x-1,y,nlst):
        return False
    #오른쪽에 보 있을 때 확인
    elif [x+1,y,1] in nlst and not able1(x+1,y,nlst):
        return False
    else:
        return True

def solution(n, build_frame):
    answer = []
    for x,y,k,ox in build_frame:
        if k == 0 and ox == 1 and able0(x,y,answer):
            answer.append([x,y,0])
        elif k == 0 and ox == 0 and del0(x,y,answer):
            answer.remove([x,y,0])
        elif k == 1 and ox == 1 and able1(x,y,answer):
            answer.append([x,y,1])
        elif k == 1 and ox == 0 and del1(x,y,answer):
            answer.remove([x,y,1])

    answer.sort()

    return answer
    

solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])