def init(texte):
    dico_dest = {}
    for i in range(1, len(texte)):
        couple = texte[i - 1:i + 1]
        alimente(couple, dico_dest)
    return dico_dest


def alimente(couple, dico_dest, v=1):
    if couple in dico_dest:
        dico_dest[couple] += v
    else:
        dico_dest[couple] = v


def etape(dico_assoc, dico):
    dico_dest = {}
    for k, v in dico.items():
        alimente(k[0] + dico_assoc[k], dico_dest, v)
        alimente(dico_assoc[k] + k[1], dico_dest, v)
    return dico_dest


def compte(dico):
    dl ={}
    for k, v in dico.items():
        alimente(k[0], dl, v)
        alimente(k[1], dl, v)
    return dl


def main(fichier):
    with open(fichier) as fh:
        texte = fh.readline().strip()
        fh.readline()
        dico_assoc = {}
        for ligne in fh:
            ligne = ligne.strip().split(' -> ')
            dico_assoc[ligne[0]] = ligne[1]

    dico_e = init(texte)
    for _ in range(40):
        dico_e = etape(dico_assoc, dico_e)
    dl = compte(dico_e)
    dl[texte[0]] += 1
    dl[texte[-1]] += 1
    for k in dl:
        dl[k] //= 2
    M, m = max(dl.values()), min(dl.values())
    return M - m


print(main("jeu2.txt"))
