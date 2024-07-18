# bj 12871
# 무한 문자열
# 실버 5

s = input()
t = input()

q = s * 100
p = t * 100


print(1) if q[0:100] == p[0:100] else print(0)


'''
ababab
abab
'''
'''
abcdef
abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefab
'''
