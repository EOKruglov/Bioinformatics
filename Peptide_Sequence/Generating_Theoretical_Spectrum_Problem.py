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


# peptide_pattern = "LEQN" LEQNLE

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


def main():
    peptide_pattern = 'LEQN'
    cyclo_spectrum = get_cyclo_spectrum(peptide_pattern)
    for i in cyclo_spectrum:
        print(i)


if __name__ == "__main__":
    main()


