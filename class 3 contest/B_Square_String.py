t=int(input())
arr=[]
for i in range(t):
    a=input()
    arr.append(a)
for i in arr:

    if len(i)%2==0 and (i[len(i)//2:]==i[:len(i)//2]):
        print("YES")
    else:
        print("NO")

