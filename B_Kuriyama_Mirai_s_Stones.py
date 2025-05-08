from itertools import accumulate
n=int(input())
v=list(map(int,input().split()))
m=int(input())
rev=sorted(v)
rev_prefix=list(accumulate(rev))
prefix=list(accumulate(v))

for i in range(m):
    ty,l,r=map(int,input().split())
    if ty>1:
        
        if l-2<0:
            print(rev_prefix[r-1])
        else:
        
            print(rev_prefix[r-1]-rev_prefix[l-2])
    else:

        if l-2<0:
            print(prefix[r-1])
        else:
        
            print(prefix[r-1]-prefix[l-2])

        
    count = defaultdict(int)
    count[0] = 1 
    curr=0
    ans=0

    for i in range(n):
        curr+=int(s[i])
        
        key=curr-(i+1)
        ans+=count[key]
        count[key]+=1

    print(ans) 