s= int(input())
t= list(map(int,input().split()))
t=sorted(t,reverse=True)
ans=0

for i in range(len(t)):

    if t[i]<0:
        ans=t[i]
        break
    if int(t[i]**(0.5))!=t[i]**0.5:
        ans=t[i]
        break

print(ans)
