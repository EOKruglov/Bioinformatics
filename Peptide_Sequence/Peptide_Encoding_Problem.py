codon_table = {
    'AAA': 'K',
    'AAC': 'N',
    'AAG': 'K',
    'AAU': 'N',
    'ACA': 'T',
    'ACC': 'T',
    'ACG': 'T',
    'ACU': 'T',
    'AGA': 'R',
    'AGC': 'S',
    'AGG': 'R',
    'AGU': 'S',
    'AUA': 'I',
    'AUC': 'I',
    'AUG': 'M',
    'AUU': 'I',
    'CAA': 'Q',
    'CAC': 'H',
    'CAG': 'Q',
    'CAU': 'H',
    'CCA': 'P',
    'CCC': 'P',
    'CCG': 'P',
    'CCU': 'P',
    'CGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'CGU': 'R',
    'CUA': 'L',
    'CUC': 'L',
    'CUG': 'L',
    'CUU': 'L',
    'GAA': 'E',
    'GAC': 'D',
    'GAG': 'E',
    'GAU': 'D',
    'GCA': 'A',
    'GCC': 'A',
    'GCG': 'A',
    'GCU': 'A',
    'GGA': 'G',
    'GGC': 'G',
    'GGG': 'G',
    'GGU': 'G',
    'GUA': 'V',
    'GUC': 'V',
    'GUG': 'V',
    'GUU': 'V',
    'UAA': '',
    'UAC': 'Y',
    'UAG': '',
    'UAU': 'Y',
    'UCA': 'S',
    'UCC': 'S',
    'UCG': 'S',
    'UCU': 'S',
    'UGA': '',
    'UGC': 'C',
    'UGG': 'W',
    'UGU': 'C',
    'UUA': 'L',
    'UUC': 'F',
    'UUG': 'L',
    'UUU': 'F'
}

reverse_pattern_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}


def get_reverse_complement(pattern: str):
    reverse_pattern = ''
    for i in pattern[::-1]:
        reverse_pattern += reverse_pattern_map[i]
    return reverse_pattern


def get_encode_peptides(dna_pattern: str, peptide_pattern: str, is_reverse: bool = False):
    rna_pattern = dna_pattern.replace('T', 'U')
    encode_peptides = []
    for i in range(len(rna_pattern) - 3 * len(peptide_pattern) + 1):
        encode_peptide = ''
        for j in range(len(peptide_pattern)):
            curr = rna_pattern[i + j * 3:i + 3 + j * 3]
            curr_peptide = codon_table[curr]
            if curr_peptide == peptide_pattern[j]:
                encode_peptide += curr
            else:
                break
        if len(encode_peptide) == len(peptide_pattern) * 3:
            encode_peptide = encode_peptide.replace('U', 'T')
            if is_reverse:
                encode_peptide = get_reverse_complement(encode_peptide)
            encode_peptides.append(encode_peptide)
    return encode_peptides


def main():
    dna_pattern = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
    peptide_pattern = "MA"
    encode_peptides = get_encode_peptides(dna_pattern, peptide_pattern)
    reverse_encode_peptides = get_encode_peptides(get_reverse_complement(dna_pattern), peptide_pattern, is_reverse=True)
    for i in encode_peptides + reverse_encode_peptides:
        print(i)


if __name__ == '__main__':
    main()
