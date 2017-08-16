import math

def quadradoPerfeito(numero):
   verificar = numero**(1/2)



   if verificar is int:
      print("o numero {} é um quadrado perfeito do numero {}".format(numero, verificar))
   else:
      print("o numero {} não é um quadrado perfeito".format(numero))


quadradoPerfeito(25)