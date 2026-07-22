import random


# Função para exibir o título de abertura
def mostrar_titulo():
    title = r"""
                    //    \
                   ((     ))
               ===  \_v_//  ===
 Art by          ====)_^_(====
Roland Waylor    ===/ O O \===
                 = | /_ _\ | =
                =   \/_ _\/   =
                     \_ _/
                     (o_o)
                      VwV
    """
    print(title)
    print("Bem-vindo ao FIBULA RPG!")


# ─── Classe PAI ────────────────────────────────────────
class Entidade:
    def __init__(self, nome, hp, forca):
        self.nome = nome
        self.hp = hp
        self.forca = forca

    def receber_dano(self, dano):
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0

    def esta_vivo(self):
        return self.hp > 0

    def atacar(self, alvo):
        atacante_sorte = random.randint(0, 6)
        defensor_sorte = random.randint(0, 6)

        if atacante_sorte == 6:
            print(f"{self.nome} acertou um crítico!")
        elif atacante_sorte > 0:
            print(f"{self.nome} acertou!")
        else:
            print(f"{self.nome} errou!")

        dano = self.forca * atacante_sorte - alvo.forca * defensor_sorte

        if dano > 0:
            alvo.receber_dano(dano)
            print(f"{alvo.nome} sofreu {dano} de dano.")
        else:
            print(f"{alvo.nome} não sofreu dano.")


# ─── Classe FILHA: Jogador ───────────────────────────
class Jogador(Entidade):
    def __init__(self, nome, hp, forca):
        super().__init__(nome, hp, forca)  # inicializa a parte comum
        self.level = 1
        self.exp = 0
        self.inventario = []

    def usar_item(self):
        if not self.inventario:
            print("Seu inventário está vazio!")
            return
        print("Inventário:")
        for index, item in enumerate(self.inventario):
            print(f"{index + 1}. {item}")
        opcao_item = int(input("Escolha o item (ou 0 para cancelar): "))
        if opcao_item == 0:
            return
        item_escolhido = self.inventario[opcao_item - 1]
        if item_escolhido == "Poção":
            print("Você usou uma poção!")
            self.hp += 20
            if self.hp > 100:
                self.hp = 100
            print(f"Seu HP agora é {self.hp}")
            self.inventario.pop(opcao_item - 1)
        else:
            print("Item inválido!")

    def fugir(self):
        import random

        sucesso = random.choice([True, False])
        if sucesso:
            print(f"{self.nome} fugiu com sucesso!")
            return True
        else:
            print(f"{self.nome} não conseguiu escapar!")
            return False


# ─── Classe FILHA: Monstro ──────────────────────────────
class Monstro(Entidade):
    def __init__(self, nome, hp, forca, exp):
        super().__init__(nome, hp, forca)  # inicializa a parte comum
        self.exp = exp


# Função para iniciar um novo jogo
def iniciar_novo_jogo():
    nome = input("Qual o seu nome? ")
    jogador = Jogador(nome, 100, 3)
    return jogador


# Função para sortear um monstro
def sortear_monstro(jogador_lv):
    monstros = [
        {"nome": "slime", "hp": 10, "forca": 2, "exp": 10},
        {"nome": "goblin", "hp": 20, "forca": 4, "exp": 20},
        {"nome": "troll", "hp": 40, "forca": 8, "exp": 40},
        {"nome": "orc", "hp": 80, "forca": 16, "exp": 80},
        {"nome": "múmia", "hp": 160, "forca": 32, "exp": 160},
        {"nome": "quimera", "hp": 320, "forca": 64, "exp": 320},
        {"nome": "dragão", "hp": 1000, "forca": 100, "exp": 1000},
    ]

    if jogador_lv < 5:
        escolhido = random.choice(monstros[0:3])
    elif jogador_lv < 10:
        escolhido = random.choice(monstros[2:6])
    else:
        escolhido = monstros[-1]

    return Monstro(
        escolhido["nome"], escolhido["hp"], escolhido["forca"], escolhido["exp"]
    )


# Função para exibir game over
def game_over():
    print("O jogo acabou.")
    print("Obrigado por jogar!")
    exit(1)


# Função para calcular o level up
def calcular_level(jogador, exp_monstro):
    jogador.exp = jogador.exp + exp_monstro
    experiencia_necessaria = 3**jogador.level

    if jogador.exp > experiencia_necessaria:  # Subiu de level?
        print("Level up!")
        jogador.level += 1
        jogador.hp = 100
        jogador.forca = jogador.forca * 2


# Função para obter uma poção
def obter_pocao():
    chance = random.random()
    if chance <= 0.2:
        print("Você ganhou uma poção!")
        return "Poção"
    else:
        return None


# Função principal do jogo
def main():
    mostrar_titulo()
    jogador = iniciar_novo_jogo()
    print("\n")

    jogador_enfrentando_monstro = False

    while True:
        if not jogador_enfrentando_monstro:
            monstro = sortear_monstro(jogador.level)

            print(f"\nUm {monstro.nome} aleatório aparece!")
            print(f"HP: {monstro.hp}\n")
            jogador_enfrentando_monstro = True
        else:
            print(f"\nVocê está enfrentando um {monstro.nome}!")
            print(f"HP: {monstro.hp}\n")

        print(f"{jogador.nome}: {jogador.hp}/100")
        print(f"Level: {jogador.level}")
        print("O que você deseja fazer?")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Fugir")
        print("4. Visualizar status")
        print("5. Sair do jogo")
        opcao = int(input())

        if opcao == 1:
            print("\n")
            # Jogador ataca o monstro
            jogador.atacar(monstro)
            print("\n")
            if monstro.esta_vivo():
                # Monstro ataca o jogador
                monstro.atacar(jogador)
                print("\n")
                if not jogador.esta_vivo():
                    game_over()
            else:
                # Jogador ganhou experiência
                print(f"Você ganhou {monstro.exp} XP!")
                calcular_level(jogador, monstro.exp)
                # Pode ganhar item
                pocao = obter_pocao()
                if pocao is not None:
                    jogador.inventario.append(pocao)
                jogador_enfrentando_monstro = False
                continue
        elif opcao == 2:
            jogador.usar_item()
            continue
        elif opcao == 3:
            fugiu = jogador.fugir()
            if fugiu:
                jogador_enfrentando_monstro = False
                continue
            else:
                # Monstro ataca o jogador
                monstro.atacar(jogador)
                print("\n")
                if not jogador.esta_vivo():
                    game_over()
        elif opcao == 4:
            print(f"\n{jogador.nome}")
            print(f"HP: {jogador.hp}/100")
            print(f"LV: {jogador.level}")
            print(f"EXP: {jogador.exp}")
            exp_proximo_nivel = 3**jogador.level
            print(f"Falta {exp_proximo_nivel - jogador.exp} XP para evoluir")
            print(f"Força: {jogador.forca}")
            print(f"Inventário: {jogador.inventario}\n")
            continue
        elif opcao == 5:
            game_over()
        else:
            print("Opção inválida!\n")
            continue


if __name__ == "__main__":
    main()
