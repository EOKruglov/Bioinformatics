from itertools import product


def get_all_k_mers_list(k):
    lst = ['A', 'C', 'G', 'T']
    return list(product(lst, repeat=k))


def get_all_k_mers_differing_list(k_mer, all_k_mers_list, d):
    diff_list = [k_mer]
    for item in all_k_mers_list:
        count = 0
        for i in range(len(k_mer)):
            if k_mer[i] != item[i]:
                count += 1
        if count <= d:
            diff_list.append(item)
    return diff_list


def is_pattern_appears(dna, all_k_mers_list, pattern, k, d):
    string_num = len(dna)
    count = 0
    for dna_string in dna:
        for i in range(len(dna_string) - k + 1):
            if tuple(dna_string[i: i + k]) in get_all_k_mers_differing_list(pattern, all_k_mers_list, d):
                count += 1
                break
    return string_num == count


def motif_enumeration(dna, k, d):
    patterns = []
    all_k_mers_list = get_all_k_mers_list(k)
    for k_mer in all_k_mers_list:
        if is_pattern_appears(dna, all_k_mers_list, k_mer, k, d):
            patterns.append(k_mer)
    return patterns


def main():
    k = 4
    d = 1
    dna = ['CACTGATCGACTTATC', 'CTCCGACTTACCCCAC', 'GTCTATCCCTGATGGC', 'CAGGGTTGTCTTGTCT']
    motifs = motif_enumeration(dna, k, d)
    result = []
    for motif in motifs:
        res = ''
        for i in motif:
            res += i
        result.append(res)
    print(' '.join(result))


if __name__ == '__main__':
    main()
