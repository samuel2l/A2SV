n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    lucky = float("-inf")
    for i in range(r, l - 1, -1):
        luck = int(max(str(i))) - int(min(str(i)))        
        if luck > lucky:
            lucky = luck
            best_num = i
        if luck == 9:
            break
    print(best_num)