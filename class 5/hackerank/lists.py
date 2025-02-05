if __name__ == '__main__':
    N = int(input())
    inputs=[]
    arr=[]

    for i in range(N):
        a,*b= map(str,input().split())
        inputs.append([a,b])

    for i in inputs:
        if i[0]=="append":
            arr.append(int(i[1][0]))
        elif i[0]=="insert":
            arr.insert(int(i[1][0]),int(i[1][1]))
        elif i[0]=="print":
            print(arr)
        elif i[0]=="remove":
            arr.remove(int(i[1][0]))
        elif i[0]=="sort":
            arr.sort()
        elif i[0]=="pop":
            arr.pop()
        elif i[0]=="reverse":
            arr=arr[::-1]
