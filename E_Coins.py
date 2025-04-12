t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    solved=False

    if n%2==0:
        solved=True
    #try smallest value of k. If the remainder is even then 2x can add and hence is possible
    if (n-k)%2==0:
        solved=True
                
    if solved:
        print("YES")
    else:
        print("NO")



