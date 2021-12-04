class Grille:
    def __init__(self, liste):
        # self.matrice = [[0] * 5 for _ in range(5)]
        self.matrice = [[[l, 0] for l in liste[i*5:i*5 + 5]] for i in range(5)]

    def est_colonne_remplie(self, indice):
        produit = 1
        i = 0
        while produit != 0 and i < 5:
            produit *= self.matrice[i][indice][1]
            i += 1
        return produit != 0

    def est_ligne_remplie(self, indice):
        produit = 1
        i = 0
        while produit != 0 and i < 5:
            produit *= self.matrice[indice][i][1]
            i += 1
        return produit != 0

    def __str__(self):
        s = "[\n"
        for i in range(5):
            s += str(self.matrice[i]) + "\n"
        s += "]"
        return s

    def marque(self, nombre):
        for i in range(5):
            for j in range(5):
                if self.matrice[i][j][0] == nombre:
                    self.matrice[i][j][1] = 1

    def a_gagne(self):
        gagne = False
        i = 0
        while not gagne and i < 5:
            gagne = self.est_colonne_remplie(i) or self.est_ligne_remplie(i)
            i += 1
        return gagne

    def somme_non_marques(self):
        somme = 0
        for i in range(5):
            for j in range(5):
                if self.matrice[i][j][1] == 0:
                    somme += self.matrice[i][j][0]
        return somme


def main(fichier):
    with open(fichier) as fh:
        tirages = list(map(int, fh.readline().split(',')))
        grilles = []
        while True:
            if not fh.readline():
                break
            liste = []
            for _ in range(5):
                liste += list(map(int, fh.readline().split()))
            g = Grille(liste)
            # print(g)
            grilles.append(g)

    derniere_gagnante = None
    for numero in tirages:
        liste_grilles_a_enlever = []
        for i, g in enumerate(grilles):
            g.marque(numero)
            if g.a_gagne():
                derniere_gagnante = (g, numero)
                liste_grilles_a_enlever.append(g)
        for g in liste_grilles_a_enlever:
            grilles.remove(g)

    print(derniere_gagnante[0].somme_non_marques() * derniere_gagnante[1])


main("jeu2.txt")
