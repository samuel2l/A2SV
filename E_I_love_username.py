n=int(input())
points=list(map(int,input().split()))
ans=0
for i in range(1,len(points)):
        if points[i]>max(points[:i]) or points[i]<min(points[:i]):
                ans+=1

print(ans)
                
    