class octopus:
    def __init__(self, e):
        self.energie = e

    def step_energie(self):
        self.energie = (self.energie + 1) % 10


def etape(matrice):
    n = len(matrice)
    r = range(n)
    veut_flashe = []
    for i in r:
        for j in r:
            matrice[i][j].step_energie()
            if matrice[i][j].energie == 0:
                veut_flashe.append((i, j))
    a_flashe = []
    while len(veut_flashe) > 0:
        o = veut_flashe.pop(0)
        a_flashe.append(o)
        i, j = o
        if i != 0:
            matrice[i-1][j].step_energie()
            if matrice[i-1][j].energie == 0 and (i-1, j) not in a_flashe:
                veut_flashe.append((i-1, j))
            #
            if j != 0:
                matrice[i-1][j-1].step_energie()
                if matrice[i-1][j-1].energie == 0 and (i-1, j-1) not in a_flashe:
                    veut_flashe.append((i-1, j-1))
            if j != n-1:
                matrice[i-1][j+1].step_energie()
                if matrice[i-1][j+1].energie == 0 and (i-1, j+1) not in a_flashe:
                    veut_flashe.append((i-1, j+1))
        if i != n-1:
            matrice[i+1][j].step_energie()
            if matrice[i+1][j].energie == 0 and (i+1, j) not in a_flashe:
                veut_flashe.append((i+1, j))
            #
            if j != 0:
                matrice[i+1][j-1].step_energie()
                if matrice[i+1][j-1].energie == 0 and (i+1, j-1) not in a_flashe:
                    veut_flashe.append((i+1, j-1))
            if j != n-1:
                matrice[i+1][j+1].step_energie()
                if matrice[i+1][j+1].energie == 0 and (i+1, j+1) not in a_flashe:
                    veut_flashe.append((i+1, j+1))
        if j != 0:
            matrice[i][j-1].step_energie()
            if matrice[i][j-1].energie == 0 and (i, j-1) not in a_flashe:
                veut_flashe.append((i, j-1))
        if j != n-1:
            matrice[i][j+1].step_energie()
            if matrice[i][j+1].energie == 0 and (i, j+1) not in a_flashe:
                veut_flashe.append((i, j+1))
    for o in a_flashe:
        i, j = o
        matrice[i][j].energie = 0
    return len(a_flashe)


def print_matrice(M):
    s = ""
    n = len(M)
    r = range(n)
    for i in r:
        for j in r:
            s += str(M[i][j].energie)
        s += "\n"
    print(s)


def main(fichier):
    with open(fichier) as fh:
        for i, ligne in enumerate(fh):
            ligne = ligne.strip()
            if i == 0:
                n = len(ligne)
                matrice = [[0 for _ in range(n)] for _ in range(n)]
            matrice[i] = []
            for e in map(int, list(ligne)):
                matrice[i].append(octopus(e))

    N = 0
    step = 0
    while N != n ** 2:
        N = etape(matrice)
        step += 1
    print_matrice(matrice)
    print(step)


main("jeu2.txt")
