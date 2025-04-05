n = int(input())
presents = list(map(int, input().split()))

arr = [0 for _ in range(n)] 

for i in range(n):
    arr[presents[i] - 1] = i + 1
# ans=""
# for i in arr:
#     ans=ans+str(i)+" "
# print(ans)
print(*arr)
