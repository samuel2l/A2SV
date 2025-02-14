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



             


a="acb"
b="acxb"
i=0
j=0
uncommon=[]
while i<len(a):
    if a[i]==b[j]:
        continue
    else:
        while a[i]!=b[j] and j<len(b):
            uncommon.append(b[j])
            j+=1

print("ei")
print(uncommon)            

   