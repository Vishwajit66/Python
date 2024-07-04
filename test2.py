for i in range(1, 6):
    for j in range(1, 6):
        if j <= i:
            print(i, end=" ")
        else:
            print(j, end=" ")
    print()