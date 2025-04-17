n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a_p=0
b_p=0
ans=[]
while a_p < n and b_p <m:
    if a[a_p]<=b[b_p]:
        ans.append(a[a_p])
        a_p+=1
    else:
        ans.append(b[b_p])        
        b_p+=1


if a_p==n:
    ans+=b[b_p:]
if b_p==m:
    ans+=a[a_p:]

print(*ans)