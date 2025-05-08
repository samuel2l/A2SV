from itertools import accumulate
n=int(input())
t=list(map(int,input().split()))

bob=0
alice=0
alice_count=0
bob_count=0

alice_prefix=list(accumulate(t))
bob_prefix=list(accumulate(t[::-1]))

while alice_count+bob_count < n:
    if alice_prefix[alice] <= bob_prefix[bob]:
        alice+=1
        alice_count+=1
    elif alice_prefix[alice]> bob_prefix[bob]:
        bob+=1
        bob_count+=1


print(alice_count,bob_count)
