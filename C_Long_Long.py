t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    left=0
    right=0
    print("for a ",a)
    while right<len(a):

        while a[right]>0:

            right+=1
            left+=1
        while a[right]<=0:

            if right+1>=len(a) or a[right+1]>0:
                break            
            right+=1
        print("right and left after",right,left)

