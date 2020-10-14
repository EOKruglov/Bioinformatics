masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def get_cyclo_spectrum(linear_spectrum: list):
    cyclo_spectrum = [0, sum(linear_spectrum)]

    for i in range(len(linear_spectrum) - 1):
        c_pattern = linear_spectrum + linear_spectrum[0:i]
        for j in range(len(c_pattern) - i):
            cyclo_spectrum.append(sum(c_pattern[j:j + i + 1]))

    cyclo_spectrum.sort()
    return cyclo_spectrum


def get_linear_spectrum(peptide: list):
    linear_spectrum = [0, sum(peptide)]

    for i in range(len(peptide) - 1):
        for j in range(len(peptide) - i):
            linear_spectrum.append(sum(peptide[j:j + i + 1]))

    linear_spectrum.sort()
    return linear_spectrum


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


def is_consistent(peptide: list, spectrum: list):
    for i in peptide:
        if i in spectrum:
            spectrum.remove(i)
        else:
            return False
    return True


def cyclo_peptide_sequencing(spectrum: list):
    peptides = []
    for v in masses:
        if v in spectrum:
            peptides.append([v])

    while peptides:
        peptides = expand_peptides(peptides)
        peptides_buff = peptides.copy()
        for peptide in peptides_buff:
            if sum(peptide) == spectrum[-1]:
                if get_cyclo_spectrum(peptide) == spectrum:
                    print_spectrum(peptide)
                while peptide in peptides:
                    peptides.remove(peptide)
            elif not is_consistent(get_linear_spectrum(peptide), spectrum.copy()):
                while peptide in peptides:
                    peptides.remove(peptide)


if __name__ == '__main__':
    str_spectrum = '0 97 97 99 101 103 196 198 198 200 202 295 297 299 299 301 394 396 398 400 400 497'
    spectrum = str_spectrum.split(' ')
    for i in range(0, len(spectrum)):
        spectrum[i] = int(spectrum[i])
    cyclo_peptide_sequencing(spectrum)
