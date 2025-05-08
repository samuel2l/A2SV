from itertools import accumulate
n,q=map(int,input().split())
p=sorted(map(int,input().split()),reverse=True)
prefix=list(accumulate(p))

for _ in range(q):
    x,y=map(int,input().split())
    if x-y-1<0:
        print(prefix[x-1])
    else:
        print(prefix[x-1]-prefix[x-y-1])
