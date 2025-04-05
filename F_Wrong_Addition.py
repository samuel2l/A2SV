# n = int(input())
# for _ in range(n):
#     operand, res = map(int, input().split())
#     output_str = str(res)
#     input_str = str(operand)

#     i, j =  - 1,- 1
#     ans = ""
#     isPossible = True

#     while abs(j) <= len(input_str):
#         if abs(i) > len(output_str):
#             isPossible = False
#             break
#         if int(output_str[i]) - int(input_str[j])>=0:
#             ans = str(int(output_str[i]) - int(input_str[j])) + ans
#             i -= 1
#             j -= 1
#         else:
#             if abs(i - 1)>len(output_str) or int(output_str[i - 1]) == 0:
#                 isPossible = False
#                 break

#             num = int(output_str[i - 1]+output_str[i])
#             if num - int(input_str[j]) > 9:
#                 isPossible = False
#                 break
#             ans = str(num - int(input_str[j])) + ans
#             i -= 2
#             j -= 1


#     while abs(i) <= len(output_str):
#         ans = output_str[i] + ans
#         i -= 1

#     if isPossible and int(ans) >= 0:
#         print(int(ans))
#     else:
#         print(-1)

n=int(input())
for _ in range(n):
    operand,res=map(int,input().split())
    output_str=str(res)
    input_str=str(operand)
    maxi_length=max(len(output_str),len(input_str))
    if len(input_str)!=maxi_length:
        input_str= "0"*(len(output_str)-len(input_str)) + input_str
    i,j=-1,-1
    ans=""
    isPossible=True
    
    while abs(i)<=len(output_str) and abs(j)<=len(input_str):
        temp=int(output_str[i])-int(input_str[j])
        if temp>=0:
            if temp>9:
                isPossible=False
                print("-1")
                break

            else:
                ans= str(int(output_str[i])-int(input_str[j])) + ans
                i-=1
                j-=1
        else:
            if abs(i-1)>len(output_str) or output_str[i-1]=="0":
                print("-1")
                isPossible=False                
                break
            else:
                if int(output_str[i-1]+output_str[i])-int(input_str[j])>9 :
                    print("-1")
                    isPossible=False                
                    break                    
                ans= str(int(output_str[i-1]+output_str[i])-int(input_str[j])) + ans
                i-=2
                j-=1
        if abs(i)>len(output_str) and abs(j)<=len((str(operand))):
            print("-1")
            isPossible=False
            break

    if isPossible:print(int(ans))
