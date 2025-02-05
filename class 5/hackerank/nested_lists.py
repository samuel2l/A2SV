if __name__ == '__main__':
    arr=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        scores.append(score)
    second_lowest=[i for i in scores if i!=min(scores)]
    lowest=[i[0] for i in arr if i[1]==min(second_lowest)]
    lowest.sort()
    [print(i) for i in lowest]
        
        