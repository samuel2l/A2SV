for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    mini=1
    maxi=n
    left=0
    right=n-1
    solved=False

    
    while left<right:
        if arr[left]==mini:
            left+=1
            mini+=1

        elif arr[right]==maxi:
            right-=1
            maxi-=1

        elif arr[left]==maxi:
            left+=1
            maxi-=1

        elif arr[right]==mini:
            right-=1
            mini+=1

        else:
            print(left+1,right+1)
            solved = True
            break

    if not solved:
        print(-1)