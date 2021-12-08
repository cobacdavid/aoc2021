def main(fichier):
    with open(fichier) as fh:
        somme = 0
        for ligne in fh:
            chiffres = ligne.strip().split('|')[1].split()
            for c in chiffres:
                if len(c) == 2 or len(c) == 4 or \
                   len(c) == 3 or len(c) == 7:
                    somme += 1
        return somme


print(main("jeu2.txt"))
