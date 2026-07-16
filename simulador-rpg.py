import random


def mostrar_titulo():
    print("===================================")
    print("      SIMULADOR DE RPG EM TEXTO     ")
    print("===================================")


def iniciar_jogo():
    nome = input("Digite o seu nome: ")
    hp = 100
    lvl = 1
    forca = 3
    exp = 0
    inventario = []
    status = True  # Vivo(True) ou morto(False)

    return nome, hp, lvl, forca, exp, inventario, status


mostrar_titulo()
nome, hp, lvl, forca, exp, inventario, status = iniciar_jogo()
