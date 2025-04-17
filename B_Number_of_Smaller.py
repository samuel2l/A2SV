n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

p1=0
ans=[]

for i in range(m):
    while p1<n and a[p1]< b[i]:
        p1+=1
    ans.append(p1)

print(*ans)