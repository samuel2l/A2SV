t=int(input())
for _ in range(t):
    x=int(input())
    p=1/3
    right=int(x**p)+1
    left=1
    solved=False
    while left<=right:
        curr=left**3 + right**3


        if curr==x:
            solved=True
            print("YES")
            break
        elif curr > x:
            right-=1
        else:
            left+=1
    if not solved:
        print("NO")
