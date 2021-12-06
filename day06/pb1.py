class Lanternfish:
    def __init__(self, age=None):
        self.age = age or 8

    def cycle(self):
        self.age -= 1
        if self.age < 6:
            self.age %= 7

    def est_age_nul(self):
        return self.age == 0


class GroupeLanternFish:
    def __init__(self, liste_age):
        self.liste_poissons = []
        for a in liste_age:
            self.liste_poissons.append(Lanternfish(a))

    def une_evolution(self):
        somme = 0
        for f in self.liste_poissons:
            somme += f.est_age_nul()
        for f in self.liste_poissons:
            f.cycle()
        for _ in range(somme):
            self.liste_poissons.append(Lanternfish())

    def __str__(self):
        l = [f.age for f in self.liste_poissons]
        # return f"{len(l)} poissons : {str(l)}"
        return f"{len(l)} poissons"


def main(fichier):
    with open(fichier) as fh:
        liste = list(map(int, fh.readline().strip().split(",")))
        g = GroupeLanternFish(liste)
        for i in range(80):
            g.une_evolution()
        print(g)


main("jeu2.txt")
