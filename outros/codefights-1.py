def centuryFromYear(year):
    seculo = year // 100
    resto = year % 100

    if resto != 0:
        seculo += 1

    print(seculo)


centuryFromYear(1995)


centuryFromYear(2001)
