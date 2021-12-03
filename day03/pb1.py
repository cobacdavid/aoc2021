def vers_liste_bin(dec, longueur):
    rep = [0] * longueur
    i = longueur - 1
    while dec >= 1:
        dec, reste = divmod(dec, 2)
        rep[i] = reste
        i -= 1
    return rep


def vers_dec(liste_bin):
    return sum(2 ** (len(liste_bin) - i - 1) * c
               for i, c in enumerate(liste_bin))


def somme_liste(l1, l2):
    return [a + b for a, b in zip(l1, l2)]


def analyse_somme(nb_sommes, somme):
    return [int(a > nb_sommes // 2) for a in somme], \
        [int(a <= nb_sommes // 2) for a in somme]


def main(fichier):
    with open(fichier) as fh:
        for i, b in enumerate(fh):
            b = b.strip()
            if i == 0:
                L = len(b)
                somme = [0] * L
            b = eval('0b' + b)
            somme = somme_liste(somme, vers_liste_bin(b, L))
    g, r = map(vers_dec, analyse_somme(i + 1, somme))
    return g * r


print(main("jeu2.txt"))
