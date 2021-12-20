# def recur(i, j, m):
#     if i == 0 and j == 0:
#         return m[i][j]
#     elif i == 0:
#         return recur(0, j - 1, m) + m[i][j]
#     elif j == 0:
#         return recur(i - 1, 0, m) + m[i][j]
#     return min(recur(i, j - 1, m), recur(i - 1, j, m)) + m[i][j]


def main(fichier):
    with open(fichier) as fh:
        m = []
        for ligne in fh:
            m.append(list(map(int, list(ligne.strip()))))

    N = len(m)

    c = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        c[0][i] = sum(m[0][k] for k in range(i+1))
        c[i][0] = sum(m[k][0] for k in range(i+1))
    for i in range(1, N):
        for j in range(1, N):
            c[i][j] = min(c[i-1][j], c[i][j-1]) + m[i][j]

    return c[N-1][N-1] - m[0][0]
    # return recur(N - 1, N - 1, m) - m[0][0]


print(main("jeu2.txt"))
