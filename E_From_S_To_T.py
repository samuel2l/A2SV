from collections import Counter

def is_subseq(s,p):
    i,j=0,0
    while i<len(s) and j<len(p):
        if s[i]==p[j]:
            i+=1
        j+=1
    return i==len(s)

q=int(input())
for _ in range(q):
    s=input()
    t=input()
    p=input()

    count_s=Counter(s)
    count_t=Counter(t)
    count_p=Counter(p)
    isValid=True
    if not is_subseq(s,t):
        print("NO")
        continue

    for i in t:
        if count_t[i]> count_s[i]+count_p[i]:
            isValid=False
    if isValid:
        print("YES")
    else:
        print("NO")






             

