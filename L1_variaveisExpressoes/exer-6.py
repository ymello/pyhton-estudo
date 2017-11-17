# Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A formula de conversao , sendo F a temperatura em Fahrenheit
# e C a temperatura em Celsius.

C = int(input("Qual a sua temperatua em Celsius? "))


F = C * (9.0/5.0)+32.0

print("Sua temperatura em Fahrenheit é {}".format(F))