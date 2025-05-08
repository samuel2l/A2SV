from collections import Counter
from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=defaultdict(int)
    solved=False
    # for i in count:
    #     if count[i]>=3:
    #         solved=True
    #         print(i)
    #         break
    # if not solved:
    #     print(-1)

    for i in a:
        count[i]+=1
        if count[i]>=3:
            print(i)
            solved=True
            break
    if not solved:
        print(-1)
    


