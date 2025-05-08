from itertools import accumulate
n=int(input())
a=sorted(map(int,input().split()),reverse=True)
m=int(input())
q=list(map(int,input().split()))

prefix=list(accumulate(a))

for coupon in q:
    print(prefix[coupon-2]+(prefix[-1]-prefix[coupon-1]))

