with open("jeu2.txt") as fh:
    position = [0] * 2
    mvt = {"f": (0, 1), "u": (1, -1), "d": (1, 1)}
    for ligne in fh:
        instruction, count = ligne.strip().split()
        dpct = mvt[instruction[0]]
        position[dpct[0]] += int(count) * dpct[1]

print(position[0] * position[1])
