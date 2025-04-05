n=int(input())
arrs=[]
lengths=[]
for _ in range(n):
    l=int(input())
    lengths.append(l)
    arr=list(map(int,input().split()))
    for i in range(len(arr)):

        if arr[i]==1:
            arr[i]=2

    for i in range(len(arr)-1):
        if str(arr[i]/arr[i+1])[-2:]==".0" or str(arr[i+1]/arr[i])[-2:]==".0":
            arr[i+1]+=1
    print(*arr)