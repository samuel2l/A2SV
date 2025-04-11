t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    smallest=a.index(min(a))
    biggest=a.index(max(a))

    print(smallest+1,biggest+1)
