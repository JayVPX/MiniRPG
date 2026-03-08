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
    
    return vida
    

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

    if (resposta == '1'):
        print()
        print("Você agacha e examina no que você está em pisando.")
        print("Um questionamento que antes era sobre \"onde você está pisando?\", se torna sobre \"em quem você pisando?\".")
        print("Você está em cima de um cadáver morto, cheio de marcas de garras sangrando pelo corpo.")
        print("Você não consegue conter o susto que você tomou a ver essa cena pesada.")
        print("Seu susto acordou algo, algo com passos pesados, bufando como uma fera, mas impossível de identificar naquela escuridão.")
        vida = beast_encounter(vida, armor)
    elif (resposta == '2'):
        print()
        print("Você ignora complementamente sobre o que você está pisando e se mantém focado em prosseguir cautelosamente enquanto se escora pela parede daquilo que parece ser um corredor bem extenso.")
        print("Você caminha pacientemente através daquela escuridão, até encontrar o que parece ser o fim daquele corredor silencioso e vazio.")
        print("Você encontra numa sala iluminada.")
    else:
        logout()
    
    return vida

## Encontro com a monstruosidade
def beast_encounter(vida: float, armor: bool):

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
        vida = beast_battle(vida, armor)
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

    return vida

def beast_battle(vida: float, armor: bool):
    return vida
