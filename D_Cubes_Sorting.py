t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    solved=False
    #worst case bubble sort inviolves n(n-1)/2 swaps
    #to prevent that just ensure array is not strictly decreasing 
    #that way iti never reaches max num of swaps possible
    for i in range(1,n):
        if a[i]>=a[i-1]:
            solved=True
            break
    if solved:
        print("YES")
    else:
        print("NO")

    
