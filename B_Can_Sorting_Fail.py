t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    sort=sorted(arr)
    solved=False
    ans=[]
    # for i in range(1,n):
    copy=arr.copy()
    #     length=i
    #     copy[:length+1]=sorted(arr[:length+1])
    #     copy[n-length:]=sorted(arr[n-length:])

    if copy==sort:
        print("NO")
    else:
        print("YES")




    