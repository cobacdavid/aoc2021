def graphe(dico, ligne):
    debut, fin = ligne.split("-")
    if debut in dico:
        dico[debut].append(fin)
    else:
        dico[debut] = [fin]
    if fin in dico:
        dico[fin].append(debut)
    else:
        dico[fin] = [debut]


def dico_liste(sommet, dico, liste):
    if sommet in dico:
        dico[sommet] += 1
    else:
        dico[sommet] = 1
    if sommet == "start":
        liste.append(sommet)
    deux_atteint = False
    for k, v in dico.items():
        if v == 2 and k != "start":
            deux_atteint = True
    if deux_atteint:
        for k in dico:
            liste.append(k)
    return liste


def parcours(dico, debut, fin, cheminActuel=[],
             dico_visites={}, liste_visites=[], listeg=[]):
    if debut == fin:
        cheminActuel.append(debut)
        listeg.append(cheminActuel)
    else:
        cheminActuel = cheminActuel + [debut]
        if debut.upper() != debut:
            liste_visites = dico_liste(debut, dico_visites, liste_visites[:])
        for v in dico[debut]:
            if v not in liste_visites:
                parcours(dico, v, fin, cheminActuel,
                         dico_visites.copy(), liste_visites, listeg)
        return len(listeg)


def main(fichier):
    with open(fichier) as fh:
        dico = {}
        for ligne in fh:
            ligne = ligne.strip()
            graphe(dico, ligne)
    return parcours(dico, "start", "end")


print(main("jeu3.txt"))
