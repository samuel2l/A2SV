s=int(input())

t=str(s)
ansint=s
ans=''
solved=False
while solved!=True:
    ansint+=1
    if len(str(ansint))==len(set(str(ansint))):
        solved=True
print(ansint)
