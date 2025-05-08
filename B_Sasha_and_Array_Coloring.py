t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    left=0
    right=len(a)-1
 
    ans=0
    while left<right:
        ans+=(a[right]-a[left])
        left+=1
        right-=1
    print(ans)