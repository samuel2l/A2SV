n = int(input())

for i in range(n+1):
    ans = ""

    for j in range(i+1):
        ans+=str(j)+" "

    for j in range(i-1,-1,-1):
        ans+=str(j)+" "
 
    print(" "*(2* (n - i))+ans)

for i in range(n-1,-1,-1):
    ans=""

    for j in range(i+1):
        ans+=str(j)+" "

    for j in range(i-1,-1,-1):
        ans+=str(j)+" "

    ans=ans.strip()
    print(" "*(2*(n-i))+ans)