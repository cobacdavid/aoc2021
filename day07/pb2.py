def main(fichier):
    with open(fichier) as fh:
        ma_liste = list(map(int, fh.readline().strip().split(',')))
        M, m = max(ma_liste), min(ma_liste)

        # position = m
        somme_min = float('inf')
        for p in range(m, M + 1):
            somme = 0
            for crabe in ma_liste:
                d = abs(crabe - p)
                somme += d * (d + 1) // 2
            if somme < somme_min:
                somme_min = somme
                # position = p

    return somme_min


print(main("jeu2.txt"))
