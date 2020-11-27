scoring_matrix = [
    [2, -2, 0, 0, -3, 1, -1, -1, -1, -2, -1, 0, 1, 0, -2, 1, 1, 0, -6, -3],
    [-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4, 0, -2, -2, -8, 0],
    [0, -5, 4, 3, -6, 1, 1, -2, 0, -4, -3, 2, -1, 2, -1, 0, 0, -2, -7, -4],
    [0, -5, 3, 4, -5, 0, 1, -2, 0, -3, -2, 1, -1, 2, -1, 0, 0, -2, -7, -4],
    [-3, -4, -6, -5, 9, -5, -2, 1, -5, 2, 0, -3, -5, -5, -4, -3, -3, -1, 0, 7],
    [1, -3, 1, 0, -5, 5, -2, -3, -2, -4, -3, 0, 0, -1, -3, 1, 0, -1, -7, -5],
    [-1, -3, 1, 1, -2, -2, 6, -2, 0, -2, -2, 2, 0, 3, 2, -1, -1, -2, -3, 0],
    [-1, -2, -2, -2, 1, -3, -2, 5, -2, 2, 2, -2, -2, -2, -2, -1, 0, 4, -5, -1],
    [-1, -5, 0, 0, -5, -2, 0, -2, 5, -3, 0, 1, -1, 1, 3, 0, 0, -2, -3, -4],
    [-2, -6, -4, -3, 2, -4, -2, 2, -3, 6, 4, -3, -3, -2, -3, -3, -2, 2, -2, -1],
    [-1, -5, -3, -2, 0, -3, -2, 2, 0, 4, 6, -2, -2, -1, 0, -2, -1, 2, -4, -2],
    [0, -4, 2, 1, -3, 0, 2, -2, 1, -3, -2, 2, 0, 1, 0, 1, 0, -2, -4, -2],
    [1, -3, -1, -1, -5, 0, 0, -2, -1, -3, -2, 0, 6, 0, 0, 1, 0, -1, -6, -5],
    [0, -5, 2, 2, -5, -1, 3, -2, 1, -2, -1, 1, 0, 4, 1, -1, -1, -2, -5, -4],
    [-2, -4, -1, -1, -4, -3, 2, -2, 3, -3, 0, 0, 0, 1, 6, 0, -1, -2, 2, -4],
    [1, 0, 0, 0, -3, 1, -1, -1, 0, -3, -2, 1, 1, -1, 0, 2, 1, -1, -2, -3],
    [1, -2, 0, 0, -3, 0, -1, 0, 0, -2, -1, 0, 0, -1, -1, 1, 3, 0, -5, -3],
    [0, -2, -2, -2, -1, -1, -2, 4, -2, 2, 2, -2, -1, -2, -2, -1, 0, 4, -6, -2],
    [-6, -8, -7, -7, 0, -7, -3, -5, -3, -2, -4, -4, -6, -5, 2, -2, -5, -6, 17, 0],
    [-3, 0, -4, -4, 7, -5, 0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2, 0, 10]
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
            s[i][j] = max(0, s[i - 1][j] - sigma, s[i][j - 1] - sigma, s[i - 1][j - 1] + f)
            if s[i][j] == s[i - 1][j] - sigma:
                backtrack[i][j] = 'green'
            if s[i][j] == s[i][j - 1] - sigma:
                backtrack[i][j] = 'blue'
            if s[i][j] == s[i - 1][j - 1] + f:
                backtrack[i][j] = 'red'
            if s[i][j] == 0:
                backtrack[i][j] = 'black'

    max_s = 0
    max_i = 0
    max_j = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] > max_s:
                max_i = i
                max_j = j
                max_s = s[i][j]
    return backtrack, max_s, max_i, max_j


def output_align(backtrack, v, w, j, i):
    ans1 = ""
    ans2 = ""
    while i != 0 or j != 0:
        if backtrack[i][j] == 'black':
            break
        elif backtrack[i][j] == 'green':
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
    backtrack, s, max_i, max_j = lcs_backtrack(v, w)
    res_1, res_2 = output_align(backtrack, v, w, max_j, max_i)
    print(s)
    print(res_1[::-1])
    print(res_2[::-1])


if __name__ == '__main__':
    main()
