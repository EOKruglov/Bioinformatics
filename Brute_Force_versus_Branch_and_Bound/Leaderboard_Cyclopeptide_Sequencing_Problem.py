masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def get_linear_spectrum(peptide: list):
    linear_spectrum = [0, sum(peptide)]

    for i in range(len(peptide) - 1):
        for j in range(len(peptide) - i):
            linear_spectrum.append(sum(peptide[j:j + i + 1]))

    linear_spectrum.sort()
    return linear_spectrum


def get_linear_score(peptide: list, spectrum: list):
    score = 0
    for i in get_linear_spectrum(peptide):
        if i in spectrum:
            score += 1
            spectrum.remove(i)
    return score


def expand(peptides: list):
    new_peptides = []
    for v in masses:
        for i in range(0, len(peptides)):
            new_peptides.append(peptides[i] + [v])
    return new_peptides


def trim(leader_board: list, spectrum: list, n: int):
    if len(leader_board) < n:
        return leader_board
    score_list = []
    new_leader_board = []
    for peptide in leader_board:
        score_list.append(get_linear_score(peptide, spectrum.copy()))
    score_map = list(zip(score_list, leader_board))
    score_map.sort(key=lambda x: x[0], reverse=True)
    max_score = score_map[0][0]
    for score, peptide_value in score_map:
        if score == max_score:
            new_leader_board.append(peptide_value)
    return new_leader_board


def print_peptide(spectrum: list):
    for i in range(0, len(spectrum)):
        spectrum[i] = str(spectrum[i])
    print('-'.join(spectrum))


def leaderboard_cyclopeptide_sequencing(spectrum: list, n: int):
    leader_peptide = []
    leader_board = [leader_peptide]
    while leader_board:
        leader_board = expand(leader_board)
        for peptide in leader_board.copy():
            if sum(peptide) == spectrum[-1]:
                if get_linear_score(peptide, spectrum.copy()) > get_linear_score(leader_peptide, spectrum.copy()):
                    leader_peptide = peptide
            elif sum(peptide) > spectrum[-1]:
                leader_board.remove(peptide)
        leader_board = trim(leader_board, spectrum, n)
    print_peptide(leader_peptide)


def main():
    n = 9
    str_spectrum = '0 71 101 103 113 114 128 131 156 156 172 199 232 242 259 269 270 287 300 303 313 372 372 373 388 ' \
                   '398 400 414 431 459 469 486 501 501 503 528 545 570 572 572 587 604 614 642 659 673 675 685 700 ' \
                   '701 701 760 770 773 786 803 804 814 831 841 857 874 901 917 917 942 945 959 960 970 972 1002 1073'
    spectrum = str_spectrum.split(' ')
    for i in range(0, len(spectrum)):
        spectrum[i] = int(spectrum[i])
    leaderboard_cyclopeptide_sequencing(spectrum, n)


if __name__ == '__main__':
    main()
