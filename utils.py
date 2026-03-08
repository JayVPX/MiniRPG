import random

def random_damage(vida: float, armor: bool):
    dano = random.randint(1,5)

    if(armor):
        dano = round(dano * 0.8)
        vida = vida - dano
    else:
        vida = vida - dano

    if (vida <= 0):
        print()
        print("Você morreu")
        print("GAME OVER")
        exit()
    return vida, dano

def random_heal(vida: float):
    heal = random.randint(2,10)
    vida = vida + heal
    return vida, heal

def show_life(vida):
    print(f"Sua vida atual: {vida}/30")

def logout():
    print("Opção inválida. Reinicie o jogo.")
    exit()
