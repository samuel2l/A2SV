k,n,w=list(map(int, input().split()))
ans=0
for i in range(w):
    cost=(i+1)*k
    ans+=cost
if n>ans:
    print("0")
else:
    print(ans-n)
