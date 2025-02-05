if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores=list(arr)
    largest=max(scores)
    non_max=[score for score in scores if score!=largest]
    print(max(non_max))
