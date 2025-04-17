t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    # x component is always even
    #check if n is odd if odd and k is even there is no possible combo
    if n%2!=0 and k%2==0:
        print("NO")
    else:
        print("YES")



