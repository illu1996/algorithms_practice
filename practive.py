def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2,int(x**0.5)+ 1):
            if x%i == 0:
                return False
    return True

def solution(numbers):
    str_num = list(map(str,numbers))
    per = []
    for i in range(1,len(numbers)+1):
        per += list(permutations(str_num,i))