mass_table = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}


def get_cyclo_peptide_pattern(pattern: str, order):
    return pattern + pattern[0:order]


def get_mass_sum(pattern: str):
    mass_sum = 0
    for i in pattern:
        mass_sum += mass_table[i]
    return mass_sum


def get_cyclo_spectrum(pattern: str):
    cyclo_spectrum = [0, get_mass_sum(pattern)]

    for i in range(len(pattern) - 1):
        c_pattern = get_cyclo_peptide_pattern(pattern, i)
        for j in range(len(c_pattern) - i):
            cyclo_spectrum.append(get_mass_sum(c_pattern[j:j + i + 1]))

    cyclo_spectrum.sort()
    return cyclo_spectrum


def get_score(peptide: str, spectrum: list):
    score = 0
    for i in get_cyclo_spectrum(peptide):
        if i in spectrum:
            score += 1
            spectrum.remove(i)
    return score


def main():
    peptide = 'NQEL'
    str_spectrum = '0 99 113 114 128 227 257 299 355 356 370 371 484'
    spectrum = str_spectrum.split(' ')
    for i in range(0, len(spectrum)):
        spectrum[i] = int(spectrum[i])
    print(get_score(peptide, spectrum))


if __name__ == '__main__':
    main()