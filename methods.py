from paths.magePath import *
from paths.roguePath import *
from methods import *
from utils import *
import time


def intro():
   
    print("=== RPG: Tríade do Destino ===")
    print()
    print('Bem-vindo a Valtherra, um mundo mágico, sombrio e repleto de desafios. Aqui, infinitas possibilidades aguardam por você.')
    print("Escolha uma das três jornadas e viva na pele uma experiência única, onde cada decisão moldará o seu destino.")
    print("Cada história, enredo, ambientação e personagem são exclusivos da sua escolha, e cada situação será uma consequência direta das suas ações.")
    print("Será você capaz de conquistar a glória, enfrentar monstros e desvendar mistérios antigos, ou sucumbirá aos perigos que espreitam nas sombras de Valtherra?\n")
    time.sleep(2)

    print("O que está esperando? A glória não é alcançada por quem hesita. O destino espera apenas pelos audazes.\n")
  
    
    print()
    print('Feito por: João Praxedes & Vitor Guerra')
    print()

def select_class():
    print("=============================")
    time.sleep(2)

    print()
    print("Escolha sua classe:")
    print("1 - Mago")
    print("2 - Ladino")
    print("3 - Guerreiro")
    print()

    classe = input('> ')
    time.sleep(1)
    if classe == "1":
        print("=== Você escolheu: MAGO ===")
        print()
        print("Você é um aprendiz mago enviado pela Academia Raya Lucaria.")
        print("Sua missão é investigar a Torre da Lua Quebrada, uma antiga torre de magia abandonada.")
        print("Torre esta que já foi o lar de um grande Arquimago, que dizem ser o criador de uma magia capaz de rasgar a realidade e destruir o mundo.")
        print("Há alguns anos, criaturas mágicas começaram a sair da torre e atacar vilarejos.")
        print("Se você resolver esse mistério, finalmente será reconhecido como um verdadeiro mago.")
        print()


    elif classe == "2":
        print("=== Você escolheu: LADINO ===")
        print()
        print("Você é um aventureiro de Rank médio em busca de garantir sua subsistência e uma vida com alguns luxos.")
        print("Vive resgatando tesouros e riquezas encontradas em suas empreitadas nas diversas estruturas antigas, perigosas e aparentemente abandonadas pelo mundo de Valtherra.")
        print("Em uma taverna, você ouve um grupo de aventureiros conversando sobre certos rumores acerca de uma dungeon")
        print("Mais especificamente, a dungeon são as Catacumbas de Eldritch, uma antiga civilização que há muito já se ruiu.")
        print("Dizem que no fundo da dungeon existe um baú cheio de tesouros valioso, que quem o encontrar viverá o resto da vida sem se preocupar com gastos.")
        print("Movido pela ganância e curiosidade, você decide explorar esse desafio em forma de ruínas.")
        print("Porque afinal, quem não arrisca, não petisca...")
        print()


    elif classe == "3":
        print("=== Você escolheu: GUERREIRO ===")
        print()
        print("Você é o guerreiro da profecia, escolhido pela Deusa da Luz, Luminarie, abençoado com um poder sagrado latente.")
        print("Seu destino sempre esteve escrito nas estrelas. Destrua o mal que caminha, ou seja, o Rei Demônio que assola estas terras.")
        print("Com coragem e fé inabalável, você se vê cruzando as terras devastadas de Ashland, lar dos demônios.")
        print("Após dias caminhando sob o inferno na terra, diante de você está a Fortaleza de Velkarys, morada do Rei Demônio.")
        print()
    
    return classe

def warrior_path():
    print("UGA BUGA UGA")

def mage_path():
    vidaInicial = 30
    buffArmor = False

    time.sleep(2)
    # Intro do Mage
    print("\n=== EXTERIOR DA TORRE DA LUA QUEBRADA ===\n")
    print("Após dias de viagem, você finalmente chega ao vale onde a torre se encontra.")
    print('A Torre da Lua Quebrada se ergue diante de você, mesmo parcialmente destruída, ainda é possível sentir a grandeza que um dia a torre já teve.')
    print('Runas antigas brilham fracamente nas paredes de pedra, você consegue sentir a mana instável pairando no ar ao seu redor.')
    print("Enquanto você observa a entrada principal, algo se move entre as ruínas.")

    # First Step
    vida = mage_start(vidaInicial, buffArmor)

    # Second Step  
    vida, secondStepResposta = mage_tower_entrance(vida, buffArmor)

    # Local de partida baseado na Segunda Escolha
    if(secondStepResposta in ('1','2')):
        vida, buffArmor = mage_library(vida, buffArmor)  # Caminho para Biblioteca
        vida = mage_staircase(vida, buffArmor)           #Depois vai para a Escadaria
    
    elif(secondStepResposta =="3"):
        vida, buffArmor = mage_laboratory(vida, buffArmor)      #Caminho para laboratório secreto
     

    mage_pre_boss_intro(vida, buffArmor)    #INTRO PRE BOSS FIGHT

    mage_boss_fight(vida, buffArmor)        #BOSS FIGHT

    mage_end()                              #END

def rogue_path():
    vidaInicial = 30
    buffArmor = False

    # Flags para registrar acontecimentos que mudam o rumo a longo prazo
    poisoned = 0
    beast_defeated = 0

    time.sleep(2)
    # Intro do Ladino
    print("Após uma longa procura pela exata localização dessas antigas ruínas.")
    print("Recolhendo informações de outros aventureiros, seguindo rumores de mal-informados e ouvindo histórias das várias tragédias que ocorreram nessa estrutura curiosa, mas traiçoeira.")
    print("Você finalmente se encontra diante delas.")
    print("Agora, você está diante das Catacumbas de Eldritch.")
    print("Um lugar que, de acordo com rumores, promete muita prosperidade, mas acompanhada de perigos à altura, sendo local onde muitos aventureiros adentraram, mas nunca saíram.")
    print("Você deve seguir com muita cautela!")

    # First Step
    vida, poisoned = rogue_start(vidaInicial, buffArmor)

    # Second Step  
    vida, secondStepResposta = catacombs_entrance(vida, buffArmor)

     # Local de partida baseado na Segunda Escolha
    if(secondStepResposta == '1'):
        vida, beast_defeated = dark_corridor(vida, buffArmor)         # Caminho para Corredor Sombrio
    elif(secondStepResposta == '2'):
        vida = narrow_corridor(vida, buffArmor)                       # Caminha para Corredor Estreito
    
    #Fourth
    vida = treasure_room(vida, buffArmor)

    #End
    rogue_end(vida, buffArmor, poisoned, beast_defeated)
    
