# k=int(input())
# seqs=[]
# for _ in range(k):
#     n=int(input())
#     inp=list(map(int,input().split()))
#     seqs.append(inp)
# solved=False
# for seq in range(len(seqs)):
#     if solved==False:
#         for j in range(1,len(seqs[seq])):
#             # print("the slice selected",seqs[seq][j:])
#             test=sum(seqs[seq][j:])
#             if j+1 < len(seqs[seq]):
#                 test=sum(seqs[seq][:j]) + sum(seqs[seq][j+1:])
#             else:
#                 test=sum(seqs[seq][:len(seqs[seq])])
#             # print("sum",test)
#             if solved==False:

#                 for k in range(seq+1,len(seqs)):
#                     if solved==False:
#                         for p in range(1,len(seqs[k])):
#                             # print("slice in second check",seqs[k][p:])
                            
#                             match=sum(seqs[k][p:])
#                             if k+1 < len(seqs[k]):
#                                 match=sum(seqs[k][:p]) + sum(seqs[k][p+1:])
#                             else:
#                                 match=sum(seqs[seq][:len(seqs[k])])
#                             # print("match",match)
#                             if match==test:
#                                 solved=True
#                                 print("YES")
#                                 print(seq+1,j+1)
#                                 print(k+1,p)
                                
#                                 break

# if solved==False:
#     print("NO")



        

k=int(input())
seqs=[]
for _ in range(k):
    n=int(input())
    inp=list(map(int,input().split()))
    seqs.append(inp)

solved=False
ans={}
for index in range(len(seqs)):
    seq_sum=sum(seqs[index])

    if not solved:
        for element in range(len(seqs[index])):
                curr_seq=seqs[index]
                sum_without_index=seq_sum-curr_seq[element]
                                    
                if sum_without_index not in ans :
                                            #seq,idx removed
                    ans[sum_without_index]=(index+1,element+1)
                else:
                     if ans[sum_without_index][0]!=index+1:
                        print("YES")
                        print(index+1,element+1)
                        print(ans[sum_without_index][0],ans[sum_without_index][1])
                        
                        solved=True
                        break


if not solved:
    print("NO")
