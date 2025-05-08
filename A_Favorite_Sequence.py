t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    end=len(b)-1
    start=0
    i=0
    copy=["00"]*len(b)
    idx=0
    for j in range((len(b)//2)+1):
        if i<len(b):
            # print(b[j])
            copy[i]=b[j]
            i+=2
    # print(copy)
    # print(copy)
    rem=(len(b)//2)
    remm=b[-rem:]
    # print(copy)
    # print(remm)
    idx=len(remm)-1
    for i in range(len(copy)):
        # print("curr i",i)
        if copy[i]=="00":
            copy[i]=remm[idx]
            idx-=1
    #     # print(b[i])
    print(*copy)
        # print("ah i",i)
    # print(*copy)


