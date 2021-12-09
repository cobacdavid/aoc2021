def voisins(matrice, l, c):
    h = len(matrice)
    w = len(matrice[0])
    liste = []
    if l != 0:
        liste.append(matrice[l - 1][c])
    if l != h - 1:
        liste.append(matrice[l + 1][c])
    if c != 0:
        liste.append(matrice[l][c - 1])
    if c != w - 1:
        liste.append(matrice[l][c + 1])
    return liste


def est_lower(valeur, liste_valeurs_voisins):
    lower = True
    for v in liste_valeurs_voisins:
        if valeur >= v:
            lower = False
    return lower


def main(fichier):
    with open(fichier) as fh:
        matrice = []
        for ligne in fh:
            matrice.append(list(map(int, list(ligne.strip()))))
        h = len(matrice)
        w = len(matrice[0])
        v_lower = []
        for l in range(h):
            for c in range(w):
                pixel = matrice[l][c]
                v = voisins(matrice, l, c)
                if est_lower(pixel, voisins(matrice, l, c)):
                    v_lower += [matrice[l][c] + 1]
    return sum(v_lower)


print(main("jeu2.txt"))
