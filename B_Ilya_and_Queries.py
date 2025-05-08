from itertools import accumulate

s = input()
m = int(input())

prefix = [0] * (len(s))  

for i in range(1,len(s)):
    if s[i] == s[i-1]: 
        prefix[i] = 1
print(prefix)
prefix = list(accumulate(prefix))

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix[end-1] - prefix[start-1])