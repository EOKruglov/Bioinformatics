def form_profile(motifs, k):
    profile = [[0 for el in range(k)] for s in range(4)]
    buff_dct = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    t = 0
    for i, raw in enumerate(motifs):
        for j, el in enumerate(raw):
            profile[buff_dct[el]][j] += 1
        t = i + 1
    for i, raw in enumerate(profile):
        for j, el in enumerate(raw):
            profile[i][j] = el / t
    return profile


def find_most_probable_motif(dna_str, profile, k):
    profile_dict = {
        'A': profile[0],
        'C': profile[1],
        'G': profile[2],
        'T': profile[3]
    }
    probability = 0
    result = dna_str[:k]
    for i in range(len(dna_str) - k + 1):
        pattern = dna_str[i:i + k]
        buf_probability = 1
        for j, m in enumerate(pattern):
            buf_probability *= profile_dict[m][j]
        if buf_probability > probability:
            probability = buf_probability
            result = pattern
    return result


def get_count(motifs, k):
    profile = [[0 for el in range(k)] for s in range(4)]
    buff_dct = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    for raw in motifs:
        for j, el in enumerate(raw):
            profile[buff_dct[el]][j] += 1
    return profile


def get_score(motifs, k):
    count = get_count(motifs, k)
    score = 0
    for i in range(4):
        score += sum(count[i])
    for i in range(len(count[0])):
        score -= max([count[0][i], count[1][i], count[2][i], count[3][i]])
    return score


def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][0:k])
    for i in range(len(dna[0]) - k + 1):
        motif_0 = dna[0][i:i + k]
        motifs = [motif_0]
        for j in range(1, t):
            profile = form_profile(motifs, k)
            buf_motif = find_most_probable_motif(dna[j], profile, k)
            motifs.append(buf_motif)
        if get_score(motifs, k) < get_score(best_motifs, k):
            best_motifs = motifs
    return best_motifs


def main():
    k_t = input().split(' ')
    k = int(k_t[0])
    t = int(k_t[1])
    dna = []
    for i in range(t):
        dna.append(input())
    motifs = greedy_motif_search(dna, k, t)
    for i in motifs:
        print(i)


if __name__ == '__main__':
    main()
