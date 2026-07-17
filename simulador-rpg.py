import random

weakness = {
    "humana": "Magia (elemental ou necromante)",
    "sylvan": "Ataques corporais em geral, e ataque de magia necromante",
    "Varyn": "Ataques de arco e flecha, particularmente por flechas venenosas",
    "Umbri": "Ataques corporais em geral, e ataques de magia elemental",
    "Chronari": "Ataques de magia, particularmente por magias sombrias",
    "Auriano": "Ataques de magia sombria.",
}

racas = {
    "Humano": {
        "id": 1,
        "hp": 100,
        "forca": 3,
        "description": "Humanos são versáteis e adaptáveis, aprendem rápido e evoluem qualquer habilidade.",
        "special": "Quanto menor a vida, maior a força e defesa.",
        "weakness": weakness["humana"],
    },
    "Sylvan": {
        "id": 2,
        "hp": 80,
        "forca": 5,
        "description": "Sylvans são habitantes da floresta, especialistas em arquearia e magia elemental. Possuem orelhas pontudas.",
        "special": "Sylvans têm uma ligação com a natureza, curam mais, usam plantas para fazer poções e venenos e tem resistência a venenos",
        "weakness": weakness["sylvan"],
    },
    "Varyns": {
        "id": 3,
        "hp": 120,
        "forca": 2,
        "description": "Varyns são mestres em combate corpo a corpo, capazes de lutar com lâminas de todos os tipos de material. Possuem escamas pelo corpo",
        "special": "Varyns possuem mais força, resistência a fogo, e possuem um rugido que atordoa quem estiver por perto.",
        "weakness": weakness["Varyn"],
    },
    "Umbri": {
        "id": 4,
        "hp": 90,
        "forca": 4,
        "description": "Umbri são guerreiros sombrios, dominam o combate corpo a corpo e possuem poderosas habilidades de magia sombria.",
        "special": "Umbri são resistentes ao frio, podem ver espíritos, detectam passagens secretas e resistem a corrupção.",
        "weakness": weakness["Umbri"],
    },
    "Chronari": {
        "id": 5,
        "hp": 110,
        "forca": 3,
        "description": "Chronoris são guardiões do tempo, mestres em magia elemental, especialmente em magias do tempo.",
        "special": "Chronoris podem manipular o tempo para obter vantagem em combate.",
        "weakness": weakness["Chronari"],
    },
    "Auriano": {
        "id": 6,
        "hp": 100,
        "forca": 3,
        "description": "Aurianos são mestres em tecnologia divina.",
        "special": "Itens fabricados possuem qualidade superior.",
        "weakness": weakness["Auriano"],
    },
}


def mostrar_titulo():
    print("===================================")
    print("      SIMULADOR DE RPG EM TEXTO     ")
    print("===================================")


def iniciar_jogo():
    nome = input("Digite o seu nome: ")
    # hp = 100
    lvl = 1
    # forca = 3
    exp = 0
    # inventario = []
    # status = True  # Vivo(True) ou morto(False)

    return nome, lvl, exp


def escolher_raca():
    print("Escolha a sua raça:")
    for raca in racas:
        print(
            f"{racas[raca]['id']}. {raca} (HP: {racas[raca]['hp']}, Força: {racas[raca]['forca']}, Descrição: {racas[raca]['description']}, Especial: {racas[raca]['special']}, Fraqueza: {racas[raca]['weakness']})"
        )

    escolha = int(input("Digite o número da raça escolhida: "))
    for raca in racas:
        if racas[raca]["id"] == escolha:
            return raca, racas[raca]["hp"], racas[raca]["forca"]

    print("Raça inválida. Escolhendo Humano por padrão.")
    return "Humano", racas["Humano"]["hp"], racas["Humano"]["forca"]


def sortear_monstro(jogador_lvl):
    # Lista de monstros: [nome, hp, força, exp]
    # slime = ["Slime", 10, 2, 10]
    # goblin = ["Goblin", 20, 4, 20]
    # troll = ["Troll", 40, 8, 40]
    # orc = ["Orc", 80, 16, 80]
    # mumia = ["Múmia", 160, 32, 160]
    # quimera = ["Quimera", 320, 64, 320]
    # dragao = ["Dragão", 1000, 100, 1000]

    monstros = {
        "slime": ["Slime", 10, 2, 10],
        "goblin": ["Goblin", 20, 4, 20],
        "troll": ["Troll", 40, 8, 40],
        "orc": ["Orc", 80, 16, 80],
        "mumia": ["Múmia", 160, 32, 160],
        "quimera": ["Quimera", 320, 64, 320],
        "dragao": ["Dragão", 1000, 100, 1000],
    }

    # Retornando monstros de acordo com lvl do jogador
    if jogador_lvl <= 5:
        monstro_sorteado = random.choice([monstros["slime"], monstros["goblin"]])
    elif jogador_lvl <= 15:
        monstro_sorteado = random.choice(
            [monstros["goblin"], monstros["troll"], monstros["orc"]]
        )
    else:
        monstro_sorteado = random.choice(
            [monstros["mumia"], monstros["quimera"], monstros["dragao"]]
        )

    return monstro_sorteado


def game_over():
    print("GAME OVER! Você morreu.")
    print("Obrigado por jogar.")
    exit(0)


def atacar(atacante_nome, atacante_forca, defensor_nome, defensor_hp, defensor_forca):
    atacante_sorte = random.randint(0, 6)
    defensor_sorte = random.randint(0, 6)

    dano = atacante_forca * atacante_sorte - defensor_forca * defensor_sorte
    defensor_hp = defensor_hp - dano  # defensor_hp -= dano

    if atacante_sorte == 6:
        print(
            f"{atacante_nome} acertou um ataque crítico! Dano de {dano}, HP do defensor agora é {defensor_hp}"
        )
    elif atacante_sorte > 0:
        print(
            f"{atacante_nome} acertou o alvo! Dano de {dano}, HP do defensor agora é {defensor_hp}"
        )
    else:
        print(
            f"{atacante_nome} errou o ataque! O defensor não sofreu dano, HP do defensor ainda é {defensor_hp}"
        )

    if defensor_hp <= 0:
        print(f"{defensor_nome} foi derrotado!")
        return True, defensor_hp


# calcular o level up
def calcular_lvl(jogador_lvl, jogador_exp, jogador_hp, jogador_forca, exp_monstro):
    jogador_exp = jogador_exp + exp_monstro
    exp_necessaria = jogador_lvl**3

    if jogador_exp >= exp_necessaria:
        jogador_lvl += 1
        jogador_hp += 100
        jogador_forca *= 2
        print(
            f"Parabéns! Você subiu de nível! Agora você é nível {jogador_lvl}, com {jogador_hp} de HP e {jogador_forca} de força."
        )
    return jogador_lvl, jogador_exp, jogador_hp, jogador_forca


mostrar_titulo()
nome, lvl, exp = iniciar_jogo()
raca, hp, forca = escolher_raca()
monstro_sorteado = sortear_monstro(lvl)
print(f"{monstro_sorteado}")
