import random

def random_damage(vida: float, armor: bool):
    dano = random.randint(2,8)

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
    heal = random.randint(5,10)
    vida = vida + heal
    return vida, heal

def show_life(vida):
    print(f"Sua vida atual: {vida}/50")

def logout():
    print("Opção inválida. Reinicie o jogo.")
    exit()
