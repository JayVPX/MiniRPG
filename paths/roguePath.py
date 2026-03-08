from utils import *
import time

## Chegando nas Catacumbas
def rogue_start(vida: float, armor: bool):
    time.sleep(2)
    print()
    print("A estrutura é antiga e desgastada pelo tempo.")
    print("Grandes blocos de pedra escura formam um arco parcialmente destruído, coberto por musgo e raízes que se infiltraram nas rachaduras ao longo dos séculos.")
    print("O interior é tomado por uma escuridão densa, como se a própria luz hesitasse em atravessar aquele limiar.")
    print("Um ar frio e úmido escapa lentamente das profundezas, carregando consigo o cheiro de pedra antiga e decomposição.")

    time.sleep(2)
    print()
    print("Ao redor da entrada, restos quebrados de pilares e esculturas esquecidas sugerem que aquele lugar já pertenceu a uma civilização poderosa.")
    print("Agora, tudo o que resta são ruínas… e silêncio.")

    time.sleep(1)
    print()
    print("Por um breve momento, você tem a sensação de que algo nas profundezas observa sua chegada.")

    time.sleep(2)
    print()
    print("O que você faz?")
    print()
    print("1- Entrar nas catacumbas")
    print("2- Observar a entrada com mais atenção")
    print("3- Voltar para a estrada\n")

    show_life(vida)
    resposta = input("> ")
    time.sleep(1)

    poisoned = 0
    if (resposta == '1'):
        print()
        print("Você se sente confiante, traz consigo, em sua cintura, sua espada curta, leve e rápida, que acompanhou você nos diversos embates que teve durante sua vida de aventureiro.")
        print("Além de sua besta leve amarrada em suas costas, a qual em conjunto com sua grande pontaria torna você um inimigo bastante perigoso.")
        print("Isso tudo sem contar as diversas armas mais sutis e ocultas que você carrega consigo, esperando momentos oportunos para serem usadas.")
        print("Como facas de arremesso, pedaço robusto de madeira, pederneira e aço.")

        time.sleep(2)
        print()
        print("Se enchendo de coragem, e talvez um pouco de tolice, você encara aquela escuridão e segue adentro como se você não tivesse nada a temer.")
        print("Infelizmente, sua falta de cautela é respondida com uma aranha pulando no seu peito direito e perfurando suas presas no seu pescoço.")
        print("Ela era relativamente grande em relação ao tamanho de aranhas comuns.")
        print("possuía um corpo majoritariamente negro como a escuridão, com detalhes púrpuros chamativos, e olhos escarlates que transpareciam um perigo mortal.")
        poisoned = 1

        time.sleep(2)
        print()
        print("Tudo ocorreu muito rápido, mas você também reagiu ao perigo eminente o mais veloz que pôde.")
        print("No momento que as presas pernetraram seu pescoço, em resposta a dor, você puxa a criatura com a mão esquerda com toda sua força enquanto segura firmemente a empunhadura da sua espada com a mão direita.")
        print("Como resultado da força aplicada, você desanexa ela de seu corpo e joga ela no ar, momento no qual você habilmente desembanha a espada e no mesmo movimento corta a aranha ao meio antes dela aterrisar.")

        time.sleep(2)
        print()
        print("Você definitivamente é um lutador ágil e habilidoso, e você sabe disso.")
        print("Porém, nesse momento você percebe que não agir diligentemente pode lhe custar mais do que uma mordida de uma criatura relativamente pequena.")
        print("Então, você afia os olhos ao finalmente ter adentrado as catacumbas, sente seu pescoço doendo e vê sangue escorrendo, mas sente que consegue continuar.")

        vida, dano = random_damage(vida, armor)
        print(f'Você recebeu {dano} de dano')
        show_life(vida)
        print()
    
    elif (resposta == '2'):
        print()
        print("Você se sente confiante, traz consigo, em sua cintura, sua espada curta, leve e rápida, que acompanhou você nos diversos embates que teve durante sua vida de aventureiro.")
        print("Além de sua besta leve amarrada em suas costas, a qual em conjunto com sua grande pontaria torna você um inimigo bastante perigoso.")
        print("Isso tudo sem contar as diversas armas mais sutis e ocultas que você carrega consigo, esperando momentos oportunos para serem usadas.")
        print("Como facas de arremesso, pedaço robusto de madeira, pederneira e aço.")

        time.sleep(2)
        print()
        print("Você é corajoso, mas não é um tolo.")
        print("Você sobreviveu até hoje mesmo vivendo aventuras perigosas, e isso se deve muito pela sua astúcia, além da sua capacidade de combate.")
        print("Então, você olha atentamente para o interior daquele lugar mórbido e sente a presença de uma criatura a espreita, esperando o momento para dar o bote.")
        print("A maior parte dela se funde com a escuridão, mas ela possui traços chamativos que a entregam, principalmente os seus olhos vividamente avermelhados.")
        print("Vocẽ rapidamente saca sua besta leve das costas e atira uma flecha precisamente entre os olhos chamativos dessa criatura que exala perigo, a qual, sem tempo de reagir, cai no chão sem vida.")

        time.sleep(2)
        print()
        print("Após abater o primeiro inimigo, você entra nas ruínas cautelosamente, com o olhar afiado, segurando firmemente a empunhadura da sua espada")

    elif (resposta == '3'):
        print()
        print("Você pressente um perigo mortal nas profundezas dessas ruínas.")
        print("Com sua experiência de aventureiro Rank médio, sente que apenas a morte lhe espera ao entrar nesse lugar sombrio.")
        print("Você decide então preservar a própria vida, percebendo que a ganância nessa situação lhe traria seu fim precoce.")
        print("Você percorre o extenso caminho de volta até a capital Lunaria, e começa a buscar por novas oportunidades de ganho monetário.")
        print("Talvez tenha sido uma boa ideia evitar o perigo, pois você definitivamente ainda está vivo e fisicamente disposto para novas aventuras.")
        print("Mas quem sabe o tamanho das riquezas poderiam ter lá...")
        print("GAME OVER")
        print()
        exit()
    else:
        logout()
    
    return vida, poisoned
    

## Entrada nas Catacumbas
def catacombs_entrance(vida: float, armor: bool):
    print()
    print("Você se encontra numa sala muito escura, sendo a única fonte de luz a entrada das catacumbas que ilumina a parte da sala mais próxima do exterior.")

    time.sleep(2)
    print()
    print("O que você faz?")
    print()
    print("1- Seguir em frente sem uma fonte de luz")
    print("2- Acender uma tocha\n")

    show_life(vida)
    resposta = input("> ")
    time.sleep(1)

    if (resposta == '1'):
        print()
        print("Você decide seguir em frente sem acender nenhuma fonte de luz.")
        print("Você toma essa decisão, pois que teme que a luz atraia outras criaturas se esgueirando pela escuridão, e segue em frente se guiando principalmente pela audição e tato.")
    elif (resposta == '2'):
        print()
    else:
        logout()


    return vida, resposta

## Corredor Escuro
def dark_corridor(vida: float, armor: bool):
    print()
    print("Você tenta manter sua mão esquerda encostando pelas paredes para a fim de sentir para onde você está seguindo.")

    time.sleep(2)
    print()
    print("Você sente que conseguiu prosseguir bastante caminho adentro, embora tenha perdido o senso de direção de onde veio.")

    time.sleep(2)
    print()
    print("O chão é duro, o clima é fúnebre e a única coisa que você ouve além da sua respiração são gotas de algum líquido caem do teto.")
    print("Você segue aguçando todos seus sentidos em esperança de se guiar nesse caminho incerto.")

    time.sleep(2)
    print("Você estranha... Há momentos atrás você estava caminhando por um chão duro e agora sente algo menos rígido sob seus pés")

    time.sleep(2)
    print()
    print("O que você faz?")
    print()
    print("1- Examinar piso")
    print("2- Seguir em frente\n")

    show_life(vida)
    resposta = input("> ")
    time.sleep(1)

    beast_defeated = 0
    if (resposta == '1'):
        print()
        print("Você agacha e examina no que você está em pisando.")
        print("Um questionamento que antes era sobre \"onde você está pisando?\", se torna sobre \"em quem você pisando?\".")
        print("Você está em cima de um cadáver morto, cheio de marcas de garras sangrando pelo corpo.")
        print("Você não consegue conter o susto que você tomou a ver essa cena pesada.")
        print("Seu susto acordou algo, algo com passos pesados, bufando como uma fera, mas impossível de identificar naquela escuridão.")
        vida, beast_defeated = beast_encounter(vida, armor)
    elif (resposta == '2'):
        print()
        print("Você ignora complementamente sobre o que você está pisando e se mantém focado em prosseguir cautelosamente enquanto se escora pela parede daquilo que parece ser um corredor bem extenso.")
        print("Você caminha pacientemente através daquela escuridão, até encontrar o que parece ser o fim daquele corredor silencioso e vazio.")
    else:
        logout()
    
    print()
    print("Você após muito caminhar por aquele corredor escuro, se encontra numa sala estranhamente bem iluminada")
    
    return vida, beast_defeated

## Encontro com a monstruosidade
def beast_encounter(vida: float, armor: bool):

    beast_defeated = 0

    time.sleep(2)
    print()
    print("Você ouve um rosnado grave ecoando pelo corredor, seguido do som de algo farejando o ar.")
    print("A criatura se move lentamente pela escuridão, como um predador acostumado a caçar naquele ambiente.")

    time.sleep(2)
    print()
    print("O que você faz?")
    print()
    print("1- Acender tocha")
    print("2- Atacar primeiro no escuro")
    print("3- Ficar imóvel")
    print("4- Tentar recuar\n")

    show_life(vida)
    resposta = input("> ")
    time.sleep(1)

    if (resposta == '1'):
        print("Você sente que está em completamente vulnerável e em desvantagem no escuro contra esse predador faminto.")
        print("Você tem quase certeza que ele já está totalmente certo da sua presença naquele lugar escuro onde ambos não se veem.")
        print("Você se conformou que é tarde demais, agora é matar ou morrer.")
        print("Você recolhe um bastão de madeira nos seus pertences, juntamente a uma perdeneira e pedaço de aço, utilizando-os para criar fogo acender seu bastão.")

        time.sleep(2)
        print()
        print("A chama da tocha ganha vida em sua mão, iluminando o corredor com uma luz trêmula e alaranjada.")
        print("As sombras nas paredes dançam de forma inquietante enquanto o fogo lentamente revela o que se esconde diante de você.")

        time.sleep(2)
        print()
        print("A poucos passos de distância, algo enorme se move.")

        time.sleep(1)
        print()
        print("A luz finalmente alcança a criatura.")

        time.sleep(1)
        print()
        print("É um grande predador quadrúpede, semelhante a um leão, porém muito mais sinistro.")
        print("Sua pelagem é negra e irregular, absorvendo parte da luz da tocha como se a própria escuridão tivesse se agarrado ao seu corpo.")
        print("Seus músculos são largos e poderosos, e cada movimento faz suas garras enormes rasparem lentamente na pedra do chão.")

        time.sleep(2)
        print()
        print("Seus olhos vermelhos brilham intensamente na penumbra, fixos em você, atentos a cada gesto seu.")

        time.sleep(1)
        print()
        print("Quando a criatura move a cauda, você percebe fileiras de espinhos rígidos percorrendo toda sua extensão, que balançam lentamente no ar como uma ameaça silenciosa.")

        time.sleep(1)
        print()
        print("A fera solta um rosnado baixo e profundo, revelando presas longas e manchadas de sangue seco.")
        print("O cheiro de carne em decomposição que você havia sentido antes agora faz sentido.")

        time.sleep(2)
        print()
        print("Espalhados pelo chão ao redor da criatura estão restos de ossos e pedaços de equipamentos enferrujados — evidências claras de aventureiros que não tiveram a mesma sorte que você…")
        print("Pelo menos até agora.")
        
        time.sleep(2)
        print()
        print("O Leão Sombrio de Eldritch parece ter vivido muito tempo nas profundezas dessas catacumbas.")

        time.sleep(1)
        print()
        print("E, neste momento, ele claramente decidiu que você será sua próxima refeição.")
        vida, beast_defeated = beast_battle(vida, armor)
    elif (resposta == '2'):
        print("Você, mesmo naquela escuridão e sem visão do ser perigoso que está na sua frente, atira uma flecha contra aquela criatura usando sua besta.")
        print("Pela aparente grande extensão da criatura, deduzida pelos passos pesados e rosnar robusto, era praticamente impossível errar.")
        print("A criatura responde quase que instantaneamente a flecha que lhe perfurou, soltando o rugido aterrorizante em sua direção.")
        print("Juntamente com o rugido, ouve claramente a gigantesca criatura avançando furiosa contra sua direção, com passos muito fortes exprimindo demasiada viceralidade e a intenção impiedosa da mesma.")
        time.sleep(2)
        print()
        print("O que você faz?")
        print()
        print("1- Atacar com sua espada")
        print("2- Fugir")
        print("3- Desviar para o lado\n")

        show_life(vida)
        respostaSecond = input("> ")
        time.sleep(1)

        if (respostaSecond == '1'):
            print("Você reage por puro instinto.")
            print("Assim que ouve a criatura avançando em sua direção, você desembainha sua espada e avança também, tentando acertar um golpe na escuridão antes que ela o alcance.")
            print("Mas você não consegue ver o inimigo.")
            print("Apenas ouvir.")

            time.sleep(1)
            print()
            print("Por um breve momento, sua lâmina corta o ar vazio.")
            print("No instante seguinte, algo colossal colide contra você.")

            time.sleep(1)
            print()
            print("Uma força esmagadora atinge seu corpo com violência brutal.")
            print("Garras enormes atravessam seu peito como se sua armadura e carne fossem papel.")
            print("Você mal tem tempo de entender o que aconteceu.")

            time.sleep(1)
            print()
            print("A última coisa que você ouve é um rosnado profundo ecoando nas catacumbas enquanto sua espada escapa de sua mão e cai no chão de pedra.")

            time.sleep(1)
            print()
            print("Seu corpo se junta aos muitos outros que nunca conseguiram sair daquele lugar.")

            time.sleep(1)
            print()
            print("Você morreu.")
            print("GAME OVER")
            print()
            exit()

        elif (respostaSecond == '2'):
            print("O rugido da criatura faz o chão vibrar.")

            time.sleep(1)
            print()
            print("Sem pensar duas vezes, você se vira e começa a correr pelo corredor escuro, tentando voltar pelo caminho de onde veio.")

            time.sleep(1)
            print()
            print("Mas você não enxerga nada.")

            time.sleep(1)
            print()
            print("Seus passos são desorientados, seu coração dispara, e o som da criatura atrás de você cresce rapidamente.")

            time.sleep(1)
            print()
            print("Ela é mais rápida.")

            time.sleep(1)
            print()
            print("Muito mais rápida.")

            time.sleep(1)
            print()
            print("Você sente um impacto violento nas suas costas antes mesmo de conseguir reagir.")
            print("Algo pesado o derruba no chão com brutalidade.")

            time.sleep(1)
            print()
            print("Garras gigantes se cravam em seu corpo, prendendo você contra o chão de pedra.")

            time.sleep(1)
            print()
            print("O rugido da criatura ecoa uma última vez nas catacumbas.")

            time.sleep(1)
            print()
            print("Depois disso, só resta silêncio.")

            time.sleep(1)
            print()
            print("Você morreu.")
            print("GAME OVER")
            print()
            exit()

        elif (respostaSecond == '3'):
            print("Quando você ouve a criatura avançando em sua direção, decide agir rápido.")

            time.sleep(1)
            print()
            print("No último instante, você se joga para o lado, tentando sair da trajetória daquilo que quer que esteja correndo contra você.")

            time.sleep(1)
            print()
            print("Por um breve momento, parece que funcionou.")

            time.sleep(1)
            print()
            print("A massa gigantesca da criatura passa por onde você estava um segundo antes.")

            time.sleep(1)
            print()
            print("Mas você esqueceu de uma coisa.")
            print("A criatura não é apenas grande.")
            print("Ela é longa.")

            time.sleep(1)
            print()
            print("Você sente algo chicotear violentamente na escuridão.")

            time.sleep(1)
            print()
            print("Uma dor absurda atravessa seu corpo quando algo afiado perfura suas costas.")
            print("A cauda da criatura, coberta por espinhos rígidos, atravessa seu corpo e o levanta do chão por um breve instante.")

            time.sleep(1)
            print()
            print("O ar abandona seus pulmões.")

            time.sleep(1)
            print()
            print("Então o mundo fica silencioso.")

            time.sleep(1)
            print()
            print("Seu corpo cai sem vida no chão frio das catacumbas.")
            print("Você morreu.")
            print("GAME OVER")
            print()
            exit()
        else:
            logout()

    elif (resposta == '3'):
        print("Você consegue rapidamente entender que está diante da sua provável morte.")
        print("Porém, mesmo que saber disso normalmente desesperaria uma pessoa comum, você utiliza isso como motivação manter a calma e segurar todo esse medo e agonia permeia sua mente.")
        print("Você se mantem calmo e estático na esperança da criatura aparentemente colossal não tenha lhe percebido e passe direto por você.")
        time.sleep(2)
        print("Você não pode vê-la nessa escuridão, mas o movimentar dela e seus grunhindos faz ser fácil perceber o quão aterrorizante é a criatura com que está lidando.")
        print("Você permanece completamente quieto, respirando o mais leve que você pode enquanto ouve a criatura se movimentando e passando por você")
        print("Você sente o cheiro podre de morte que você acredita vim da sua boca, responsável devorar diversos aventureiros.")
        time.sleep(3)
        print("Você, a partir dos seus sentidos, percebe que maior parte da criatura já passou pelo seu lado e está destanciando de você.")
        time.sleep(1)
        print("Você se sente aliviado, um alívio passageiro, pois você sente algo espinhoso arrastar na sua perna e rasgar sua carne, como se esse algo espinhoso fizesse parte da porção traseira da criatura.")
        time.sleep(1)
        print("Você grita de dor.")
        print("Você cai no chão.")
        print("Mas a dor agora é o menor do seus problemas.")
        print("Sua posição foi divulgada e você está no chão se contorcendo de dor.")
        print("Por um breve instante, tudo fica em silêncio.")
        time.sleep(3)
        print("Então você ouve.")
        time.sleep(1)
        print("A criatura para de se mover.")
        time.sleep(1)
        print("O som pesado de suas patas contra a pedra cessa completamente, como se o próprio tempo tivesse congelado.")
        time.sleep(1)
        print("O rosnado baixo que antes se afastava agora retorna, mais próximo… mais atento.")
        time.sleep(1)
        print("Ela percebeu você.")
        time.sleep(1)
        print("Você tenta se arrastar para trás, mas sua perna ferida mal responde.")
        time.sleep(1)
        print("O sangue escorre quente pela pedra fria enquanto o pânico finalmente toma conta da sua mente.")
        time.sleep(1)
        print("Na escuridão absoluta, você ouve o som da criatura se virando.")
        time.sleep(1)
        print("Passos pesados.")
        time.sleep(1)
        print("Lentos.")
        time.sleep(1)
        print("Deliberados.")
        time.sleep(1)
        print("Ela se aproxima novamente.")
        time.sleep(1)
        print("Você tenta erguer sua espada, mas antes que consiga reagir, algo enorme se lança sobre você.")
        time.sleep(1)
        print("O peso colossal da criatura o prende contra o chão.")
        time.sleep(1)
        print("Presas gigantes se fecham ao redor do seu torso.")
        time.sleep(1)
        print("Por um breve segundo, tudo que você sente é pressão.")
        time.sleep(1)
        print("Depois… nada.")
        print("As Catacumbas de Eldritch acabam de ganhar mais um cadáver esquecido.")
        print("Você morreu.")
        print("GAME OVER")
        print()
        exit()
    elif (resposta == '4'):
        print("O instinto de sobrevivência fala mais alto que qualquer plano racional.")
        time.sleep(1)
        print("O medo toma conta de você.")
        time.sleep(1)
        print("Mesmo tentando permanecer em silêncio, seu corpo começa a recuar lentamente para trás, passo por passo, tentando se afastar daquela presença monstruosa que se move pela escuridão.")
        time.sleep(1)
        print("Cada movimento é calculado.")
        time.sleep(1)
        print("Cada respiração é controlada.")
        time.sleep(1)
        print("Você tenta ser o mais silencioso possível.")
        time.sleep(1)
        print("Mas o pânico dentro da sua mente torna seus movimentos menos precisos do que você imagina.")
        time.sleep(1)
        print("Seu pé encontra algo no chão.")
        time.sleep(1)
        print("Algo irregular.")
        time.sleep(1)
        print("Algo que rola sob sua bota.")
        time.sleep(1)
        print("Antes que você possa reagir, seu equilíbrio se perde completamente.")
        time.sleep(1)
        print("Você cai.")
        time.sleep(1)
        print("Seu corpo bate contra o chão de pedra com um som seco que ecoa pelo corredor escuro.")
        time.sleep(1)
        print("Por um breve instante, você permanece imóvel no chão.")
        time.sleep(1)
        print("Seu coração dispara.")
        time.sleep(1)
        print("Agora você entende.")
        time.sleep(1)
        print("Acabou.")
        time.sleep(1)
        print("Seu corpo começa a tremer involuntariamente enquanto você tenta controlar a respiração.")
        time.sleep(1)
        print("Então você ouve.")
        time.sleep(1)
        print("A criatura para de se mover.")
        time.sleep(1)
        print("O silêncio que toma conta do corredor é ainda mais aterrorizante que os passos pesados de antes.")
        time.sleep(1)
        print("Ela percebeu você.")
        time.sleep(1)
        print("Lentamente, o som de garras raspando na pedra recomeça.")
        time.sleep(1)
        print("Passos pesados.")
        time.sleep(1)
        print("Firmes.")
        time.sleep(1)
        print("Diretamente na sua direção.")
        time.sleep(1)
        print("Você tenta se levantar, mas o medo paralisa seus músculos por um instante precioso demais.")
        time.sleep(1)
        print("De repente, algo enorme emerge da escuridão.")
        time.sleep(1)
        print("Você mal tem tempo de gritar.")
        time.sleep(1)
        print("Uma massa colossal colide contra seu corpo, esmagando você contra o chão.")
        time.sleep(1)
        print("Então tudo fica silencioso novamente.")
        print("Você morreu.")
        print("GAME OVER")
        print()
        exit()
    else:
        logout()

    return vida, beast_defeated

def beast_battle(vida: float, armor: bool):

    beast_defeated = 0

    print()
    print("O Leão Sombrio de Eldritch abaixa o corpo, preparando-se para avançar.")

    time.sleep(1)
    print()
    print("A tocha ilumina suas presas manchadas de sangue enquanto ele rosna profundamente.")
    print("Seus músculos se contraem como molas prestes a disparar.")

    time.sleep(2)
    print("Ele salta.")
    print("Você mal tem tempo de reagir.")

    time.sleep(2)
    print()
    print("O que você faz?")
    print()
    print("1- Atirar com a besta")
    print("2- Arremessar facas")
    print("3- Atacar com a espada\n")

    show_life(vida)
    resposta = input("> ")
    time.sleep(1)

    if (resposta == '1'):
        print("Você levanta rapidamente sua besta leve e dispara.")

        time.sleep(1)
        print()
        print("A flecha corta o ar e atinge o ombro da criatura.")

        time.sleep(1)
        print()
        print("O leão ruge de dor, mas não para.")

        time.sleep(1)
        print()
        print("Ele se choca contra você com brutalidade, derrubando você contra a parede de pedra.")

        vida, dano = random_damage(vida, armor)
        print(f'Você recebeu {dano} de dano')
        show_life(vida)
        print()

        print()
        print("Você consegue se levantar antes que ele ataque novamente.")

        time.sleep(2)
        print()
        print("O que você faz?")
        print()
        print("1- Atacar os olhos com a espada")
        print("2- Tentar manter distância")

        show_life(vida)
        resposta = input("> ")
        time.sleep(1)

        if (resposta == '1'):
            print("Você avança rapidamente.")

            time.sleep(1)
            print()
            print("O leão tenta mordê-lo, mas sua agilidade de ladino é maior.")

            time.sleep(1)
            print()
            print("Você desliza para o lado e crava sua espada diretamente em um dos olhos da criatura.")

            time.sleep(1)
            print()
            print("O rugido da fera ecoa por toda a catacumba.")
            
            time.sleep(1)
            print()
            print("Cega de um lado, a criatura se debate violentamente.")

            time.sleep(1)
            print()
            print("Ela consegue atingir você com uma de suas patas.")
            print("Que devido a sua agilidade na reação, causa apenas um corte não tão profundo na lateral da sua barriga")

            vida, dano = random_damage(vida, armor)
            print(f'Você recebeu {dano} de dano')
            show_life(vida)
            print()

            time.sleep(1)
            print("Mas agora ela está vulnerável.")

            time.sleep(2)
            print()
            print("O que você faz?")
            print()
            print("1- Tentar cortar sua garanta")
            print("2- Tentar cortar o tendão de sua pata dianteira\n")

            show_life(vida)
            resposta = input("> ")
            time.sleep(1)

            if (resposta == '1'):
                print("Você gira a espada e a crava profundamente no pescoço da criatura.")

                time.sleep(1)
                print()
                print("Porém, inicialmente, sua espada fica presa lateral esquerda do pescoço dela e você não consegue cortar sua garganta")

                time.sleep(1)
                print()
                print("Você é então respondido com um forte rugido devido a dor e a agonia que o Leão sente.")
                print("Rugido o qual precede a tentativa de morder violentamente a cabeça do ser responsável por essa ferida profunda, que se encontra vulnerável a sua frente segurando a espada presa.")

                time.sleep(2)
                print()
                print("Você não solta a espada.")
                print("Essa é uma chance única de derrotar a criatura e sobreviver aquilo.")

                time.sleep(2)
                print()
                print("Você desvia agilmente sua cabeça para o lado ainda segurando sua espada fincada no pescoço daquela monstruosidade.")

                time.sleep(1)
                print()
                print("As presas erram completamente sua cabeça, mas presas perfuram seu ombro esquerda com muita ferocidade, fazendo você deixar cair a tocha da mão esquerda.")
                vida, dano = random_damage(vida, armor)
                print(f'Você recebeu {dano} de dano')
                show_life(vida)
                print()

                time.sleep(1)
                print()
                print("Você grita, sangra e agoniza enquanto seu provável executor aplica mais força na mandibula.")
                vida, dano = random_damage(vida, armor)
                print(f'Você recebeu {dano} de dano')
                show_life(vida)
                print()

                time.sleep(1)
                print()
                print("Você usa toda essa dor e ciência da morte iminente para dar tudo que seu corpo tem a oferecer.")

                time.sleep(1)
                print()
                print("A mão esquerda nua agora segura sua espada juntamente com a direita, ambas aplicando força absurda contra a garganta da criatura que vai sendo cortada pouco a pouco")

                time.sleep(1)
                print()
                print("Você grita dando tudo de si e a criatura rosna enquanto aplica cada vez mais pressão no ombro que espirra sangue para todos os lados")
                vida, dano = random_damage(vida, armor)
                print(f'Você recebeu {dano} de dano')
                show_life(vida)
                print()

                time.sleep(2)
                print()
                print("Até que...")

                time.sleep(1)
                print()
                print("Sua lâmina atravessa toda a garganta da criatura, escorrendo uma quantidade exorbitante de sangue negro do pescoço da mesma")

                time.sleep(1)
                print()
                print("Sua mandíbula perde a força, sua patas não conseguem mais mantê-la de pé")

                time.sleep(1)
                print()
                print("Após alguns segundos de agonia, o Leão Sombrio de Eldritch cai morto.")

                time.sleep(1)
                print()
                print("Você respira fundo")

                time.sleep(1)
                print()
                print("A luta terminou")
                beast_defeated = 1

            elif (resposta == '2'):
                print("Você decide mirar na mobilidade da criatura.")

                time.sleep(1)
                print()
                print("Em vez de insistir na garganta protegida pela força monstruosa do leão, você gira rapidamente o corpo e mira sua lâmina na pata dianteira da criatura.")

                time.sleep(1)
                print()
                print("Sua espada corta profundamente atrás da articulação da pata.")

                time.sleep(1)
                print()
                print("O tendão se rompe.")

                time.sleep(1)
                print()
                print("O Leão Sombrio solta um rugido brutal enquanto sua pata falha e seu corpo colossal perde parte do equilíbrio.")

                time.sleep(1)
                print()
                print("Mas a criatura ainda está longe de derrotada.")

                time.sleep(1)
                print()
                print("Com um movimento violento, sua cauda espinhosa chicoteia o ar na sua direção.")

                time.sleep(1)
                print()
                print("Os espinhos rasgam seu torso antes que você consiga se afastar completamente.")

                vida, dano = random_damage(vida, armor)
                print(f'Você recebeu {dano} de dano')
                show_life(vida)
                print()

                time.sleep(1)
                print("O leão agora manca, mas continua extremamente perigoso.")
                print("Seu sangue negro escorre pela pedra enquanto ele se prepara para um último ataque.")

                time.sleep(2)
                print()
                print("O que você faz?")
                print()
                print("1- Saltar sobre a criatura e cravar a espada em seu pescoço")
                print("2- Disparar sua besta à queima-roupa\n")

                show_life(vida)
                resposta = input("> ")
                time.sleep(1)

                if (resposta == '1'):
                    print("Você decide acabar com aquilo de uma vez.")

                    time.sleep(1)
                    print()
                    print("Mesmo ferido, você avança contra a criatura manca.")

                    time.sleep(1)
                    print()
                    print("O leão tenta erguer a pata saudável para atingir você...")

                    time.sleep(1)
                    print()
                    print("Mas o peso do próprio corpo o trai.")

                    time.sleep(1)
                    print()
                    print("Você salta sobre o dorso da criatura e crava sua espada profundamente em seu pescoço.")

                    time.sleep(1)
                    print()
                    print("A lâmina atravessa músculos, carne e finalmente a garganta da fera.")

                    time.sleep(1)
                    print()
                    print("O Leão Sombrio ruge uma última vez.")

                    time.sleep(1)
                    print()
                    print("Seu corpo gigantesco se debate violentamente por alguns segundos.")

                    time.sleep(1)
                    print()
                    print("Então ele desaba pesadamente no chão de pedra.")

                    time.sleep(1)
                    print()
                    print("O predador das Catacumbas de Eldritch finalmente está morto.")

                    beast_defeated = 1
                elif (resposta == '2'):
                    print("Você rapidamente larga a pressão da luta corpo a corpo.")

                    time.sleep(1)
                    print()
                    print("Com movimentos rápidos, você puxa sua besta leve das costas.")

                    time.sleep(1)
                    print()
                    print("O leão manca na sua direção, preparando um último salto.")

                    time.sleep(1)
                    print()
                    print("Mas ele está lento demais.")

                    time.sleep(1)
                    print()
                    print("Você aponta a besta diretamente para a cabeça da criatura.")

                    time.sleep(1)
                    print()
                    print("E dispara.")

                    time.sleep(1)
                    print()
                    print("A flecha atravessa o olho restante da fera e penetra profundamente em seu crânio.")

                    time.sleep(1)
                    print()
                    print("O rugido que sai da criatura é curto.")

                    time.sleep(1)
                    print()
                    print("Seu corpo colossal perde a força e cai pesadamente no chão.")

                    time.sleep(1)
                    print()
                    print("O Leão Sombrio de Eldritch não se move mais.")

                    beast_defeated = 1
                else:
                    logout()
            else:
                logout()

        elif (resposta == '2'):
            print("Você decide não se aproximar daquela monstruosidade.")

            time.sleep(1)
            print()
            print("Em vez disso, começa a recuar lentamente enquanto mantém a espada pronta.")

            time.sleep(1)
            print()
            print("O Leão Sombrio rosna profundamente e começa a circular você.")

            time.sleep(1)
            print()
            print("Seus olhos vermelhos acompanham cada movimento seu.")

            time.sleep(1)
            print()
            print("De repente ele salta.")

            time.sleep(1)
            print()
            print("Você tenta recuar, mas uma de suas garras alcança seu peito.")

            vida, dano = random_damage(vida, armor)
            print(f'Você recebeu {dano} de dano')
            show_life(vida)

            print()
            time.sleep(1)
            print("Você consegue manter alguma distância novamente.")

            time.sleep(2)
            print()
            print("O que você faz?")
            print()
            print("1- Sacar sua besta")
            print("2- Esperar o ataque para contra-atacar\n")

            show_life(vida)
            resposta = input("> ")
            time.sleep(1)

            if (resposta == '1'):
                print("Você rapidamente puxa sua besta das costas.")

                time.sleep(1)
                print()
                print("O leão avança novamente.")

                time.sleep(1)
                print()
                print("Você dispara.")

                time.sleep(1)
                print()
                print("A flecha atinge o peito da criatura.")

                time.sleep(1)
                print()
                print("Mas ele ainda alcança você.")

                vida, dano = random_damage(vida, armor)
                print(f'Você recebeu {dano} de dano')
                show_life(vida)

                time.sleep(1)
                print()
                print("A criatura está ferida, mas ainda luta.")

                time.sleep(2)
                print()
                print("O que você faz?")
                print()
                print("1- Finalizar com espada")
                print("2- Usar a tocha novamente\n")

                show_life(vida)
                resposta = input("> ")
                time.sleep(1)

                if (resposta == '1'):
                    print("Você avança antes que a criatura recupere o equilíbrio.")

                    time.sleep(1)
                    print()
                    print("Sua espada corta profundamente o pescoço da fera.")

                    time.sleep(1)
                    print()
                    print("O sangue negro jorra pelo chão de pedra.")

                    time.sleep(1)
                    print()
                    print("O Leão Sombrio tenta dar mais um passo...")

                    time.sleep(1)
                    print()
                    print("Mas cai morto.")

                    beast_defeated = 1
                elif (resposta == '2'):
                    print("Você rapidamente pega a tocha que havia deixado cair.")

                    time.sleep(1)
                    print()
                    print("A criatura manca levemente por causa da flecha cravada em seu peito, mas ainda avança com ferocidade.")

                    time.sleep(1)
                    print()
                    print("Quando o Leão Sombrio se aproxima novamente, você ergue a tocha diante do rosto da criatura.")

                    time.sleep(1)
                    print()
                    print("As chamas iluminam suas presas ensanguentadas e os olhos vermelhos que agora encaram diretamente você.")

                    time.sleep(1)
                    print()
                    print("O fogo toca sua pelagem negra.")

                    time.sleep(1)
                    print()
                    print("A criatura solta um rugido furioso e recua um pouco, claramente incomodada com as chamas.")

                    time.sleep(1)
                    print()
                    print("Mas isso não dura muito.")

                    time.sleep(1)
                    print()
                    print("Com um movimento violento, a cauda espinhosa chicoteia o ar.")

                    vida, dano = random_damage(vida, armor)
                    print(f'Você recebeu {dano} de dano')
                    show_life(vida)

                    time.sleep(1)
                    print()
                    print("Os espinhos rasgam seu braço e quase fazem você largar a tocha novamente.")

                    time.sleep(2)
                    print()
                    print("A criatura agora parece mais cautelosa... mas ainda mortal.")

                    time.sleep(2)
                    print()
                    print("O que você faz?")
                    print()
                    print("1- Avançar com a espada enquanto ela hesita")
                    print("2- Sacar a besta novamente e tentar um disparo final\n")

                    show_life(vida)
                    resposta = input("> ")
                    time.sleep(1)

                    if (resposta == '1'):
                        print("Você decide aproveitar a hesitação da criatura.")

                        time.sleep(1)
                        print()
                        print("Com um grito, você avança contra o Leão Sombrio.")

                        time.sleep(1)
                        print()
                        print("Sua espada atravessa profundamente o pescoço da fera.")

                        time.sleep(1)
                        print()
                        print("O sangue negro escorre violentamente sobre o chão de pedra.")

                        time.sleep(1)
                        print()
                        print("A criatura tenta rugir novamente...")

                        time.sleep(1)
                        print()
                        print("Mas apenas um som abafado sai de sua garganta destruída.")

                        time.sleep(1)
                        print()
                        print("O corpo colossal da criatura treme por alguns segundos.")

                        time.sleep(1)
                        print()
                        print("Então desaba pesadamente no chão.")

                        time.sleep(1)
                        print()
                        print("O Leão Sombrio de Eldritch está morto.")

                        beast_defeated = 1
                    elif (resposta == '2'):
                        print("Mesmo ferido, você decide confiar novamente em sua pontaria.")

                        time.sleep(1)
                        print()
                        print("Você rapidamente puxa a besta das costas.")

                        time.sleep(1)
                        print()
                        print("O leão percebe o movimento e avança mais uma vez.")

                        time.sleep(1)
                        print()
                        print("Você aponta a arma diretamente para a cabeça da criatura.")

                        time.sleep(1)
                        print()
                        print("E dispara.")

                        time.sleep(1)
                        print()
                        print("A flecha atravessa o olho restante da criatura.")

                        time.sleep(1)
                        print()
                        print("O rugido que ecoa pelas catacumbas é curto.")

                        time.sleep(1)
                        print()
                        print("A força abandona o corpo gigantesco da fera.")

                        time.sleep(1)
                        print()
                        print("O Leão Sombrio de Eldritch cai morto diante de você.")

                        beast_defeated = 1
                    else:
                        logout()
                else:
                    logout()
            elif (resposta == '2'):
                print("Você firma os pés no chão de pedra.")

                time.sleep(1)
                print()
                print("Em vez de atacar, você apenas observa.")

                time.sleep(1)
                print()
                print("O Leão Sombrio rosna baixo, desconfiado.")

                time.sleep(1)
                print()
                print("Seus olhos vermelhos brilham na escuridão enquanto ele começa a rodear você novamente.")

                time.sleep(1)
                print()
                print("Então, sem aviso, ele salta.")

                time.sleep(1)
                print()
                print("Você espera até o último segundo.")

                time.sleep(1)
                print()
                print("As garras passam raspando por você...")

                vida, dano = random_damage(vida, armor)
                print(f'Você recebeu {dano} de dano')
                show_life(vida)

                time.sleep(1)
                print()
                print("Mas a criatura se expõe completamente no ataque.")

                time.sleep(1)
                print()
                print("Essa é a sua chance.")

                time.sleep(2)
                print()
                print("O que você faz?")
                print()
                print("1- Cravar a espada no peito da criatura")
                print("2- Rolar para o lado e atacar o pescoço\n")

                show_life(vida)
                resposta = input("> ")
                time.sleep(1)

                if (resposta == '1'):
                    print("Você segura firme sua espada.")

                    time.sleep(1)
                    print()
                    print("Quando o peso da criatura cai sobre você...")

                    time.sleep(1)
                    print()
                    print("Você empurra a lâmina diretamente para frente.")

                    time.sleep(1)
                    print()
                    print("A espada atravessa profundamente o peito da fera.")

                    time.sleep(1)
                    print()
                    print("O rugido que ecoa pelas catacumbas é curto e violento.")

                    time.sleep(1)
                    print()
                    print("O Leão Sombrio tenta se levantar...")

                    time.sleep(1)
                    print()
                    print("Mas suas forças desaparecem.")

                    time.sleep(1)
                    print()
                    print("A criatura cai morta sobre o chão de pedra.")

                    beast_defeated = 1

                elif (resposta == '2'):
                    print("No último segundo você se joga para o lado.")

                    time.sleep(1)
                    print()
                    print("O corpo colossal da criatura passa por você.")

                    time.sleep(1)
                    print()
                    print("Antes que ela consiga se virar...")

                    time.sleep(1)
                    print()
                    print("Sua espada corta profundamente o pescoço da fera.")

                    time.sleep(1)
                    print()
                    print("Sangue negro se espalha pelo chão.")

                    time.sleep(1)
                    print()
                    print("O Leão Sombrio tenta rugir mais uma vez...")

                    time.sleep(1)
                    print()
                    print("Mas apenas um som fraco escapa de sua garganta.")

                    time.sleep(1)
                    print()
                    print("Então o monstro desaba, morto.")

                    beast_defeated = 1
                else:
                    logout()
            else:
                logout()
        else:
            logout()
    elif (resposta == '2'):
        print("Você puxa rapidamente uma de suas facas.")

        time.sleep(1)
        print()
        print("E a arremessa contra a criatura.")

        time.sleep(1)
        print()
        print("A lâmina gira no ar.")

        time.sleep(1)
        print()
        print("E atinge o flanco do Leão Sombrio.")

        time.sleep(1)
        print()
        print("A reação é imediata.")

        time.sleep(1)
        print()
        print("A criatura ruge com uma fúria brutal.")

        time.sleep(1)
        print()
        print("Então dispara na sua direção.")

        time.sleep(1)
        print()
        print("Você entende na mesma hora.")

        time.sleep(1)
        print()
        print("Não dá para vencer aquilo aqui.")

        time.sleep(1)
        print()
        print("Você corre.")

        time.sleep(1)
        print()
        print("Os corredores das catacumbas passam borrados ao seu redor.")

        time.sleep(1)
        print()
        print("Atrás de você, o som das patas da criatura se aproxima.")

        time.sleep(1)
        print()
        print("Cada rugido parece mais perto.")

        time.sleep(1)
        print()
        print("Uma garra gigantesca raspa a parede ao seu lado.")

        time.sleep(1)
        print()
        print("Pedras se quebram e caem no chão.")

        time.sleep(1)
        print()
        print("Você mergulha por uma passagem estreita entre duas colunas de pedra.")

        time.sleep(1)
        print()
        print("O corpo enorme da criatura tenta seguir...")

        time.sleep(1)
        print()
        print("Mas fica preso por um instante.")

        time.sleep(1)
        print()
        print("Esse instante é o suficiente.")

        time.sleep(1)
        print()
        print("Você continua correndo até o som do monstro desaparecer na escuridão.")

        time.sleep(2)
        print()
        print("Você escapou da criatura e preservou sua vida.")

        beast_defeated = 0
    elif (resposta == '3'):
        print("Com um grito, você avança contra a criatura.")

        time.sleep(1)
        print()
        print("Sua espada corta o ar das catacumbas.")

        time.sleep(1)
        print()
        print("Mas o Leão Sombrio é mais rápido do que você imaginava.")

        time.sleep(1)
        print()
        print("A criatura desvia com um movimento brutal.")

        time.sleep(1)
        print()
        print("Antes que você consiga recuar, uma garra enorme atinge seu ombro.")

        vida, dano = random_damage(vida, armor)
        print(f'Você recebeu {dano} de dano')
        show_life(vida)

        time.sleep(1)
        print()
        print("A força do golpe quase faz você cair.")

        time.sleep(1)
        print()
        print("Agora, de perto...")

        time.sleep(1)
        print()
        print("Você percebe o tamanho real da criatura.")

        time.sleep(1)
        print()
        print("Músculos enormes.")
        
        time.sleep(1)
        print()
        print("Presas maiores que sua mão.")

        time.sleep(1)
        print()
        print("E aqueles olhos vermelhos fixos em você.")

        time.sleep(1)
        print()
        print("Você entende uma coisa imediatamente.")

        time.sleep(1)
        print()
        print("Não dá para vencer isso aqui.")

        time.sleep(1)
        print()
        print("A criatura ruge e avança novamente.")

        time.sleep(1)
        print()
        print("Você se vira e começa a correr pelos túneis das catacumbas.")

        time.sleep(1)
        print()
        print("Atrás de você, o som das patas pesadas ecoa pela pedra.")

        time.sleep(1)
        print()
        print("Cada passo da criatura faz o chão tremer.")

        time.sleep(1)
        print()
        print("Você vira um corredor estreito quase escorregando no chão úmido.")

        time.sleep(1)
        print()
        print("O rugido da fera ecoa logo atrás.")

        time.sleep(1)
        print()
        print("Mas então você encontra uma passagem estreita entre duas colunas quebradas.")

        time.sleep(1)
        print()
        print("Você passa por ela correndo.")

        time.sleep(1)
        print()
        print("O corpo gigantesco do Leão Sombrio tenta seguir...")

        time.sleep(1)
        print()
        print("Mas não consegue passar.")

        time.sleep(1)
        print()
        print("O rugido furioso da criatura ecoa pelas catacumbas enquanto você se afasta.")

        time.sleep(2)
        print()
        print("Você conseguiu escapar.")

        beast_defeated = 0
    else:
        logout()

    return vida, beast_defeated
