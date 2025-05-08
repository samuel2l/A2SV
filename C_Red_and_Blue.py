t=int(input())
for _ in range(t):
    r_len=int(input())
    r=list(map(int,input().split()))
    b_len=int(input())
    b=list(map(int,input().split()))

    #using kadanes algorithm
    # total=r+b

    curr=maxi=b[0]
    for i in range(1,len(b)):
        curr=max(b[i],curr+b[i])
        maxi=max(maxi,curr)


    # print(maxi)
    # print("r",r)
    currR=maxiR=r[0]
    for i in range(1,len(r)):
        currR=max(r[i],currR+r[i])
        maxiR=max(maxiR,currR)
    print(maxiR+abs(maxi))


    