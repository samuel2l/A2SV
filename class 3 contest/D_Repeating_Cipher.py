n=int(input())
t=input()
ans=''
i=0
cnt=2
while i< n:
    if i==0:
        ans+=t[i]
        i=2
    else:
        ans+=t[i]
        cnt+=1
        i+=cnt   
        
print(ans)
