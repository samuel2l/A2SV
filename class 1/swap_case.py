def swap_case(s):
    g=''    
    for i in s:
        if i==i.lower():
            g+=i.upper()
        elif i==i.upper():
            g+=i.lower()
    return g
            
            

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)