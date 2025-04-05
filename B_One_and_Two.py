t=int(input())

def mul(seq):
    
    cnt=seq.count(2)
    return 2*cnt


for _ in range(t):
    n=int(input())
    isSolved=False
    sequence=list(map(int,input().split()))
    ans={}
    after={}
    for i in range(len(sequence)-1):
        ans[i]=mul(sequence[:i+1])
        after[i]=mul(sequence[i+1:])

    for i in range(len(sequence)-1):

        if ans.get(i,-1 )==after.get(i,-2 ):
            isSolved=True
            print(i+1)
        if isSolved:
            break
    if isSolved==False:
        print(-1)

