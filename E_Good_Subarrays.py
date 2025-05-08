from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    prefix_count = defaultdict(int)
    prefix_count[0] = 1 
    curr=0
    ans=0
    #sum of subarray=sum from subarray[left:right+1]
    #rewritten as:
    #sum from left to right = right -left +1
    #prefix[right]-prefix[left-1]=right-left+1
    #but to count subarrays we will only be using the right pointer so we rewrite equation to have the rights and constants on one side
    #using change of subject:
    #prefix[right] - right = prefix[left-1] - left+ 1

    for right in range(n):
        curr+=int(s[right])
        #prefix[right] is basically the current sum at the current index ie. curr
        formula_result=curr - right - 1
        ans+=prefix_count[formula_result]
        prefix_count[formula_result]+=1

    print(ans)