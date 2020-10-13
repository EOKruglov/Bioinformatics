masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def get_cyclo_spectrum(linear_spectrum: list):
    cyclo_spectrum = [0, sum(linear_spectrum)]

    for i in range(len(linear_spectrum) - 1):
        c_pattern = linear_spectrum + linear_spectrum[0:i]
        for j in range(len(c_pattern) - i):
            cyclo_spectrum.append(sum(c_pattern[j:j + i + 1]))

    cyclo_spectrum.sort()
    return cyclo_spectrum


def expand_peptides(peptides: list):
    new_peptides = []
    for v in masses:
        for i in range(0, len(peptides)):
            new_peptides.append(peptides[i] + [v])
    return new_peptides


def print_spectrum(spectrum: list):
    for i in range(0, len(spectrum)):
        spectrum[i] = str(spectrum[i])
    print('-'.join(spectrum))


def cyclo_peptide_sequencing(spectrum: list):
    peptides = []
    for v in spectrum:
        if v in masses:
            peptides.append([v])

    while peptides:
        peptides_buff = []
        peptides = expand_peptides(peptides)
        for peptide in peptides:
            if sum(peptide) in spectrum:
                if get_cyclo_spectrum(peptide) == spectrum:
                    print_spectrum(peptide)
                else:
                    peptides_buff.append(peptide)
        peptides = peptides_buff


if __name__ == '__main__':
    str_spectrum = '0 113 128 186 241 299 314 427'
    spectrum = str_spectrum.split(' ')
    for i in range(0, len(spectrum)):
        spectrum[i] = int(spectrum[i])
    cyclo_peptide_sequencing(spectrum)
