def main(fichier):
    with open(fichier) as fh:
        resultats = {")": 0, "]": 0, "}": 0, ">": 0}
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
            if not valide:
                resultats[expression[i - 1]] += 1
    points = resultats[")"] * 3 + resultats["]"] * 57\
        + resultats["}"] * 1197 + resultats[">"] * 25137
    return points


print(main("jeu2.txt"))
