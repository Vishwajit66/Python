cases = int(input())
a = 0
t = []

for k in range(cases):
    row, col = map(int, input().split())
    t.append([row, col])
    a += row + 1

for k in range(cases):
    l = t[k][0] 
    c = t[k][1] 

    for i in range(l):
        for j in range(c):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                print("*", end="")
            else:
                print(".", end="")
        print()
    print()