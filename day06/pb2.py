import copy


class GroupeLanternFish:
    def __init__(self, liste_age):
        self.liste_poissons = {i: 0 for i in range(9)}
        for a in liste_age:
            self.liste_poissons[a] += 1

    def une_evolution(self):
        tmp = copy.deepcopy(self.liste_poissons)
        for i in range(8):
            self.liste_poissons[i] = tmp[i + 1]
        self.liste_poissons[6] += tmp[0]
        self.liste_poissons[8] = tmp[0]

    def __str__(self):
        l = self.liste_poissons
        v = sum(self.liste_poissons.values())
        return f"{v} poissons"


def main(fichier):
    with open(fichier) as fh:
        liste = list(map(int, fh.readline().strip().split(",")))
        g = GroupeLanternFish(liste)
        for i in range(256):
            g.une_evolution()
        print(g)


main("jeu2.txt")
