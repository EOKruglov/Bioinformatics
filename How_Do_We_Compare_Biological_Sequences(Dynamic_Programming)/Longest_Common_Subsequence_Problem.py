res = ''


def lcs_backtrack(v, w):
    s = [[0 for i in range(len(w))] for j in range(len(v))]
    backtrack = [[0 for i in range(len(w))] for j in range(len(v))]

    for i in range(len(v)):
        backtrack[i][0] = 'green'
    for i in range(len(w)):
        backtrack[0][i] = 'blue'

    for i in range(len(v)):
        for j in range(len(w)):
            if v[i] == w[j]:
                s[i][j] = max([s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + 1])
            else:
                s[i][j] = max([s[i - 1][j], s[i][j - 1]])
            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = 'green'
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = 'blue'
            elif s[i][j] == s[i - 1][j - 1] + 1 and v[i] == w[j]:
                backtrack[i][j] = 'red'
    return backtrack


def output_lcs(backtrack, v, i, j):
    if i == 0 and j == 0:
        return
    if backtrack[i][j] == 'green':
        output_lcs(backtrack, v, i - 1, j)
    elif backtrack[i][j] == 'blue':
        output_lcs(backtrack, v, i, j - 1)
    else:
        global res
        res += v[i]
        output_lcs(backtrack, v, i - 1, j - 1)


def main():
    w = '_' + input()
    v = '_' + input()
    backtrack = lcs_backtrack(v, w)
    output_lcs(backtrack, v, len(v) - 1, len(w) - 1)
    print(res[::-1])


if __name__ == "__main__":
    main()
