t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    string="".join([str(i) for i in b])
    if "101" in string:
        print("NO")
    else:
        print("YES")
