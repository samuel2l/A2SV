def sign(num):
    return num > 0

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    
    p1=0
    ans=0
    while p1<n:
        #update p2 to where p1 is
        p2=p1

        #current max is maxi but check its next elements of same sign and update
        maxi=a[p1]

        while p2<n and sign(a[p1])==sign(a[p2]):
            maxi=max(maxi,a[p2])
            p2+=1
        #add maxi to subsequence
        ans+=maxi
        #Update p1 to where p2 ended
        p1=p2
    print(ans)