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


def parcours(dico, debut, fin, cheminActuel=[], liste_visites=[], listeg=[]):
    if debut == fin:
        cheminActuel.append(debut)
        listeg.append(cheminActuel)
    else:
        cheminActuel = cheminActuel + [debut]
        if debut.upper() != debut:
            liste_visites = liste_visites + [debut]
        for v in dico[debut]:
            if v not in liste_visites:
                parcours(dico, v, fin, cheminActuel, liste_visites, listeg)
        return len(listeg)


def main(fichier):
    with open(fichier) as fh:
        dico = {}
        for ligne in fh:
            ligne = ligne.strip()
            graphe(dico, ligne)
    return parcours(dico, "start", "end")


print(main("jeu3.txt"))
