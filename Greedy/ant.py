def search(m, x, y):
    m[x][y] = 9
    while x < len(m) and y < (len(m[0])-1):
        if m[x][y] == 2:
            m[x][y] = 9
            break
        elif m[x][y + 1] == 0:
            m[x][y] = 9
            y += 1
        elif m[x][y + 1] == 1:
            m[x][y] = 9
            if m[x + 1][y] == 0:
                x += 1
            elif m[x + 1][y] == 1:
                break
            elif m[x+1][y]== 2:
                x += 1
        for i in range(len(m)):
            print(m[i])
    return m


m = [[0] * 11 for _ in range(11)]
ans = [[0] * 10 for _ in range(10)]
for i in range(1, len(m)):
    # 1 0+list
    a = [0] + list(map(int, input().split()))
    m[i] = a
search(m, 2, 2)
for i in range(1, len(m)):
    for j in range(1, len(m[0])):
        ans[i - 1][j - 1] = m[i][j]
for i in range(len(ans)):
    print(ans[i])