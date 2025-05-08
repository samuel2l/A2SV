# n=int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# good_pairs=0
# # visited=set()
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]+a[j] > b[i]+b[j] and  i!=j:
#             # print(a[i],a[j])
#             good_pairs+=1
#             # visited.add((j,i))
#             # visited.add((i,j))
            
# print(good_pairs//2)

# n=int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# good_pairs=0
# # visited=set()
# # for i in range(len(a)):
# #     for j in range(i+1,len(b)):
# #         if a[i]+a[j] > b[i]+b[j]:
# #             good_pairs+=1
# left=0
# right=1
# while left<len(a)-1:
#     while right<len(a):
#         if a[left]+a[right] > b[left]+b[right]:
#             good_pairs+=1
#         right+=1
#     left+=1
#     right=left+1

# print(good_pairs)

#this would have worked if they were together you try
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# window_size=len(a)-2

# left=0
# right=window_size
# window_sum_a=sum(a[:window_size])
# window_sum_b=sum(b[:window_size])
# print("initial window sum",window_sum_a,window_sum_b)
# sum_a=sum(a)
# sum_b=sum(b)
# good_pairs=0
# # right+=1
# while left<len(a)-1:
#     window_sum_a=window_sum_a-a[left]+a[right]
#     window_sum_b=window_sum_b-b[left]+b[right]
#     print(left,right,"new win sum",window_sum_a,window_sum_b)
#     if sum_a-window_sum_a > sum_b-window_sum_b:
#         good_pairs+=1


#     left+=1
#     right+=1
#     right%=len(a)
# print(good_pairs)
