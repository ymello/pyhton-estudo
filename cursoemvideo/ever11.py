# 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pinta-lo sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("digite a largura: "))
altura = float(input("digite a altura: "))

area = largura * altura
qtdLatas = area //2

print("a qauntidade de tintas é: {}".format(qtdLatas))