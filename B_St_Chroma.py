t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    permutation=[i for i in range(n)]
    # ans=[]
    if x in permutation:
        ans=permutation[:x]+permutation[x+1:]+[x]
        print(*ans)
    else:
        ans=permutation[:x]+permutation[x+1:]
        print(*ans)
