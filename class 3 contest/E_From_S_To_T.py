q=int(input())
queries=[]
for _ in range(q):
    s=input()
    t=input()
    p=input()
    queries.append([s,t,p])

for i in queries:
    #p
    for char in i[2]:
        #s
        
        if i[0]==i[1]:
            print("YES")
            
        for j in range(len(i[0])-1):
            
            new=i[0][:j] + char + i[0][j+1:]
            if new==i[1]:
                print("YES")
    print("NO")
             


