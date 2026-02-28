from random import randint
from time import sleep

# o modulo random - randint >>> para ter algo aleatório no programa, podendo o computador interagir comigo
itens = ('Pedra', 'Papel', 'Tesoura')
# o computador escolhe um número entre 0 e 2
computador = randint(0, 2)
game = str(input("""Suas opções:
 [0] PEDRA:
 [1] PAPEL:
 [2] TESOURA:"""))
jogador = int(input("Qual é a sua jogada: "))
print("Computador jogou: {}".format(itens[computador]))
print("-=" * 20)
print("Jogador jogou: {}".format(itens[jogador]))
print("-=" * 20)

# Iniciando o game
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=" * 20)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA!")
