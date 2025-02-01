q=int(input())
queries=[]
for _ in range(q):
    s=input()
    t=input()
    p=input()
    queries.append([s,t,p])
print(queries)
for i in queries:
    print("i",i)
    
    #p
    for char in i[2]:
        #s
        print("CHAR",char)
        
        if i[0]==i[1]:
            print("YES")
            
        for j in range(len(i[0])-1):
            
            i[0]=i[0][:j] + char + i[0][j+1:]
            print("i[0]w",i[0])
            if i[0]==i[1]:
                print("YES")
    print("NO")
             


