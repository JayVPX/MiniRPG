import random


def random_damage(vida: float, armor: bool):
    dano = random.randint(2,5)

    if(armor):
        dano = round(dano * 0.8)
        vida = vida - dano
    else:
        vida = vida - dano

    if (vida <= 0):
        print()
        print("Você morreu")
        print()
        print("GAME OVER")
        print()
        input("Pressione ENTER para sair...")

        exit()

    return vida, dano

def random_heal(vida: float):
    heal = random.randint(2, 5)
    vida = min(vida + heal, 30)
    return vida, heal

def show_life(vida):
    print(f"Sua vida atual: {vida}/30")

def logout():
    print("Opção inválida.")
    print()

    print("OBRIGADO POR JOGAR!")
    input("Pressione ENTER para sair...")

    exit()



def restart():
    print()
    print("OBRIGADO POR JOGAR!")
    input("Pressione ENTER para sair...")

    exit()

