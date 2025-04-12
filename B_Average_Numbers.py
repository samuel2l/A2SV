n=int(input())
a=list(map(int,input().split()))
ans=[]
avgs=[]
summ=sum(a)
for i in range(n):
    curr=a[i]


    avg=(summ-curr)/(n-1)
    avgs.append(avg)


ans=[]
for i in range(n):
    if a[i] ==avgs[i]:
        ans.append(i+1)
print(len(ans))
print(*ans)
 


    