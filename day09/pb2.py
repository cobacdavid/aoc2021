def voisins(matrice, l, c):
    h = len(matrice)
    w = len(matrice[0])
    liste = []
    if l != 0:
        liste.append((l - 1, c, matrice[l - 1][c]))
    if l != h - 1:
        liste.append((l + 1, c, matrice[l + 1][c]))
    if c != 0:
        liste.append((l, c - 1, matrice[l][c - 1]))
    if c != w - 1:
        liste.append((l, c + 1, matrice[l][c + 1]))
    return liste


def est_lower(valeur, liste_valeurs_voisins):
    lower = True
    for v in liste_valeurs_voisins:
        if valeur >= v[2]:
            lower = False
            break
    return lower


def parcours(matrice, l, c):
    for v in voisins(matrice, l, c):
        if v not in visites and matrice[l][c] <= v[2] and v[2] != 9:
            visites.append(v)
            bassins.append(v)
            parcours(matrice, v[0], v[1])

def main(fichier):
    global bassins
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
            if est_lower(pixel, voisins(matrice, l, c)):
                v_lower += [(l, c)]
    #
    Bassins = []
    for pb in v_lower:
        bassins = [(pb[0], pb[1])]
        parcours(matrice, pb[0], pb[1])
        Bassins.append(len(bassins))
    #
    prod = 1
    for s in sorted(Bassins)[-3:]:
        prod *= s
    return prod


visites = []
bassins = []


print(main("jeu2.txt"))
