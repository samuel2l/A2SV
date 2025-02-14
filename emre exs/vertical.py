i=0
# end=int(input())
ans=[]
end=11
while i<=end-2:
    curr=(end-2)-i  
    print(int(curr)*" ",i*"*")
        
    i+=1

while i>=1:
    if i==end-2 or i==end-1:
        pass
    else:
        curr=(end-2)-i  
        print(int(curr)*" ",i*"*")
        
    i-=1
