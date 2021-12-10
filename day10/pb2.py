def main(fichier):
    with open(fichier) as fh:
        score = []
        j = 0
        score_ouvrants = {"(": 1, "[": 2, "{": 3, "<": 4}
        for expression in fh:
            expression = list(expression.strip())
            pile = []
            valide = True
            i = 0
            while valide and i < len(expression):
                e = expression[i]
                if e == ")":
                    valide = len(pile) > 0 and pile.pop() == "("
                elif e == "]":
                    valide = len(pile) > 0 and pile.pop() == "["
                elif e == ">":
                    valide = len(pile) > 0 and pile.pop() == "<"
                elif e == "}":
                    valide = len(pile) > 0 and pile.pop() == "{"
                else:
                    pile.append(e)
                i += 1
            if valide:
                j += 1
                score_e = 0
                while len(pile) > 0:
                    e = pile.pop()
                    score_e = (score_e + score_ouvrants[e]) * 5
                score_e //= 5
                score.append(score_e)

        score.sort()
        return score[j // 2]


print(main("jeu2.txt"))
