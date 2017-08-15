## 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar // considere us 1,00 =  R$ 3,27

dinheiro = float(input("quanto voce tem de dinheiro na sua carteira?"))


quantoDolares = dinheiro / 3.27

print("voce pode comprar {} dolares".format(round(quantoDolares, 2)))