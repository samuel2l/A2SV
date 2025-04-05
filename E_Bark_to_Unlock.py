n = input()
l = int(input())
words = [input() for _ in range(l)]
solved = False

if n in words:
    print("YES")
    solved = True

if not solved:
    for i in words:
        for j in words:
            if (i + j).find(n) != -1:
                print("YES")
                solved = True
                break
        if solved:
            break

if not solved:
    print("NO")