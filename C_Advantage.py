t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    copy=[]
    copy[:]=s[:]
    maxi=s.index(max(copy))
    copy.remove(copy[maxi])
    maxi2=s.index(max(copy))

    ans=[]
    for i in range(len(s)):
        if i==maxi:

            ans.append(s[i]-s[maxi2])
        else:

            ans.append(s[i]-s[maxi])
    print(*ans)

