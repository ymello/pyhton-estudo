from math import sqrt

''' Exercicio 1 '''


def distancia(x1, y1, x2, y2):
    calc1 = (x2 - x1) ** 2
    calc2 = (y2 - y1) ** 2

    final = sqrt(calc2 + calc1)
    return final


'''exercicio 2'''


def calculo2(a, b, c):
    r = (a + b) ** 2
    s = (b + c) ** 2

    d = (r + s) // 2
    return d


''' Exercicio 3 '''


def idade(anos, meses, dias):
    mesesAnos = anos * 12
    diasMeses = (meses + mesesAnos) * 30
    idadeDias = diasMeses + dias

    return idadeDias


'''Exercicio 4 '''


def idadeRev(dias):
    meses = dias // 30
    diasFinais = dias % 30
    anos = meses // 12
    mesFinal = 0

    if meses >= 12:
        mesFinal = meses - (anos * 12)

    print(anos)
    print(mesFinal)
    print(diasFinais)


idadeRev(362)
