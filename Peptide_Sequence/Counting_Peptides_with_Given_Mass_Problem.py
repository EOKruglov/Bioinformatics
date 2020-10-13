m = int(input())
count = dict()
count[0] = 1
masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
for i in range(57, m + 1):
    count[i] = 0
    for j in range(0, len(masses)):
        if i - masses[j] in count:
            count[i] = count[i - masses[j]] + count[i]
print(count[m])
