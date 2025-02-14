s= int(input())
t= list(map(int,input().split()))

t.sort()
ans=0
print(t)
# print(len(t))2
for i in range(len(t)-1,-1,-1):
    print(t[i]**0.5)
    print(int(t[i]**0.5)==t[i]**0.5)
    

 
    if  int(t[i]**0.5)!=t[i]**0.5:
        ans=t[i]
        break
print(ans)

