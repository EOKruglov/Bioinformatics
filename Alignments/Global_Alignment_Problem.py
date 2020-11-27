res = ''

scoring_matrix = [
    [4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
    [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
    [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
    [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
    [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
    [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
    [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
    [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
    [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
    [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
    [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
    [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
    [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
    [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
    [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
    [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
    [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
    [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
    [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
    [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]
]

buff_dict = {
    'A': 0,
    'C': 1,
    'D': 2,
    'E': 3,
    'F': 4,
    'G': 5,
    'H': 6,
    'I': 7,
    'K': 8,
    'L': 9,
    'M': 10,
    'N': 11,
    'P': 12,
    'Q': 13,
    'R': 14,
    'S': 15,
    'T': 16,
    'V': 17,
    'W': 18,
    'Y': 19
}


def lcs_backtrack(v, w):
    sigma = 5
    m = len(v) + 1
    n = len(w) + 1
    backtrack = [[0 for x in range(m)] for y in range(n)]
    s = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        s[i][0] = -sigma * i
        backtrack[i][0] = 'green'
    for j in range(m):
        s[0][j] = -sigma * j
        backtrack[0][j] = 'blue'
    for i in range(1, len(w) + 1):
        for j in range(1, len(v) + 1):
            f = scoring_matrix[buff_dict[v[j - 1]]][buff_dict[w[i - 1]]]
            s[i][j] = max(s[i - 1][j] - sigma, s[i][j - 1] - sigma, s[i - 1][j - 1] + f)
            if s[i][j] == s[i - 1][j] - sigma:
                backtrack[i][j] = 'green'
            if s[i][j] == s[i][j - 1] - sigma:
                backtrack[i][j] = 'blue'
            if s[i][j] == s[i - 1][j - 1] + f:
                backtrack[i][j] = 'red'
    return backtrack, s[n - 1][m - 1]


def output_align(backtrack, v, w, j, i):
    ans1 = ""
    ans2 = ""
    while i != 0 or j != 0:
        if backtrack[i][j] == 'green':
            ans1 = ans1 + '-'
            ans2 = ans2 + str(w[i-1])
            i -= 1
        elif backtrack[i][j] == 'blue':
            ans1 = ans1 + str(v[j-1])
            ans2 = ans2 + str('-')
            j -= 1
        else:
            ans1 = ans1 + str(v[j-1])
            ans2 = ans2 + str(w[i-1])
            i -= 1
            j -= 1
    return ans1, ans2


def main():
    v = input()
    w = input()
    backtrack, s = lcs_backtrack(v, w)
    res_1, res_2 = output_align(backtrack, v, w, len(v), len(w))
    print(s)
    print(res_1[::-1])
    print(res_2[::-1])


if __name__ == '__main__':
    main()
