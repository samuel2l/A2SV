t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    solved=False
    if k in a:
        print("0")
        solved=True
        continue

    a.sort()
    a[:]=a[::-1]
    coins=0
    i=0

    while i<len(a) and coins<=k:
        if coins+a[i]<=k:
            coins+=a[i]
        else:
            break
        i+=1

    if coins==k:
        print("0")
        continue
    else:
        print(k-coins)