from utils import *
import time

## Chegando na Torre
def mage_start(vida: float, armor: bool):
    time.sleep(2)
    print()
    print("Após alguns segundos, um pequeno roedor surgiu das ruínas.")
    print("Mas você percebe que algo está estranho, seus olhos brilham em azul arcano e pequenas faíscas mágicas saem de seu corpo.")
    print("Um Rato Arcano bloqueia o seu caminho.\n")
  
    time.sleep(2)

    print("O que você faz?")
    print()
    print("1- Lança um feitiço simples no rato.")
    print("2- Observar a criatura antes de atacar. ")
    print("3- Afugentar o rato com magia.")
    print("4- Fugir.\n")
   
    show_life(vida)
    resposta = input("> ")
    time.sleep(1)

    if (resposta == '1'):
        print()
        print('Reunindo sua mana e se concentrando rapidamente, você forma seu feitiço de Faísca Arcana, e lança em direção ao rato.')
        print("A magia atinge o rato com sucesso e ele é eliminado.")
        print("O caminho para a entrada principal, está liberada e você entra.")
        time.sleep(2)
        
    elif(resposta == '2'):
        print()
        print('Ao examinar o ambiente ao redor, você percebe que há outros ratos que estavam nas ruínas, dormindo.')
        print('Porém do mesmo jeito que você percebeu, eles perceberam a sua presença também.')
        print('Agora são 3 Ratos Arcanos.')
        print()
        time.sleep(2)

        print("O que você vai fazer?\n")
       
        print("1- Lutar contra os ratos.")
        print("2- Fugir.\n")

        show_life(vida)

        resposta = input("> ")
        time.sleep(1)

        if(resposta=='1'):
            vida, dano = random_damage(vida, armor)
            print()
            print("Você luta bravamente contra o trio de ratos, os eliminando, mas você foi ferido: ")
            print(f'Você recebeu {dano} de dano')

            show_life(vida)
            print()
        
        elif(resposta== '2'):
            print()
            print("Você se amedronta com o trio de ratos famintos marchando em sua direção.")
            print("Você foge da torre, com sucesso.")
            print("Tudo bem, ninguém irá lhe julgar, magos não são conhecidos exatamente pela coragem...")
            print("GAME OVER")
            print()
            exit()
        else:
           logout()

    elif(resposta== '3'):
        print()
        print("Reunindo sua mana e se concentrando rapidamente, você forma seu feitiço de Faísca Arcana e lança em direção ao rato.")
        print("A magia atinge ao lado do rato. Afugentando-o com sucesso.")
        print("O caminho para a entrada principal, está liberada e você entra.")
        print()

    elif (resposta =='4'):
        print()
        print("Você se amedronta com a esquerosidade do rato arcano.")
        print("Você foge da torre, com sucesso.")
        print("Tudo bem, ninguém irá lhe julgar, magos não são conhecidos exatamente pela coragem...")
        print("GAME OVER")
        print()
        exit()
    else:
        logout()

    return vida

## Entrada na Torre
def mage_tower_entrance(vida: float, armor: bool):
    print()
    print("Ao entrar na magnifíca torre, você se depara com uma pequena sala com um corredor meio que instável")
    print("Vendo que esse era o único caminho, você não tem outra escolha, a não ser adentrar no corredor.")
    print("Runas antigas brilham no chão e você ouve sussurros ao seu redor, quase como se fosse uma interferência no ar causada pela mana.\n")

    time.sleep(2)
   
    print("O que você deseja fazer?\n")
    

    print("1- Avançar cautelosamente pelo corredor.")
    print("2- Tentar decifrar as runas no chão.")
    print("3- Voltar e observar melhor a entrada.\n")
   
    show_life(vida)

    reposta = input("> ")
    time.sleep(1)


    # Avançar no corredor
    if (reposta == '1'):
        print()
        print("Você então avança pelo corredor mal iluminado, o clima sombrio de sussurros ainda paira pelo ar.")
        print("Mas você avança com cautela, temendo que algo possa acontecer.")
        print('E acontece...')
        print("Ao chegar na metade do corredor, um círculo mágico com um brilho cegante surge ao seu redor, rápido porém o bastante para te deixar desnorteado.")
        print("Você então entende o que aqueles sussurros eram...\n")
        time.sleep(2)

        print("Diante de você, surge uma forma fantasmagórica, parecendo nascer no meio da névoa com a escuridão daquele corredor.")
        print("Um Espectro apareceu...\n")
        time.sleep(2)

        print("Seus olhos brilham com energia sombria.")
        print("E aproveitando seu curto momento de distração ocasionado pela cegueira momentânea, ele te ataca.\n")


        vida, dano = random_damage(vida, armor)

        print(f'Você recebeu {dano} de dano')
        show_life(vida)

        time.sleep(2)
        print()

        print('O que você deseja fazer?\n')
        
        print("1- Atacar com feitiço médio.")
        print("2- Fugir.\n")
        show_life(vida)


        respostaSecond = input("> ")
        time.sleep(1)
        
        if(respostaSecond == '1'):
            print("Você se distancia do Espectro o mais rápido que pode e começa a se concentrar para lançar seu feitiço de nível médio: Raio Arcano.")
            print("Você e o Espectro trocam golpes e feitiços...")
            print("Você vê o espectro se esvaindo, enquanto as névoas crepitantes se dissipam lentamente no ar.")
            print("O Especto morreu, porém você também recebeu danos\n")
            time.sleep(2)
            vida, dano = random_damage(vida, armor)
            print(f'Você recebeu {dano} de dano')
            show_life(vida)
            
            print()
            print("Seu caminho pelo corredor agora está liberado, nenhum perigo o espreita mais...\n")
        elif(respostaSecond == '2'):
            print("Você se aterroriza com a presença do Espectro.")
            print("Você foge da torre, com sucesso.")
            print("Tudo bem, ninguém irá lhe julgar, magos não são conhecidos exatamente pela coragem...")
            print("GAME OVER")
            print()
            exit()  
       
        else: 
            logout()
    # Decifrar runas
    elif (reposta == '2'):
        print()
        print("Você se agacha, para ler em as runas brilhantes mas antigas que se encontram na entrada do corredor.")
        print("Apesar de serem arcaícas, você ainda consegue entender...")
        print("Aquelas runas continham um aviso.")
        print("Há uma armadilha mágica que invocará um Espectro no corredor.")
        print("Você entendeu que aquelas runas funcionavam como um interruptor mágico.\n")
        time.sleep(2)

        print("Com o seu conhecimento arcano, você consegue desabilitar a armadilha mágica através das runas.")
        print("Seu caminho pelo corredor agora está liberado, nenhum perigo o espreita mais...\n")
    #  Voltar e observar a entrada principal
    elif (reposta == '3'):
        print()
        print("Com todo o ar sombrio que perdura no ambiente daquele corredor, você se vê receoso de o atravessar.")
        print("Você então decide, voltar para a entrada principal, para ver se deixou algo importante para trás.\n")
        time.sleep(2)

        print("Ao chegar na sala da entrada, você começa a investigar os arredores em busca de algo que você deixou passar.")
        print("Ao encarar uma das paredes, você percebe um acúmulo de mana nessa área específica.")
        print("Mesmo sendo um aprendiz você ainda é um mago, rapidamente você percebe que aquilo se trata de uma magia de ilusão.")
        print("Sabendo disso, você logo utiliza seu feitiço: Dispersar, para remover a ilusão.\n")
        time.sleep(2)

        print('A parede ilusória desaparece, abrindo um caminho para uma sala iluminada, totalmente diferente do corredor anterior.\n')

        time.sleep(2)
        print("O que você vai fazer? \n")
        print("1- Entrar na sala")
        print("2- Ir embora.\n")

        show_life(vida)
   
        respostaSecond = input("> ")
        time.sleep(1)

        if(respostaSecond == '1'):
            print('Talvez a luz tenha te dado confiança, você entra na sala sem medo.')
        elif(respostaSecond=='2'):
            print("Você sente que a missão está muito além da sua capacidade.")
            print("Você foge da torre, com sucesso.")
            print("Tudo bem, ninguém irá lhe julgar, magos não são conhecidos exatamente pela coragem...")
            print("GAME OVER")
            print()
            exit()  
        else:
            logout()
    # Logout
    else: 
        logout()

  
    return vida, reposta

## Caminhos decididos pelo Segundo Round

# Caminho da Biblioteca
def mage_library(vida: float, armor: bool):

    time.sleep(2)
    print()
    print("Após atravessar o corredor, você chega a uma enorme biblioteca antiga.\n")
    time.sleep(2)
    print("O teto é alto e desaparece na escuridão, sustentado por colunas de pedra cobertas por runas desgastadas.")
    print("Estantes gigantescas se estendem em todas as direções, repletas de livros antigos e pergaminhos empoeirados.")
    print("Alguns livros parecem vibrar levemente, como se ainda estivessem carregados de magia.\n")
    time.sleep(2)
    print("No centro da sala há um altar de pedra.")
    print("Sobre ele repousam dois livros.\n")
    time.sleep(2)
    print("Um possui uma capa azul profunda, com símbolos arcanos gravados em prata.")
    print("O outro possui uma capa vermelha escura, com runas que parecem pulsar lentamente.\n")
    time.sleep(2)
    print("A biblioteca parece silenciosa... silenciosa demais.")
    print("Você então se aproxima do altar, e encara os dois livros\n")

    time.sleep(2)
    print("O que você vai fazer?\n")

    print("1- Abrir o livro da capa azul.")
    print("2- Abrir o livro da capa vermelho.")
    print("3- Explorar a biblioteca.\n")

    show_life(vida)

    resposta = input("> ")
    time.sleep(1)

    # Abrir Livro Azul
    if (resposta == '1'):
        print("Com certo receio, você então aproxima sua mão ao livro de azul...")
        print("O silêncio anormal da biblioteca, faz você ouvir seus batimentos e respiração tão altos, como se fosse música na taverna mais animada de Valtherra.\n")
      
        print("Ao abrir o livro azul, as runas presentes dentro começam a queimar com a energia arcana.")
        print("E então, o tão ansioso silêncio foi substituído.")
        print("O Altar começa a tremer, rangendo como uma máquina que a muito não encontra um óleo.\n")
        
        print("Ao seu redor você começa a ver vultos se movendo das velhas estandes de livro")
        print("Brevemente, com várias brilhando em cores diversas.\n")
        
        print("Sem muita surpresa você entendeu... Era uma armadilha")
        print("Os vultos eram Livros Amaldiçoados, vários deles...\n")

        print("Entretanto no meio do caos luminoso dos livros, você percebe, que em uma das estandes, uma passagem foi aberta.")
        print("Você percebe, que não consegue correr diretamente para a entrada recém aberta, pois os livros estão sob ela.\n")

        time.sleep(3)
        print("O que você vai fazer?\n")
        
        print("1- Lançar uma explosão arcana ao seu redor para destruir os livros")
        print("2- Usar magia arcana para empurrar os livros.")
        print("3- Fugir\n")

        show_life(vida)

        respostaLibrary = input('> ')
        time.sleep(1)
        
        if(respostaLibrary == '1'):
            print()
            print("Em meio ao caos, você fecha os olhos e se concentra no seu feitiço.")
            print("Você ergue a mão ergue sua mão, concentrando mana nela, soltando sua magia: Explosão Arcana")
            print("Em um piscar de olhos, irrompe uma explosão ao seu redor.\n")
            time.sleep(2)

            print("Vários livros são destruídos, mas alguns ainda se mantém intactos.")
            print("Você então percebe uma chance de correr até a saída em meio as estandes.")
            print("Sem pensar duas vezes, você aproveita essa chance e corre até a passagem.")
            print("Mas nada é fácil no mundo, enquanto você atravessava pelo grupo de livros remanescentes, alguns deles te atacam\n")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano")
            show_life(vida)

            print()
            print("Você cruza a entrada, e percebe que os livros não te seguiram.")
            print('Aliviado, você respira fundo, recuperando um pouco do fôlego.\n')
        
        elif(respostaLibrary =='2'):
            print()
            print("Em meio ao caos, você fecha os olhos e se concentra no seu feitiço.")
            print("Você ergue a mão ergue sua mão, concentrando mana nela, soltando sua magia: Impulsão Arcana")
            print("Em um piscar de olhos, você lança da sua mão uma onda de energia roxa.\n")
            time.sleep(2)

            print("Os livros que voavam na sua direção, foram empurrados para a parede")
            print("Você então percebe uma chance de correr até a saída em meio as estandes.")
            print("Sem pensar duas vezes, você aproveita essa chance e corre até a passagem.\n")
            time.sleep(2)
            print("Você cruza a entrada, e percebe que os livros não te seguiram.")
            print('Aliviado, você respira fundo, recuperando um pouco do fôlego.\n')

        elif(respostaLibrary =='3'):    
            print()
            print("Você tem fobia de livros voadores.")
            print("Você sai correndo por onde você veio.")
            print("Tudo bem, ninguém irá lhe julgar, magos não são conhecidos exatamente pela coragem...")
            print("GAME OVER")
            exit()
        else:
            logout()
  
    # Abrir Livro Vermelho
    elif (resposta == '2'):
        print("Com certo receio, você então aproxima sua mão ao livro de vermelho...")
        print("O silêncio anormal da biblioteca, faz você ouvir seus batimentos e respiração tão altos, como se fosse música na taverna mais animada de Valtherra.\n")
        time.sleep(2)

        print("Ao abrir o livro vermelho, as runas presentes dentro começam a brilhar de forma hipnotizante, as páginas começam a passar sozinhas em alta velocidade")
        print("Você entra em um estado de transe.")
        print("Ao seu redor, no chão, surge um círculo mágico, o brilho presente no livro, passa através do seu corpo, como se estivessem se fundindo a você.\n")
        time.sleep(2)
        
        print("Você recobra a consciência, o sentimento ocasionado por aquele livro ainda é desconhecido.")
        print("Você se sente como se estivesse ficado inconsciente por vários minutos, ou talvez até horas, mas ao mesmo tempo, sente como se tudo aquilo tivesse passado como um flash de luz.")
        print("Com certeza, uma sensação ambígua de se sentir...\n")
        time.sleep(2)

        print("Entretante, mesmo em confusão, algo é certo.")
        print("Você se sente um vigor extraordinário passando por suas véias, seu corpo parece mais robusto, você acredita que pode resistir até a um atropelamento de um Minotauro.")
        print("Você nunca passou por isso, mas tem certeza, aquele livro lhe encantou com um feitiço de Resistência.")
        print("Agora, você deve tomar menos dano dos inimigos.\n")
        time.sleep(2)

        print("Antes que possa comemorar sobre essa dádiva, você percebe que uma porta se abriu entre as estandes de livro.")
        print("O feitiço aumentou não só sua resistência, mas também sua confiança. Você atravessa a passagem sem medo.\n")

        armor = True
        return vida, armor 
    
    # Explorar a biblioteca
    elif(resposta=='3'):
        print('Com medo do que pode lhe acontecer ao tocar nos livros presentes no altar.')
        print("Você decide investigar um pouco a biblioteca.")
        print("Nada parece fora do esperado...\n")
        time.sleep(2)
        print("Cadeiras e mesas desgastadas com o tempo e os cupins.")
        print("Poeira e teias de aranha presentes aonde quer que fosse direcionado o olhar.")
        print("Livros sejam nas estandes ou no chão, desgastados, as capas já perecidas com o tempo, a cor das folhas semelhantes ao chão, denunciavam a idade daqueles livros.")
        print("Nada fora do comum, afinal a torre já estava abandonada a décadas.\n")

        time.sleep(2)

        print("Você continua caminhando pela biblioteca, seu olhar curioso vaga pelas estandes, o único som do ambiente que pode ser ouvido são seus passos.")
        print("Até que algo curioso chama a atenção dos seus olhos...")
        print("Uma estande. Na verdade não a estande em si, mas um livro que fazia parte dela.")
        print("No meio de todos os livros velhos e desgastados da estande, havia um que parecia novo.")
        print("A capa tinha mostrava uma cor verde viva, as folhas poderiam ser comparado ao leite de tão branco.")
        print("Você acredita que poderia sentir até aquele cheiro de produto novo exalando daquele livro\n")
        time.sleep(2)

        print("Com curiosidade, você não exita em alcançar esse livro e removê-lo da estande.")
        print("Ao abrir, o livro apenas desapareceu, como se tudo aquilo tivesse sido uma ilusão.")
        print("Você percebe que o livro voltou para o lugar de onde foi retirado.")
        print("Porém nem tempo de pensar você teve. Um ruído começa a ser emitido da estande, e em poucos segundos, uma abertura se faz entre ela. Uma saída daquela biblioteca.")
        print("Você nem pensa duas vezes e atravessa aquela entrada, saindo daquela biblioteca e avançado mais uma vez, chegando cada vez mais perto do final da torre.\n")
       

    else:
        logout()



    return vida, armor

# Caminho do Laboratório
def mage_laboratory(vida: float, armor: bool):
   
    time.sleep(3)
    print('Você adentra nessa sala secreta da torre.')
    print("O cheiro forte de ervas queimadas e reagentes alquímicos invade suas narinas imediatamente.\n")
    time.sleep(2)
   
    print("Este lugar parece ser um antigo laboratório arcano.")
    print("Mesas de pedra ocupam boa parte da sala, cobertas por frascos, tubos de vidro e instrumentos alquímicos.")
    print("Alguns recipientes ainda borbulham lentamente com líquidos de cores estranhas.")
    print("Uma luz esverdeada ilumina o ambiente, vindo de um grande recipiente cheio de algum tipo de substância mágica.\n")
    time.sleep(2)
   
    print("Ao redor das paredes, várias estantes estão abarrotadas de objetos curiosos.")
    print("Pequenos artefatos mágicos, pergaminhos enrolados e bugigangas arcanas acumulam poeira após anos de abandono.")
    print("Apesar do laboratório parecer antigo, parte dos equipamentos ainda parece funcionar.")
    print("Como se alguém... ou algo... ainda mantivesse este lugar ativo.\n")

  
    time.sleep(2)
    print("O que você deseja fazer?\n")

    print("1- Vasculhar as estantes de bugigangas mágicas.")
    print("2- Vasculhar as mesas de alquimia.")
    
    show_life(vida)

    resposta = input("> ")
    time.sleep(1)

    if(resposta =='1'):
        print()
        print("Você caminha lentamente até as estantes cobertas de poeira.")
        print("Os artefatos mágicos vibram levemente quando você passa a mão por eles.")
        print("Alguns pergaminhos se desfazem ao toque, como se o tempo finalmente cobrasse seu preço.\n")

        time.sleep(2)

        print("Entre amuletos quebrados e frascos vazios, algo chama sua atenção.")
        print("Uma pequena esfera metálica repousa dentro de um suporte de madeira.")
        print("Runas antigas estão gravadas em sua superfície, brilhando fracamente.\n")

        time.sleep(2)

        print("Quando você a pega, as runas se iluminam por um instante.")
        print("Você reconhece o artefato: uma bomba mágica.")
        print("Se ativada, ela libera uma explosão arcana devastadora.\n")

        print("Você cuidadosamente guarda a bomba em sua mochila.")
        
        vida, armor = mage_miniBoss(vida,armor)

    elif(resposta =='2'):
        print()
        print("Você se aproxima das mesas de alquimia.")
        print("Frascos borbulham lentamente, espalhando vapores coloridos pelo ar.")
        print("O cheiro é forte, uma mistura de ervas, enxofre e algo metálico.\n")

        time.sleep(2)

        print("Entre tubos de vidro e instrumentos alquímicos, você encontra um pequeno frasco intacto.")
        print("Dentro dele há um líquido azul profundo que pulsa suavemente com energia mágica.\n")

        time.sleep(2)

        print("Um rótulo antigo quase ilegível diz:")
        print("'Elixir de Resistência Arcana'.\n")

        print("Você bebe a poção. Um calor percorre seu corpo.")
        print("Sua pele parece mais rígida, como se uma proteção invisível envolvesse você.\n")

        print("Sua resistência aumentou.")
        armor = True
        vida, armor = mage_miniBoss(vida, armor)

    else:
        logout()
      
    return vida, armor

#MiniBoss do Laboratório
def mage_miniBoss(vida: float, armor: bool):
    time.sleep(3)
    print()
    
    print("Você se prepara para deixar o laboratório.")
    print("Mas no momento em que se aproxima da saída, o chão da sala vibra levemente.")
    print("Runas antigas começam a brilhar nas paredes.")
    print('Uma enorme figura de pedra se move lentamente no canto escuro da sala.\n')
    time.sleep(2)
    print("O guardião do laboratório foi despertado.")
    print("Um Golem Arcano surge diante de você.\n")

    time.sleep(2)
    print("Talvez pela grandiosidade portada naquele Golem Arcano, você ficou fora de si por alguns segundos.")
    print("Tempo suficiente para o Golem disparar uma pedra enorme em sua direção.\n")

    time.sleep(2)
    print("O que você irá fazer?\n")
    
    print("1- Lançar um feitiço para destruir a pedra.")
    print("2- Lançar um feitiço para impedir a pedra.")
    print('3- Tentar esquivar.\n')

    show_life(vida)

    escolha = input('> ')
    time.sleep(1)

    # 1º DECISÃO DA LUTA 
    if(escolha == '1'):
        print()
        print("Rapidamente você se concentra no acúmulo de mana...")
        print("E sem medir esforços você dispara o seu feitiço: Raio Arcano")
        print("Um feixe de luz roxa, pura energia arcana, vai em direção a pedra.")
        print("O Objetivo foi alcançado: Destruir a pedra, porém...\n")
        time.sleep(2)
        vida, dano = random_damage(vida, armor)
        print("A pedra foi fragmentada em várias partes, que continuaram indo em sua direção e você é alvejado por essa chuva de pedra, sem poder fazer nada.\n")
        time.sleep(2)

        print(f"Você recebeu {dano} de dano.")
        show_life(vida)     
    elif(escolha == '2'):
        print()
        print("Rapidamente você se concentra no acúmulo de mana...")
        print("E sem medir esforços você dispara o seu feitiço: Impulsão Arcana")      
        print("Uma onda de choque roxa, é liberada em direção a pedra.\n")
        time.sleep(2)

        print("A ideia foi boa, repelir a pedra com a magia, porém sua magia é fraca demais para isso.")
        print("Sua Impulsão Arcana consegue tirar um pouco o momentum da pedra, porém ela ainda está indo em sua direção.")
        print("Sem ter como fugir, você recebe o impacto da pedra, o jogando alguns metros de distância.\n")
        time.sleep(2)

        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)
        print()
    elif(escolha == '3'):
        print()
        print("Mesmo sendo um mago, você ainda consegue se movimentar.")
        print("Reflexos e agilidade não são o seu forte, mas ainda dá pro gasto.\n")
        time.sleep(2)

        print("Desesperado para desviar da pedra, você se joga para o lado, saindo rolando.")
        print("De uma maneira nenhum pouco heróica ou épica de se ver, na verdade, bem desastrada e vergonhosa se pudesse ser descrita.")
        print("Entretanto, o importante é que funcionou...")
        print("Você vê a pedra colidir com o chão do seu lado, o impacto fez o chão tremer levemente, você suspira aliviado por não ter sido atingido.\n")
    else:
        logout()

    time.sleep(2)
    print("Se recuperando da última ação, você então encara o Golem.")
    print("A criatura mágnifica feita de pedra e mana, tamanho imponente e olhos brilhando em um tom de verde ameaçador.")
    print("Esta que nenhum momento parou de se mexer, e continua marchando em sua direção\n")
    time.sleep(2)

    print("O som pesado emitido pelos passos e o tremor ocasionado pelo seu peso, traduzem o poder que aquele monstro carrega.")
    print("Cada segundo que passa a criatura está cada vez mais próximo de você.\n")
    time.sleep(2)

    print("O que você irá fazer?\n")

    print("1- Atacar diretamente o Golem.")
    print("2- Procurar alguma fraqueza no Golem.")
    if(armor):
        print("3- ")
    
    print("4- Fugir")
  
  
    return vida, armor

## Escadaria
def mage_staircase(vida: float, armor: bool):
    print(f'OI CARA PELO AMOR TOMA ESSA COISA AQUI: {armor}')

    return vida





