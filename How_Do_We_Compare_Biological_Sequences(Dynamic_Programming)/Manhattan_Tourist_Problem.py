def manhattan_tourist(n, m, down, right):
    s = [[0 for i in range(m)] for j in range(n)]
    for i in range(1, n):
        s[i][0] = s[i - 1][0] + down[i][0]

    for j in range(1, m):
        s[0][j] = s[0][j - 1] + right[0][j]

    for i in range(1, n):
        for j in range(1, m):
            s[i][j] = max([s[i - 1][j] + down[i][j], s[i][j - 1] + right[i][j]])
    return s[n - 1][m - 1]


def main():
    n_m = input().split(' ')
    n = int(n_m[0])
    m = int(n_m[1])

    down = []
    right = []

    for i in range(n):
        down_raw = input().split(' ')
        for k, v in enumerate(down_raw):
            down_raw[k] = int(v)
        down.append(down_raw)

    delim = input()

    for i in range(n + 1):
        right_raw = input().split(' ')
        for k, v in enumerate(right_raw):
            right_raw[k] = int(v)
        right.append(right_raw)
    print(manhattan_tourist(n, m, down, right))


if __name__ == '__main__':
    main()
