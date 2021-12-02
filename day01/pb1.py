with open("jeu2.txt") as fh:
    inc = 0
    data = int(fh.readline())
    for d in fh:
        # pour éviter inc += (d := int(d)) > data
        inc += 1 if (d := int(d)) > data else 0
        data = d

print(inc)
