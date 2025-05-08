n,s=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=0

summ=0
maxi=0
while right<len(a):
    summ=summ+a[right]
    if summ<=s:
        maxi=max(maxi,right-left+1)
        right+=1
    else:
        summ-=a[left]
        left+=1
        if summ<=s:
            maxi=max(maxi,right-left+1)
        right+=1
print(maxi)
    


