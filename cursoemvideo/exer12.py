# 12 - faça um algoritmo que leia o Preço de uma produto e mostre seu novo preço com 5% de desconto.

precoProduto = float(input("digite o valor do produto"))

porcentagem = precoProduto * 0.05

valorComDesconto = precoProduto - porcentagem

print("o valor do produto com desconto é: {}".format(valorComDesconto))