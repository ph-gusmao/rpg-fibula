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


def sortear_monstro(jogador_lvl):
    # Lista de monstros: [nome, hp, força, exp]
    slime = ["Slime", 10, 2, 10]
    goblin = ["Goblin", 20, 4, 20]
    troll = ["Troll", 40, 8, 40]
    orc = ["Orc", 80, 16, 80]
    mumia = ["Múmia", 160, 32, 160]
    quimera = ["Quimera", 320, 64, 320]
    dragao = ["Dragão", 1000, 100, 1000]


mostrar_titulo()
nome, hp, lvl, forca, exp, inventario, status = iniciar_jogo()
