from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    solved=False
    #a new line is created with every new 0
    #so someone infront of a 0 will have a value of 1, infront of 1 a value of 2 etc
    #so check counts of all elements in l and if the count of some value i is less than any value greater than it then it will not be possible
    #eg how can number of 2s be greater than number of 0's?
    #but first check the maximum in array given. that lets you know the macimum a line can reach
    # eg in 9 0 0 0 0 1 1 1 2 2 it has a length of nine but only a max of 2
    #so we need to ensure it has one's and zeros in it before even checking the count
    #if it does not have any element between its range then its not posible

    for i in range(max(l)):
        if i not in l:
            solved=True
            break

    if not solved:
        count=Counter(l)
        #sort the keys so you can loop through the elements after it
        #this way you do not have to loop through entire array and be doing i!=j as you know only ones ahead are greater than current
        vals=sorted(count.keys())

        for i in range(len(vals)):
            for j in range(i+1,len(vals)):
                #check count of current value < any other element greater than it
                #this means somebody dey lie
                if count[vals[i]]<count[vals[j]]:
                    solved=True
            if solved:
                break

    if solved:
        print("NO")
    else:
        print("YES")
        

    
