s= input()
eles=[]
for i in s:
    if i!='+':
        eles.append(i)
eles.sort()
correct=''
for i in range(len(eles)):
    if i==len(eles)-1:
        correct+=f'{eles[i]}'

    else:
        correct+=f'{eles[i]}+'

print(correct)

