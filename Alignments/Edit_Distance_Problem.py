def get_distance(v, w):
    n = len(w)
    m = len(v)
    s = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        s[i][0] = i
    for j in range(m):
        s[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            f = 1
            if w[i] == v[j]:
                f = 0
            s[i][j] = min(
                [
                    s[i - 1][j] + 1,
                    s[i][j - 1] + 1,
                    s[i - 1][j - 1] + f
                ]
            )
    return s[n - 1][m - 1]


def main():
    v = '_' + input()
    w = '_' + input()
    print(get_distance(v, w))


if __name__ == '__main__':
    main()
