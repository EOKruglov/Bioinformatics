def main():
    dna = input()
    k = int(input())
    profile_a = input().split(' ')
    profile_c = input().split(' ')
    profile_g = input().split(' ')
    profile_t = input().split(' ')

    for i in range(k):
        profile_a[i] = float(profile_a[i])
        profile_c[i] = float(profile_c[i])
        profile_g[i] = float(profile_g[i])
        profile_t[i] = float(profile_t[i])

    profile_dict = {
        'A': profile_a,
        'C': profile_c,
        'G': profile_g,
        'T': profile_t
    }
    result = ''
    probability = 0

    for i in range(len(dna) - k + 1):
        pattern = dna[i:i + k]
        buf_probability = 1
        for j, m in enumerate(pattern):
            buf_probability *= profile_dict[m][j]
        if buf_probability > probability:
            probability = buf_probability
            result = pattern
    print(result)


if __name__ == '__main__':
    main()
