# bj 1166
# 선물
# 싧버 3

n, l, w, h = map(int,input().split())
v = l* w * h
min_val = max(l,w,h)
s =0
e = min_val
max_val = 0
for i in range(10000):
    mid = (s + e) / 2

    if (l//mid) *(w//mid)*(h//mid) >= n:
        max_val = mid
        s= mid
    else:
        e = mid
print("%.10f" %(max_val))
