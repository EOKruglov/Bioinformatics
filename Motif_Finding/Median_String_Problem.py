from itertools import product


def get_all_k_mers_list(k):
    lst = ['A', 'C', 'G', 'T']
    return list(product(lst, repeat=k))


def hamming_distance(pattern, dna):
    distance = 0
    k = len(pattern)
    for dna_string in dna:
        minimum = 2**64
        for i in range(len(dna_string) - k + 1):
            buff_dna = dna_string[i:i + k]
            buff = 0
            for j in range(len(buff_dna)):
                if dna_string[j] != pattern[j]:
                    buff += 1
            if buff < minimum:
                minimum = buff
        distance += minimum
    return distance


def median_string(dna, k):
    distance = 2 ** 64
    median = tuple()
    for k_mer in get_all_k_mers_list(k):
        d = hamming_distance(k_mer, dna)
        if distance > d:
            distance = d
            median = k_mer
    return median


def main():
    k = 5
    dna = ['GAAACTACGCACGTAGTGTTTTGCTACGGTTCTCA', 'TATATCCACATGACCTCGACAACGCACGGTCGAAT',
           'TAGCGGGACAATCAGGTCTGAGTCGACTGTTGTGC', 'TCCTGCCGGTTGCTAACTGTAGACGTTTACCCCTT',
           'TCCCTCCCTAACTCTAGGCTACTGTCGTCCGCAGT', 'AGGCAGAAAGACAACGGTAGTAATCTAGAGACCGT',
           'CGCTCCACGCAGCTCATAGAACCGTGTTGTTCAAC', 'ACTGTCTCCCGGAAACCATAAACTACTTGGTTTGT',
           'GGTTTTCTTGACTGTAATTACAATCCAGGAGACCA', 'ATGTCGCTCTACAGTGAACACGTAACTGTCTTCGG']
    median = median_string(dna, k)
    res = ''
    for i in median:
        res += i
    print(res)


if __name__ == '__main__':
    main()
