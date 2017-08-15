## 8 - escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros


valorEmMetro = float(input("Escreva um valor em metro : "))


valorEmCentimetro = valorEmMetro / 0.010000
valorEmMilimetro = valorEmMetro / 0.0010000

print("O valor em metro: {}, O valor em Centimetro: {}, O valor em milimetro: {}".format(valorEmMetro,valorEmCentimetro,valorEmMilimetro))