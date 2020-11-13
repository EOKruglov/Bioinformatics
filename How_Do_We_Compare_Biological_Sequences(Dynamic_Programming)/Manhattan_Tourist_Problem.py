def manhattan_tourist(n, m, down, right):
    s = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n):
        s[i + 1][0] = s[i][0] + down[i][0]

    for j in range(m):
        s[0][j + 1] = s[0][j] + right[0][j]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max([s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1]])
    return s[n][m]


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
