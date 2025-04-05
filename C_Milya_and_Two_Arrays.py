t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    length=len(set(a))+ len(set(b))
    if length>3:
        print("YES")
    else:
        print("NO")

    