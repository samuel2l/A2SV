# q=int(input())
# queries=[]
# for _ in range(q):
#     s=input()
#     t=input()
#     p=input()
#     queries.append([s,t,p])
# for i in queries:
#     s,t,p=i
#     print(" S T P",s,t,p)
#     if s==t:
#         print("YES")

#     isSolved=False
#     for char in p:
#         print("P CHART",char)
#         for j in range(len(s)+1):
#             if j<len(s) and s[j] not in t:
#                 break
#             new= s[:j] + char + s[j:]
#             print("NEW ",new)

                
                

#             if new==t:
#                 print("YES")
#                 isSolved=True
#     if isSolved==False:
#         print("NO")



             


from collections import Counter


s="ab"
t="acxb"
p="cax"
isSolved=False
s_arr=[False for _ in range(len(s))]
t_arr=[]
p_arr=[]

if s==t:
    print("YES")
    isSolved=True
# if len(s)>len(t):
#     isSolved=False
#     print("NO")
s_arr=[False for _ in range(len(s))]
t_arr=[False for _ in range(len(t))]
p_arr=[]
t_count=Counter(t)
print("counter",t_count)
if s==t:
    print("YES")
    isSolved=True
# if len(s)>len(t):
#     isSolved=False
#     print("NO")
for idx in range(len(s)):
    temp=t
    if len(s)<len(t):
        if s[idx] in temp:
            if t_count[s[idx]]>0:
                t_count[s[idx]]-=1
                s_arr[idx]=True
print(s_arr)

not_in_s=[t[i] for i in range(len(s)) if s_arr[i]!=True]
print(not_in_s)