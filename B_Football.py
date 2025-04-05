n=input()
cnt=0
solved=False
if len(n)<7:
    print("NO")
elif len(n)==7 and (n=="0000000" or n=="1111111"):
    print("YES")
else:
    for i in range((len(n)-7)+1):
        if n[i:i+7]=="0000000" or n[i:i+7]=="1111111":

            print("YES")
            solved=True
            break

    if solved==False:
        print("NO")

