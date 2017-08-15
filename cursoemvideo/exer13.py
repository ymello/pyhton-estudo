# 13 - faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("digite o valor do seu salario: "))

porcentagem = salario * 0.15

salarioComAumento = salario + porcentagem

print("o valor do produto do seu salario com aumento é: {}".format(salarioComAumento))
