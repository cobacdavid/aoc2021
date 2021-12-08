def reconnaissance(un, sept, quatre, huit, liste5):
    segments = {i: None for i in range(1, 8)}
    segments[1] = etape1(sept, un)
    perms2s4 = etape2(un, quatre)
    perms1s4s7 = etape3(liste5)
    perms4s7 = perms1s4s7.difference({segments[1]})
    segments[2], segments[4], segments[7] = etape4(perms2s4, perms4s7)
    segments[6] = etape5(liste5,
                         segments[2],
                         segments[4],
                         segments[7],
                         segments[1])
    segments[3] = etape6(un, segments[6])
    segments[5] = etape7(huit, segments)
    return segments


def etape1(sept, un):
    for c in sept.difference(un):
        return c


def etape2(un, quatre):
    perms2s4 = quatre.difference(un)
    return perms2s4


def etape3(liste5):
    return liste5[0].intersection(liste5[1]).intersection(liste5[2])


def etape4(s2s4, s4s7):
    ss4 = s2s4.intersection(s4s7)
    ss2 = s2s4.difference(ss4)
    ss7 = s4s7.difference(ss4)
    for e in ss4: s4 = e
    for e in ss2: s2 = e
    for e in ss7: s7 = e
    return s2, s4, s7


def etape5(liste, s2, s4, s7, s1):
    for chiffre in liste:
        if s2 in chiffre and s4 in chiffre and s7 in chiffre:
            ss6 = chiffre.difference({s1, s2, s4, s7})
            for e in ss6:
                s6 = e
    return s6


def etape6(un, s6):
    for c in un.difference(s6):
        return c


def etape7(huit, segments):
    ens = set()
    for v in segments.values():
        if v:
            ens.add(v)
    for c in huit.difference(ens):
        return c


def base(s):
    mabase = {}
    mabase[tuple(sorted([s[1], s[2], s[3], s[5], s[6], s[7]]))] = 0
    mabase[tuple(sorted([s[3], s[6]]))] = 1
    mabase[tuple(sorted([s[1], s[3], s[4], s[5], s[7]]))] = 2
    mabase[tuple(sorted([s[1], s[3], s[4], s[6], s[7]]))] = 3
    mabase[tuple(sorted([s[2], s[3], s[4], s[6]]))] = 4
    mabase[tuple(sorted([s[1], s[2], s[4], s[6], s[7]]))] = 5
    mabase[tuple(sorted([s[1], s[2], s[4], s[5], s[6], s[7]]))] = 6
    mabase[tuple(sorted([s[1], s[3], s[6]]))] = 7
    mabase[tuple(sorted([s[1], s[2], s[3], s[4], s[5], s[6], s[7]]))] = 8
    mabase[tuple(sorted([s[1], s[2], s[3], s[4], s[6], s[7]]))] = 9
    return mabase


def main(fichier):
    with open(fichier) as fh:
        somme = 0
        for ligne in fh:
            chiffres = ligne.strip().split('|')[0].split()
            a_reconnaitre = ligne.strip().split('|')[1].split()
            liste_ens_cinq = []
            for c in chiffres:
                if len(c) == 2:
                    un = set(list(c))
                elif len(c) == 3:
                    sept = set(list(c))
                elif len(c) == 4:
                    quatre = set(list(c))
                elif len(c) == 5:
                    liste_ens_cinq.append(set(list(c)))
                elif len(c) == 7:
                    huit = set(list(c))
            dico_seg = reconnaissance(un, sept, quatre, huit,
                                      liste_ens_cinq)
            ma_base = base(dico_seg)
            s = ""
            for chiffre in a_reconnaitre:
                cle = tuple(sorted(list(chiffre)))
                s += str(ma_base[cle])
            somme += int(s)
    return somme


print(main("jeu2.txt"))
