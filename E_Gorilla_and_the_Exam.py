from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    freq = Counter(a)
    most_occuring=sorted(freq.items(),key=lambda item:item[1],reverse=True)
    new=[]
    for i in most_occuring:
        new.extend([i[0]]*i[1])

    # count=0
    
    # for i in range(len(a)-1,-1,-1):
    #     if count<k:
    #         if new[i]!=most_occuring[0][0]:
    #             new[i]=most_occuring[0][0]

    #             count+=1
    #     elif count>=k:
    #         break
    # print(len(set(new)))

   
    for i in range(1+k):

        new[-i]=most_occuring[0][0]

    print(len(set(new)))    



# from collections import Counter

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     freq = Counter(a)

#     most_occuring=sorted(freq.items(),key=lambda item:item[1])
    
#     for i in most_occuring:
#         if k>=i[1] and k!=0:
#             k-=i[1]
#             freq[i[0]]-=i[1]
#             if freq[i[0]]==0:
#                 del freq[i[0]]
        
#         else :
#             break
     
#     print(max(len(freq),1))

# from collections import Counter

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     freq = Counter(a)
#     # most_occuring=sorted(freq.items(),key=lambda item:item[1])
#     most_occuring=[key for key, count in freq.most_common()]
#     print(most_occuring)
#     for i in most_occuring:
#         if k>=freq[i] and k!=0:
#             k-=freq[i]
#             freq[i]-=freq[i]
#             if freq[i]==0:
#                 del freq[i]
        
#         else :
#             break
     
#     print(max(len(freq),1))

# from collections import Counter
# t = int(input())
# for _ in range(t):

#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))

#     freq = Counter(a)
#     freq_list = sorted(freq.values()) 

#     p = 0
#     while k > 0 and p < len(freq_list):
#         if k >= freq_list[p]:
#             k -= freq_list[p]
#             p += 1
#         else:
#             break

#     print(max(1,len(freq_list) - p))
# from collections import Counter
# t=int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = sorted(map(int, input().split()))
#     # we are to find minimum number of operations to make array empty. removing an element remove all its occ from arr
#     #without k answer is simply set(a).(give example also showing removing removes every instance of said value)
#     #  but with k operations i can manipulate input array which gives my f(a)
#     #change of one value at index of input counts as one operation
#     #populate most occuring with least occuring to help reduce num operations. and for this counter is used
#     freq=Counter(a)
#     print(freq)
#     freqs=list(freq.values())
#     print(freqs)
#     freqs.sort()
#     removed=0
#     #k always has to be greater than the value in the values list why?
#     #well if the count of some character is more than the remaining k it will not change number of 
#     # operations hence does not concern us
#     #at point where k is no longer greater than a value we can just break

#     while k > 0 and removed < len(freqs)-1:
#         if k >= freqs[removed]:
#             k -= freqs[removed]
#             removed += 1
#         else:
#             break
#     #so then our answer is num distinct- index we stopped which represents nuber of distinct characters that were replaced
# 	# Output is total_unique - removed.
#     print(len(freqs) - removed)            


