t=int(input())
arr=[]
for _ in range(t):
    a,b=map(str,input().split())
    arr.append([a,b])

for i in arr:
    if i[0].endswith("L"):
        if i[1].endswith("L"):
            if len(i[0])>len(i[1]):
                print(">")
            elif len(i[0])<len(i[1]):
                print("<")
            else:
                print("=")
        else:
            print(">")
    elif i[0]=="M":
        if i[1].endswith("L"):
                print("<")
        if i[1].endswith("S"):
            print(">")
        if i[1]=="M":
            print("=")
    elif i[0].endswith("S"):
        if i[1].endswith("S"):
            
                if len(i[0])>len(i[1]):
                    print("<")
                elif len(i[0])<len(i[1]):
                    print(">")
                else:
                    print("=")
        else:
            print("<")





