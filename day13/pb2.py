def fold_x(t, x):
    # t: ligne, colonne
    # x: colonne
    return (t[0], 2 * x - t[1])


def fold_y(t, y):
    # t: ligne, colonne
    # y: ligne
    return (2 * y - t[0], t[1])


def marque_c(t, matrice, axc):
    init = matrice[t[0]][t[1]]
    a, b = fold_x(t, axc)
    if a >= len(matrice) or b >= len(matrice[0]):
        reponse = False
    else:
        reponse = matrice[a][b]
    matrice[t[0]][t[1]] = init or reponse


def marque_l(t, matrice, axl):
    init = matrice[t[0]][t[1]]
    a, b = fold_y(t, axl)
    if a >= len(matrice) or b >= len(matrice[0]):
        reponse = False
    else:
        reponse = matrice[a][b]
    matrice[t[0]][t[1]] = init or reponse


def ajoute_lignes(matrice, numero_ligne):
    l = len(matrice)
    c = len(matrice[0])

    for _ in range(numero_ligne - l + 1):
        matrice.append([False] * c)


def ajoute_colonnes(matrice, numero_colonne):
    l = len(matrice)
    c = len(matrice[0])

    for m in matrice:
        m += [False] * (numero_colonne - c + 1)


def parcours_matrice(matrice, max_l, max_c, sens):
    for l in range(max_l):
        for c in range(max_c):
            if sens == "y":
                marque_l((l, c), matrice, max_l)
            else:
                marque_c((l, c), matrice, max_c)


def main(fichier):
    matrice = [[]]
    with open(fichier) as fh:
        while (ligne := fh.readline().strip()) != "":
            c, l = list(map(int, ligne.strip().split(',')))
            ajoute_colonnes(matrice, c)
            ajoute_lignes(matrice, l)
            matrice[l][c] = True

        Ml, Mc = len(matrice), len(matrice[0])
        for ligne in fh:
            ligne = ligne.strip()
            if ligne == "": continue
            paire = ligne.split()[-1].split('=')
            if paire[0] == "x":
                Mc = int(paire[1])
                parcours_matrice(matrice, Ml, Mc, "x")
            else:
                Ml = int(paire[1])
                parcours_matrice(matrice, Ml, Mc, "y")
        return matrice, Ml, Mc


o, Ml, Mc = main("jeu2.txt")
for l in range(Ml):
    for c in range(Mc):
        print("#" if o[l][c] else '.', end="")
    print()
