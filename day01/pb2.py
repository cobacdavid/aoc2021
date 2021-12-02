with open("jeu2.txt") as fh:
    fenetre, inc = [], 0
    for _ in range(3):
        fenetre.append(int(fh.readline()))
    data = sum(fenetre)
    for d in fh:
        fenetre = fenetre[1:] + [int(d)]
        inc += 1 if sum(fenetre) > data else 0
        data = sum(fenetre)

print(inc)
