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


def selection(liste, indice, nb_vise):
    if len(liste) == 1:
        return liste[0]

    N = len(liste)
    somme = sum(l[indice] for l in liste)
    vise = nb_vise if somme >= N / 2 else 1 - nb_vise
    retenues = [l for l in liste if l[indice] == vise]
    return selection(retenues, indice + 1, nb_vise)


def main(fichier):
    with open(fichier) as fh:
        b = fh.readline().strip()
        L = len(b)
        liste = [vers_liste_bin(eval('0b' + b), L)]
        liste += [vers_liste_bin(eval('0b' + b.strip()), L) for b in fh]
    a, b = selection(liste, 0, 1), selection(liste, 0, 0)

    return vers_dec(a) * vers_dec(b)


print(main("jeu2.txt"))
