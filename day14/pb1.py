def etape(texte, dico):
    i = 1
    texte = texte
    while i < len(texte):
        cle = texte[i-1:i+1]
        if cle in dico:
            texte = texte[:i] + dico[cle] + texte[i:]
            i += 1
        i += 1

    return texte


def compte(texte):
    dico = {c: texte.count(c) for c in texte}
    maxi = max(dico.values())
    mini = min(dico.values())
    return maxi - mini


def main(fichier):
    with open(fichier) as fh:
        texte = fh.readline().strip()
        fh.readline()
        dico = {}
        for ligne in fh:
            ligne = ligne.strip().split(' -> ')
            dico[ligne[0]] = ligne[1]

    for _ in range(10):
        texte = etape(texte, dico)
    return compte(texte)


print(main("jeu2.txt"))
