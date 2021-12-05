class Line:
    def __init__(self, A, B, ignore_diag=True):
        self.A = A
        self.B = B
        self.ignore_diag = ignore_diag
        self.liste = []
        self.liste_points()

    def liste_points(self):
        # diagonale pure
        xA, yA = self.A
        xB, yB = self.B
        #
        avancee = xB - xA
        montee = yB - yA
        #
        if avancee == 0:
            r = range(yA, yB + 1) if montee >= 0 else range(yB, yA + 1)
            for y in r:
                self.liste.append((xA, y))
        else:
            # sans doute plus simple à faire puisque je ne cherche
            # que -1, 0 ou 1
            m = (yB - yA) // (xB - xA)
            p = yA - m * xA
            r = range(xA, xB + 1) if avancee > 0 else range(xB, xA + 1)
            for x in r:
                if m == 0 and self.ignore_diag:
                    self.liste.append((x, m * x + p))

    def maj_matrice(self, matrice):
        for p in self.liste:
            matrice[p[1]][p[0]] += 1


def compte_sup_deux(matrice):
    N = len(matrice[0])
    r = range(N)
    somme = 0
    for i in r:
        for j in r:
            if matrice[i][j] > 1:
                somme += 1
    return somme


def main(fichier):
    with open(fichier) as fh:
        r = range(1_000)
        matrice = [[0 for i in r] for j in r]
        for ligne in fh:
            A, B = ligne.split(" -> ")
            A = eval("(" + A + ")")
            B = eval("(" + B + ")")
            l = Line(A, B)
            l.maj_matrice(matrice)
        N = compte_sup_deux(matrice)
        return N


print(main("jeu1.txt"))
