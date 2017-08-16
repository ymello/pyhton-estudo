def trocaData(dia,mes,ano):

    if mes == 1:
        nomeMes = "Janeiro"
    if mes == 2:
        nomeMes = "fevereiro"
    if mes == 3:
        nomeMes = "Março"
    if mes == 4:
        nomeMes = "Abril"
    if mes == 5:
        nomeMes = "Maio"
    if mes == 6:
        nomeMes = "junho"
    if mes == 7:
        nomeMes = "julho"
    if mes == 8:
        nomeMes = "Agosto"
    if mes == 9:
        nomeMes = "setembro"
    if mes == 10:
        nomeMes = "outubro"
    if mes == 11:
        nomeMes = "novembro"
    if mes == 12:
        nomeMes = "dezembro"


    print("{} de {} de {}".format(dia,nomeMes,ano))



trocaData(2,1,2016)

trocaData(15,8,2017)

trocaData(7,8,1996)

trocaData(27,10,1995)

trocaData(2,12,2013)