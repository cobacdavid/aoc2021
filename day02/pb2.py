with open("jeu2.txt") as fh:
    h_a_d = [0] * 3
    mvt = {"f": (0, 1), "u": (1, -1), "d": (1, 1)}
    for ligne in fh:
        instruction, count = ligne.strip().split()
        lettre = instruction[0]
        dpct = mvt[lettre]
        h_a_d[dpct[0]] += int(count) * dpct[1]
        if lettre == "f":
            h_a_d[2] += h_a_d[1] * int(count)

print(h_a_d[0] * h_a_d[2])
