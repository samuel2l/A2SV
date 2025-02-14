i=0
end=int(input())
while i<=end:
    if i%2!=0:
        curr=end-i        
        print(int(curr/2)*" ",i*"*")
    i+=1