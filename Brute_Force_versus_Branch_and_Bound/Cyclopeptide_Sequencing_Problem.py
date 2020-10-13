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


def expand_peptides(peptides: list):
    new_peptides = []
    for key in mass_table.keys():
        for i in range(0, len(peptides)):
            new_peptides.append(peptides[i] + key)
    return new_peptides


def spectrum_from_peptide(peptide: str):
    spectrum = []
    for i in peptide:
        spectrum.append(str(mass_table[i]))
    return spectrum


def cyclo_peptide_sequencing(spectrum: list):
    peptides = []
    output = []
    for item in mass_table.items():
        if item[1] in spectrum:
            peptides.append(item[0])

    while peptides:
        peptides_buff = []
        peptides = expand_peptides(peptides)
        for peptide in peptides:
            if get_mass_sum(peptide) in spectrum:
                if get_cyclo_spectrum(peptide) == spectrum:
                    if spectrum_from_peptide(peptide) not in output:
                        output.append(spectrum_from_peptide(peptide))
                else:
                    peptides_buff.append(peptide)
        peptides = peptides_buff.copy()
    for i in output:
        print('-'.join(i))


if __name__ == '__main__':
    str_spectrum = input()
    spectrum = str_spectrum.split(' ')
    for i in range(0, len(spectrum)):
        spectrum[i] = int(spectrum[i])
    cyclo_peptide_sequencing(spectrum)
