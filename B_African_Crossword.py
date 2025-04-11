m,n=map(int,input().split())
table=[]

for _ in range(m):
    row=list(map(str,input().split()))
    table.append(list(row[0]))

rows=len(table)
cols=len(table[0])
#create arr to track cancelled letters
cancelled=[[False]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        curr=table[i][j]
        found_col_duplicate=False
        found_row_duplicate=False
        #check columns after current column and mark them as cancelled
        for col in range(j+1,cols):            
            if table[i][col]==curr:
                found_col_duplicate=True
                cancelled[i][col]=True

        if found_col_duplicate:
            cancelled[i][j]=True

        #check rows after current row and mark them as cancelled
        for row in range(i+1,rows):            
            if table[row][j]==curr:
                found_row_duplicate=True
                cancelled[row][j]=True

        if found_row_duplicate:
            cancelled[i][j]=True

ans=""
#add unmarked cells to the final answer
for i in range(rows):
    for j in range(cols):
        if not cancelled[i][j]:
            ans+=table[i][j]
print(ans)
