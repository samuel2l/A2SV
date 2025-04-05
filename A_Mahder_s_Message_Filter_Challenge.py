t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    i=-1
    isSolved=False
    while abs(i)<=n:
        if s[i]==")":
            i-=1
        else:
            break

    num_brackets=abs(i+1)
    num_normal=n-num_brackets

    if num_brackets>num_normal:
        print("Yes")
    else:
        print("No")

