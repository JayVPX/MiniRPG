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
    print("1- Lançar um feitiço simples no rato.")
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

        print("O que você faz?\n")
       
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
            restart()
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
        restart()
    else:
        logout()

    return vida

## Entrada na Torre
def mage_tower_entrance(vida: float, armor: bool):
    print("\n=== INTERIOR DA TORRE DA LUA QUEBRADA ===\n")

    print("Ao entrar na magnifíca torre, você se depara com uma pequena sala com um corredor meio que instável")
    print("Vendo que esse era o único caminho, você não tem outra escolha, a não ser adentrar no corredor.")
    print("Runas antigas brilham no chão e você ouve sussurros ao seu redor, quase como se fosse uma interferência no ar causada pela mana.\n")

    time.sleep(2)
   
    print("O que você faz?\n")
    

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

        print('O que você faz?\n')
        
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
            restart()  
       
        else: 
            logout()
    # Decifrar runas
    elif (reposta == '2'):
        print()
        print("Você se agacha, para ler as runas brilhantes mas antigas que se encontram na entrada do corredor.")
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
        print("O que você faz? \n")

        print("1- Entrar na sala")
        print("2- Ir embora.\n")

        show_life(vida)
   
        respostaSecond = input("> ")
        time.sleep(1)

        if(respostaSecond == '1'):
            print()
            print('Talvez a luz tenha te dado confiança, você entra na sala sem medo.\n')

        elif(respostaSecond=='2'):
            print("Você sente que a missão está muito além da sua capacidade.")
            print("Você foge da torre, com sucesso.")
            print("Tudo bem, ninguém irá lhe julgar, magos não são conhecidos exatamente pela coragem...")
            print("GAME OVER")
            print()
            restart()  
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
    print("\n=== BIBLIOTECA DA LUA ETERNA ===\n")

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
    print("O que você faz?\n")

    print("1- Abrir o livro da capa azul.")
    print("2- Abrir o livro da capa vermelho.")
    print("3- Explorar a biblioteca.\n")

    show_life(vida)

    resposta = input("> ")
    time.sleep(1)

    # Abrir Livro Azul
    if (resposta == '1'):
        print()
        print("Com certo receio, você então aproxima sua mão ao livro de azul...")
        print("O silêncio anormal da biblioteca, faz você ouvir seus batimentos e respiração tão altos, como se fosse música na taverna mais animada de Valtherra.\n")
        time.sleep(2)
      
        print("Ao abrir o livro azul, as runas presentes dentro começam a queimar com a energia arcana.")
        print("E então, o tão ansioso silêncio foi substituído.")
        print("O Altar começa a tremer, rangendo como uma máquina que a muito não encontra um óleo.\n")
        time.sleep(2)
        
        print("Ao seu redor você começa a ver vultos se movendo das velhas estandes de livro")
        print("Brevemente, com várias brilhando em cores diversas.\n")
        time.sleep(2)
        
        print("Sem muita surpresa você entendeu... Era uma armadilha")
        print("Os vultos eram Livros Amaldiçoados, vários deles...\n")
        time.sleep(2)

        print("Entretanto no meio do caos luminoso dos livros, você percebe, que em uma das estandes, uma passagem foi aberta.")
        print("Você percebe, que não consegue correr diretamente para a entrada recém aberta, pois os livros estão sob ela.\n")

        time.sleep(3)
        print("O que você faz?\n")
        
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
            restart()
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

    print("\n=== LABORATÓRIO DO ECLIPSE OCULTO ===\n")

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
    print("O que você faz?\n")

    print("1- Vasculhar as estantes de bugigangas mágicas.")
    print("2- Vasculhar as mesas de alquimia.\n")
    
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
        
        vida = mage_miniBoss(vida,armor)

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

        vida = mage_miniBoss(vida, armor)

    else:
        logout()
      
    return vida, armor

#MiniBoss do Laboratório
def mage_miniBoss(vida: float, armor: bool):
    time.sleep(3)
    print()
    
    print("Você se prepara para deixar o laboratório.\n")

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
    print("O que você faz?\n")
    
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
    print()
    print("Se recuperando da última ação, você então encara o Golem.")
    print("A criatura mágnifica feita de pedra e mana, tamanho imponente e olhos brilhando em um tom de verde ameaçador.")
    print("Esta que nenhum momento parou de se mexer, e continua marchando em sua direção\n")
    time.sleep(2)

    print("O som pesado emitido pelos passos e o tremor ocasionado pelo seu peso, traduzem o poder que aquele monstro carrega.")
    print("Cada segundo que passa a criatura está cada vez mais próximo de você.\n")
    time.sleep(2)

    print("O que você faz?\n")

    print("1- Atacar diretamente o Golem.")
    print("2- Procurar alguma fraqueza no Golem.")
    print("3- Fugir\n")
    
    show_life(vida)
    
    escolhaTwo = input("> ") 
    time.sleep(1)
    
    print()

    # 2º DECISÃO DA LUTA
    if(escolhaTwo == '1'):
        print()
        print("Você então anda em direção ao Golem, afim de cortar um pouco a distância e otimizar seu ataque.")
        print("Sentindo a magia fluir pelo seu corpo, você lança seu feitiço: Corte Arcano,")
        print("Energia em forma de foices saem em direção ao Golem, atingindo a parte inferior do corpo da criatura.\n")
        time.sleep(2)
        
        print("Faíscas saem do contato da magia com a superfície dura do Golem.")
        print("O dano foi mínimo...")
        print("O Golem reage imediatamente, levantando o braço para os céus.")
        print('Não demora muito, para você ver o gigantesco braço descendo em sua direção.\n')
        time.sleep(2)

        print("O que você faz?\n")

        print("1- Tentar bloquear o golpe e dar um contra-golpe")
       
        if(armor == False):
            print("2- Tentar desviar e dar um contra-golpe")
            print("3- Utilizar a bomba mágica como contra-golpe\n")
        else:
            print('2- Tentar desviar e dar um contra-golpe')
        show_life(vida)

        escolhaThree = input("> ")
        time.sleep(1)

        if(escolhaThree == '1'):
            print()
            print("Quanto maior, mais lento... É assim que a realidade funciona.")
            print("Antes do braço do Golem, colidir no chão, você consegue desviar recuando.")
            print("Você levanta seu cajado para bloquear o ataque, na esperança de resistir e conseguir efetura um contra-golpe.")
            print("O feitiço Proteção foi usado.")
            print("A força do golem é monstruosa...\n")
            time.sleep(2)


            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano")

            show_life(vida)

            print()
            print("Seu corpo protesta de dor, mas o feitiço garante que você consiga se manter no lugar.\n")
            print("Aproveitando a chance, de não ter sido mandado para o outro lado da sala pela força descomunal da criatura.")
            print("Você lançar seu feitiço: Raio Arcano, a queima roupa no Golem.")

        elif(escolhaThree == '2'):
            print()
            print("Quanto maior, mais lento... É assim que a realidade funciona.")
            print("Antes do braço do Golem, colidir no chão, você consegue desviar recuando.")
            print("Sem perder tempo, você lança seu feitiço: Raio Arcano")
            print("A magia atinge em cheio o peito do Golem.\n")
  
        elif(armor == False and escolhaThree =='3'):
            print()
            print("Você lembra da bomba mágica que pegou a alguns momentos atrás.")
            print("Rapidamente você imbui ela com sua mana, e a joga em direção ao Golem...\n")

            time.sleep(2)
            print("Ao encostar no peito da criatura, uma onda de luz intensa se faz presente na biblioteca.")
            print("Você fica cego instantaneamente")
            print("Só pode ouvir...\n")
            time.sleep(1)

            print("BOOOOOM!\n")
            time.sleep(1)

            print("Logo, você sentiu uma onda de choque exercendo em seu corpo inteiro, fazendo você voar para o outro lado da sala.")
            time.sleep(2)

            print("Após alguns minutos desacordado, você levanta.")
            print("A fadiga te consome, e seu corpo está dolorido.")
            print("O Golem antes imponente, agora estraçalhado no chão com os seus pedaços.\n")

            print("Mas a explosão não afetou apenas ele...")

            vida, dano = random_damage(vida, armor)
           
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)

            print()
            print("Você segue para a saída do laboratório.")
            
            print()
            time.sleep(2)
            print('Ao passar da saída do laboratório.')
            print("Um círculo mágico aparece instantaneamente no seu pé.")
            print("Você percebe que é um círculo mágica de teletransporte.")
            print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

            print('...\n')
        
            print('...\n')
        
            print('...\n')
            return vida
           
        else:
            logout()

        # CAMINHO FINAL PARA CASO ESCOLHATHREE FOR 1 OU 2
        if (escolhaThree in ('1','2')):
            time.sleep(2)
            print("Surpreendentemente, o Golem antes implacável, cambaleia para trás, permanecendo imóvel\n")
            time.sleep(2)
         
            print("No centro do peito do grande Golem, habita agora um buraco, dentro dele, um orbe vívido em cor verde pulsa.")
            print("Você achou o Núcleo do Golem.\n")
            time.sleep(2)

            print("O que você faz?\n")

            print("1- Desferir um feitiço final no Núcleo.")
            print("2- Se aproximar e tomar o núcleo do Golem.\n")

            escolhaFour = input("> ")
            time.sleep(1)

            if(escolhaFour == '1'):
                print()
                print("Aproveitando o momento de fragilidade do gigante de pedra.")
                print("Você se prepara para soltar seu feitiço: Míssil Arcano")
                print("Com destino ao núcleo do Golem, você então libera seu feitiço.\n")
                time.sleep(2)

                print('O choque entre magia e núcleo acontece, você vê aquele orbe sendo dizimado em pedaços.')
                print("E assim que o núcleo deixou de existir. O Golem desmorona.\n")
                time.sleep(2)

                print("Você derrotou o Golem Arcano.\n")
                time.sleep(2)

                print("Você encara os restos do que antes era um Golem implacável.")
                print("Aliviado você, segue seu caminho para a saída do laboratório.")

                print()
                time.sleep(2)
                print('Ao passar da saída do laboratório.')
                print("Um círculo mágico aparece instantaneamente no seu pé.")
                print("Você percebe que é um círculo mágica de teletransporte.")
                print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

                print('...\n')
            
                print('...\n')
            
                print('...\n')
                return vida
                

            elif(escolhaFour == '2'):
                print()
                print("Aproveitando o momento de fragilidade do gigante de pedra.")
                print("Você rapidamente se aproxima, visando aquele orbe de energia.")
                print("Pulsando e brilhando em uma cor de verde vívido.\n")
                time.sleep(2)

                print("Você retira o núcleo do Golem, e instantaneamente o Golem desmorona.\n")
                time.sleep(2)
                
                print("Você derrotou o Golem Arcano.\n")
                time.sleep(2)

                print("Você encara o núcleo na sua mão.")
                print("E começa a sugar a energia presente dentro da esfera.")
                print("Você sente a pura energia e vitalidade do orbe sendo transferida para seu corpo.\n")
                time.sleep(2)

                vida, heal = random_heal(vida)
                print(f"Sua vida foi regenerada em {heal}")
                show_life(vida)

                print()
                print("Com suas energias revitalizadas, você segue seu caminho para a saída do laboratório.")
                
                print()
                time.sleep(2)
                print('Ao passar da saída do laboratório.')
                print("Um círculo mágico aparece instantaneamente no seu pé.")
                print("Você percebe que é um círculo mágica de teletransporte.")
                print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

                print('...\n')
            
                print('...\n')
            
                print('...\n')
                return vida
            else:
                logout()

    if (escolhaTwo =='2'):
        print()
        print("Você recua alguns passos e observa o golem.")
        print("As runas em seu corpo pulsam em intervalos regulares.\n")
        time.sleep(2)

        print("De repente você percebe algo.")
        print("No centro de seu peito há certas rachaduras, mas elas são largas o bastante para você ver um certo objeto dentro dela.")
        print("Era um orbe pulsando e brilhando numa cor vívida de verde.\n")
        time.sleep(2)


        print("Você encontrou o Núcleo do Golem!")
        time.sleep(2)

        print("O golem continua avançando lentamente em sua direção.\n")
        time.sleep(2)

        print("O que você faz?\n")

        print("1- Lançar magia suprema no núcleo.")
        print("2- Usar magia de conteção ao redor do Golem. ")
        

        if(armor == False):
            print("3- Utilizar bomba mágica contra o Golem. ")
            print("4- Tentar conectar sua mente com o núcleo do Golem.\n")
        else:
            print("3- Tentar conectar sua mente com o núcleo do Golem.\n")
        escolhaThree = input("> ")
        time.sleep(1)

        if(escolhaThree =='1'):
            print()
            print("Você sabe onde está o núcleo, porém ainda está protegido pela camada de rocha do Golem.")
            print("Decidido a acabar com isso, você ergue seu cajado preparando para lançar um dos seus feitiços supremos: Lança Prismática\n")
            time.sleep(2)

            print("Runas arcanas começam a girar ao seu redor, o ar se distorce e um feixe multicolorido surge em suas mãos.")
            print("A energia cresce em intensidade, cada cor da lança pulsa como se fosse um fragmento de estrela.")
            print("Com um gesto firme, você dispara a Lança Prismática contra o peito do Golem!\n")
            time.sleep(2)

            print("A lança de energia atravessa a camada de rocha, perfura o núcleo e o colosso solta um rugido metálico antes de desmoronar.")
            print("Mas o poder é grande demais... a magia retorna em um choque violento.")
            print("Seu corpo é atingido pelo recoil, queimaduras arcanas marcam sua pele e sua respiração fica pesada.\n")
            
            vida, dano = random_damage(vida,armor)
            print(f'Você recebeu {dano} de dano.')
            show_life(vida)

            print()
            print("Mesmo ferido, você sabe que venceu, o núcleo foi destruído e o Golem não se erguerá novamente.")
            print("Você continua seu caminho para fora do laboratório.")

            
            print()
            time.sleep(2)
            print('Ao passar da saída do laboratório.')
            print("Um círculo mágico aparece instantaneamente no seu pé.")
            print("Você percebe que é um círculo mágica de teletransporte.")
            print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

            print('...\n')
        
            print('...\n')
        
            print('...\n')

            return vida
       
        elif(escolhaThree == '2'):
            print()
            print("Você decide que não pode enfrentar o poder bruto do Golem diretamente.")
            print("Levantando seu cajado, você canaliza e solta o feitiço: Correntes Arcanas\n")
            time.sleep(2)

            print("Traça runas de contenção no ar e correntes arcanas surgem, envolvendo o colosso.")
            print("O Golem luta, mas as correntes se apertam cada vez mais, esmagando sua estrutura.\n")
            time.sleep(2)

            print("Com um estrondo, o núcleo é comprimido até se despedaçar dentro do peito da criatura.")
            print("O Golem cai imóvel, derrotado pela força da contenção arcana.\n")

            print("Você derrotou o Golem.\n")

            print("Encarando os restos da criatura, você caminha para a saída do laboratório.")

            
            print()
            time.sleep(2)
            print('Ao passar da saída do laboratório.')
            print("Um círculo mágico aparece instantaneamente no seu pé.")
            print("Você percebe que é um círculo mágica de teletransporte.")
            print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

            print('...\n')
        
            print('...\n')
        
            print('...\n')
            return vida

        elif(armor == False and escolhaThree == '3'):
            print()
            print("Você lembra da bomba mágica que pegou a alguns momentos atrás.")
            print("Rapidamente você imbui ela com sua mana, e a joga em direção ao Golem...\n")

            time.sleep(2)
            print("Ao encostar no peito da criatura, uma onda de luz intensa se faz presente na biblioteca.")
            print("Você fica cego instantaneamente")
            print("Só pode ouvir...\n")
            time.sleep(1)

            print("BOOOOOM!\n")
            time.sleep(1)

            print("Mesmo de longe, você sente uma onda de choque exercendo em seu corpo inteiro, fazendo você cair para trás\n")
            time.sleep(2)

            print("Ao abrir os olhos, onde havia o Golem de pé, implacável e imponente. Agora restava apenas fragmentos de pedra no chão.")
            print("Você derrotou o Golem Arcano.\n")
            time.sleep(2)

            print("Encarando os restos da criatura, você caminha para a saída do laboratório.")

            
            print()
            time.sleep(2)
            print('Ao passar da saída do laboratório.')
            print("Um círculo mágico aparece instantaneamente no seu pé.")
            print("Você percebe que é um círculo mágica de teletransporte.")
            print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

            print('...\n')
        
            print('...\n')
        
            print('...\n')
            return vida
        
        elif(armor == True and escolhaThree =='3'):
            print()
            print("Você decide que não pode enfrentar o poder bruto do Golem diretamente.")
            print("Você fecha os olhos e conecta sua mente ao núcleo pulsante do Golem.\n")
            time.sleep(2)

            print("Uma voz antiga ecoa: 'Liberta-me e eu cessarei minha fúria.'")
            print("Canalizando sua energia, você desfaz as runas que prendem o espírito dentro do orbe.\n")
            time.sleep(2)

            print("O núcleo se apaga lentamente, e o colosso para de se mover, como se tivesse encontrado paz.")
            print("Você não destruiu o Golem, mas o libertou — e ele não lutará mais contra você.\n")

            print("Porém ao libertar o espírito, uma onda de memórias e dor invade sua mente.\n")
            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano psíquico.")
            show_life(vida)

            print()
            print("Após se recuperar dessa onda psíquica, você caminha para fora do laboratório.")

            
            print()
            time.sleep(2)
            print('Ao passar da saída do laboratório.')
            print("Um círculo mágico aparece instantaneamente no seu pé.")
            print("Você percebe que é um círculo mágica de teletransporte.")
            print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

            print('...\n')
        
            print('...\n')
        
            print('...\n')
            return vida

        elif(armor == False and escolhaThree == '4'):
            print()
            print("Você decide que não pode enfrentar o poder bruto do Golem diretamente.")
            print("Você fecha os olhos e conecta sua mente ao núcleo pulsante do Golem.\n")
            time.sleep(2)

            print("Uma voz antiga ecoa: 'Liberta-me e eu cessarei minha fúria.'")
            print("Canalizando sua energia, você desfaz as runas que prendem o espírito dentro do orbe.\n")
            time.sleep(2)

            print("O núcleo se apaga lentamente, e o colosso para de se mover, como se tivesse encontrado paz.")
            print("Você não destruiu o Golem, mas o libertou — e ele não lutará mais contra você.\n")

            print("Porém ao libertar o espírito, uma onda de memórias e dor invade sua mente.\n")
            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano psíquico.")
            show_life(vida)

            print()
            print("Após se recuperar dessa onda psíquica, você caminha para fora do laboratório.")
            
            print()
            time.sleep(2)
            print('Ao passar da saída do laboratório.')
            print("Um círculo mágico aparece instantaneamente no seu pé.")
            print("Você percebe que é um círculo mágica de teletransporte.")
            print("Sem ter o que fazer, você apenas aceita o destino, temendo no que pode estar a vir.\n")

            print('...\n')
        
            print('...\n')
        
            print('...\n')
            return vida
        
        else:
            logout()
   
    if(escolhaTwo == '3'):
        print()
        print("Diante do colosso de pedra você treme de medo.")
        print("Você foge da torre, com sucesso.")
        print("Tudo bem, ninguém irá lhe julgar, magos não são conhecidos exatamente pela coragem...")
        print("GAME OVER")
        restart()
   
    else:
        logout()
    

    return vida

## Escadaria
def mage_staircase(vida: float, armor: bool):
    time.sleep(2)
    print()
    print("Após deixar a biblioteca para trás, você chega em uma nova sala.\n")
    
    input("Pressione ENTER, para prosseguir.")

    print("\n=== ESCADARIA DA TORRE ===\n")

    print("A sala é vasta...")
    print("No centro dela se ergue uma enorme escadaria de pedra em formato espiral, subindo em direção aos andares superiores da torre.")
    print("Os degraus são largos, mas desgastados pelo tempo, alguns até parcialmente quebrados.")
    print("Runas antigas estão gravadas nas laterais da escadaria, porém muitas delas estão apagadas ou rachadas.\n")
    time.sleep(2)
    
    print("Uma fraca luz azulada desce dos andares superiores, iluminando parcialmente o caminho.")
    print("O resto do ambiente permanece mergulhado em sombras profundas.\n")


    print("O silêncio aqui é estranho.")
    print("Não há vento ou criaturas.")
    print("Ao lado da base dos primeiros degraus há várias estátuas antigas de guerreiros.\n")
    time.sleep(2)

    print("Cada uma delas veste uma armadura completa e segura armas enferrujadas.")
    print("Todas estão imóveis, cobertas de poeira e teias de aranha.\n")
    time.sleep(2)
    
    print("Você começa a subir lentamente os degraus da escadaria.")
    print("Cada passo ecoa pela sala.\n")
    time.sleep(2)

    print("Quando você alcança aproximadamente metade da escadaria, uma sensação estranha percorre sua espinha.")
    print("Você para por um instante, mas logo volta a subir as escadas.\n")
    time.sleep(2)

    print("Um som metálico ecoa lentamente atrás de você...")
    print("Sem você saber, uma das armaduras do começo estava ali, atrás de você.")
    print("Armadura sem corpo nenhum para vesti-la, com uma aura sombria entorno dela.\n")

    print("Uma Armadura Amaldiçoada apareceu.\n")
    time.sleep(2)

    print("O que você faz?\n")

    print("1- Atacar incessantemente com feitiços contra a Armadura.")
    print("2- Usar feitiço de contenção contra a Armadura.")
    print("3- Purificar a maldição\n")
  
    show_life(vida)

    resposta = input("> ")
    time.sleep(1)

    if(resposta == '1'):
        print()
        print("Decidido a não dar espaço para a criatura reagir, você ergue seu cajado e começa a canalizar mana sem parar.")

        print("Faíscas arcanas se formam ao seu redor enquanto você dispara inumeros feitiços: Míssil Arcano, contra a Armadura Amaldiçoada.")
        print("Os feitiços colidem contra a armadura, espalhando faíscas azuis e fragmentos de magia pelo ar.")
        print("A criatura cambaleia alguns passos, mas continua avançando lentamente.\n")
        time.sleep(2)
     
        print("De repente, runas sombrias gravadas no interior da armadura começam a brilhar.")
        print("Parte da energia mágica que você lança ricocheteia de volta em sua direção.")
        print("A maldição que anima aquela armadura também reflete parte do poder arcano.\n")
        time.sleep(2)
     
        print("A onda de energia te atinge de volta.")

        vida, dano = random_damage(vida, armor)

        print(f"Você recebeu {dano} de dano.")
        show_life(vida)

        print()
        print("Ignorando a dor, você continua atacando.")
        print("A estrutura da armadura começa a rachar.")
        print("O metal antigo não suporta tanta energia arcana.\n")
        time.sleep(2)
   
        print("Com um último disparo de energia concentrada...")
        print("A Armadura Amaldiçoada se despedaça em dezenas de peças de metal espalhadas pela escadaria.\n")
        time.sleep(2)

        print("A energia sombria que a animava se dissipa lentamente no ar.")
        print("A escadaria está livre novamente. E você continua seu caminho.")
   
    elif(resposta == '2'):

        print()
        print("Você percebe que destruir aquela criatura apenas com força bruta pode ser arriscado.")
        print("Em vez disso, você decide usar seu conhecimento arcano.")
        print("Erguendo o cajado, você começa a traçar símbolos mágicos no ar, preparado você utiliza seu feitiço: Correntes Arcanas.\n")
        time.sleep(2)
     
        print("Runas de contenção surgem ao redor da Armadura Amaldiçoada.")
        print("Correntes de energia azulada disparam do chão e das paredes da escadaria.")
        print("As correntes arcanas se enrolam na armadura.")
        print("A criatura luta para se libertar, movendo seu corpo pesado de metal.")
        print("Mas as correntes mágicas apertam cada vez mais.\n")
        time.sleep(2)

   
        print("Agora imobilizada, a armadura não consegue avançar.")
        print("Você aproveita a oportunidade.")
        print("Canalizando sua mana uma última vez, você prepara um feitiço destrutivo: Raio Arcano")
        print("Um feixe concentrado de energia dispara diretamente contra o peito da armadura.")
        print("A magia atravessa o metal antigo e atinge o núcleo da maldição que a anima.\n")
        time.sleep(2)

        print("A armadura perde toda a força de repente.")
        print("As correntes desaparecem enquanto o metal cai inerte pelos degraus da escadaria.")

        print()
        print("A maldição foi destruída e a escadaria está livre.")
        print("Você segue as escadas.")

    elif(resposta =='3'):
        print()
        print("Talvez destruir a armadura não seja a única solução.")
        print("Você fecha os olhos e começa a canalizar uma magia diferente.")
        print("Purificar\n")
        time.sleep(2)
        
        print("Runas luminosas começam a surgir ao seu redor.")
        print("Uma luz suave envolve a escadaria enquanto você estende sua mão em direção à armadura.")
        print("A criatura para de se mover.\n")
        time.sleep(2)


        print("Você força mais energia para dentro do feitiço.")
        print("A luz invade a armadura, penetrando as runas da maldição.")
        print("A criatura começa a tremer violentamente.\n")

        print("Uma onda de energia sombria explode da armadura e invade sua mente.\n")

        vida, dano = random_damage(vida, armor)

        print(f"Você recebeu {dano} de dano mental.")
        show_life(vida)

        print()
        print("Memórias fragmentadas atravessam sua consciência.\n")
        time.sleep(2)

        print("Um antigo cavaleiro.")
        print("Um juramento.")
        print("Uma maldição lançada há décadas.\n")
        time.sleep(2)
      
        print("Com um último esforço, você completa o ritual.")
        print("A luz purificadora envolve completamente a armadura.\n")
        time.sleep(2)

        print("O metal cai lentamente no chão.")
        print("A alma presa finalmente foi libertada.")
        print("A escadaria volta ao silêncio, agora, sem nenhuma ameaça a frente.")
        print("Você segue seu caminho na escada.")

    else:
        logout()

    return vida

# SALA BOSS
def mage_pre_boss_intro(vida: float, armor: bool):
    ## INTRO DA SALA ANTES DO BOSS

    time.sleep(2)
    print()
    print("Você se vê agora numa nova sala, não há nenhum lugar acima de onde você está.")
    print("Logo você entende que chegou no último andar da torre.\n")
    time.sleep(2)

    input("Pressione ENTER, para prosseguir")

    print("\n=== SALA DO LIMIAR ARCANO ===\n")

    print("O teto é alto e parcialmente destruído, permitindo que a luz pálida da lua atravesse as ruínas.")
    print("Partículas de poeira flutuam lentamente pelo ar, iluminadas pela luz prateada.")
    print("As paredes estão rachadas pelo tempo.\n")
    time.sleep(2)

    print("Estátuas quebradas de antigos magos observam a sala com rostos frios e desgastados.")
    print("Algumas perderam a cabeça, outras os braços, mas todas parecem apontar para o mesmo lugar.\n")
    time.sleep(2)

    print()
    print("Para a única porta da sala.")
    print()

    time.sleep(2)
    print("Uma enorme porta de pedra negra na extremidade oposta do salão.")
    print("Runas complexas percorrem toda a sua superfície, pulsando lentamente com energia arcana.\n")
    time.sleep(2)
    
    print("Mesmo à distância, você consegue sentir a pressão mágica emanando de trás daquela porta.\n")

    print("O ar aqui é pesado.")
    print("Denso com mana instável.\n")
    time.sleep(2)
   
    print("Seu instinto de mago grita um aviso claro:\n")

    print("Algo poderoso está do outro lado.\n")

    print("Talvez o responsável pela corrupção que tomou esta torre.\n")
    time.sleep(2)

    print("Seja o que for que habite além daquela porta...")
    print("Este é o último obstáculo da Torre da Lua Quebrada.\n")
    time.sleep(4)

    # INTRO DA SALA DO BOSS

    print()
    print("Mesmo receoso, você abre aquela enorme porta de pedra...")
    print("O som é incessante e o peso era incômodo, mas ainda assim você consegue abrir.")
    print("Sabendo que agora não tem como voltar, você passa por ela.\n")
    time.sleep(2)

    input("Pressione ENTER, para prosseguir.")

    print("\n=== APOSENTOS DO ARQUIMAGO ===\n")

    print("O aposento parece antigo, mas diferente do restante da torre.")
    print("Mesas de estudo estão espalhadas pela sala, cobertas de pergaminhos deteriorados.")
    print("Estantes gigantes alcançam quase o teto, repletas de livros envelhecidos pelo tempo.\n")
    
    print("No centro da sala há um pedestal de pedra.")
    print("Sobre ele repousa um único objeto.\n")
    time.sleep(2)

    
    print("Um grimório.\n")

    print("Sua capa é feita de um couro escuro e danificado, resultado da ação do tempo.")
    print("Runas estranhas estão gravadas na superfície, pulsando lentamente com uma luz púrpura.\n")

    print("Mesmo à distância você sente algo errado.")
    print("Aquele livro... está vivo.\n")
    time.sleep(2)

    print("Quando você se aproxima alguns passos, o grimório se abre sozinho.")
    print("As páginas começam a virar violentamente, como se fossem sopradas por um vento invisível.\n")

    print("Sussurros sobrepostos começam a ecoar pela sala.")
    print("Dezenas... talvez centenas.\n")
    time.sleep(2)


    print("De repente, uma onda de energia explode do livro.")
    print("As páginas se rasgam e começam a flutuar pelo ar.")
    print("Runas corrompidas giram pela sala como um redemoinho de magia negra.\n")

    print("As páginas começam a se juntar.")
    print("Primeiro formando uma massa disforme de energia arcana.")
    print("Depois... um corpo.")
    print("Composto de páginas amaldiçoadas e runas sombrias, um rosto indefinido onde várias vozes falam ao mesmo tempo.\n")
    time.sleep(2)

    print("O Arcano Profanado nasceu.\n")
    
    print("Mesmo sem rosto, você sabe que a criatura te encara.")
    print("Todas as vozes ecoam juntas dentro da sua mente:\n")

    print("'Mais um mago veio buscar o nosso poder...'")
    print("'Mais um mago... para se tornar parte de nós.'")

    print("A batalha final da Torre da Lua Quebrada começa agora.")

# BOSS FIGHT
def mage_boss_fight(vida: float, armor: bool):
    time.sleep(2)
    
    print()
    print("O Arcano profanado ainda está instável, por ter sido recém formado pelo grimório.")
    print("Ele ataca usando páginas e runas vivas.\n")

    print("O que você faz?")

    print('1- Lançar feitiços diretamente contra o Arcano')
    print('2- Atacar o grimório no centro da criatura')
    print('3- Destruir as runas ao redor da entidade\n')

    show_life(vida)
    escolha = input("> ")
    time.sleep(1)


    # 1º FASE BOSS
    if (escolha == '1'):
        print()
        print("Ao ver as páginas vindo em sua direção, você ergue seu cajado pronto para revidar.")
        print("Lança o feitiço: Chuva Arcana")
        print("Do seu cajado é emanado múltiplos mísseis arcanos, em direção da criatura profanada e dos livros.\n")
        time.sleep(2)

        print("A colisão de livros e magia termina em sucesso, com a magia chegando a atravessar os livros e atingindo a criatura, rasgando várias partes do seu corpo.")
        print("Porém os livros destruídos reaparecem, voltando ao corpo do profanado, reconstruindo as partes destruídas.")
        print("Alguns livros continuaram avançando a você e atacando no processo.\n")

        vida, dano = random_damage(vida, armor)

        print(f'Você recebeu {dano} de dano.')
        show_life(vida)
        print()

    elif(escolha == '2'):
        print()
        print("Ao ver as páginas vindo em sua direção, você ergue seu cajado pronto para revidar.")
        print("Lança o feitiço: Raio Arcano")
        print("Do seu cajado é emanado um feixe de energia, em direção da criatura profanada e dos livros.\n")
        time.sleep(2)

        print("Seu feitiço atravessa os livros com sucesso e atinge o grimório no centro da criatura.")
        print("A criatura se contorce violentamente.")
        print("Os gritos de dor das vozes mescladas é agoniante.\n")
       
    elif (escolha == '3'):
        print()
        print("Talvez atacar diretamente não seja a solução.")
        print("Você tenta controlar sua mana e conecta-las as runas compostas no corpo da criatura.\n")

        print("A tentativa termina em sucesso, você consegue interferir no fluxo das runas.")
        print("Algumas das runas que compõe o corpo do Arcano Profanado explodem em fragmentos de magia.\n")
        time.sleep(2)

        print("Porém esses fragmentos, vão em sua direção, chocando com você.\n")
        vida, dano = random_damage(vida, armor)

        print(f'Você recebeu {dano} de dano.')
        show_life(vida)
        print()
     
    else: 
        logout()
    
    #2º FASE BOSS
    time.sleep(2)
    print("A criatura cambaleia com sua última ação.")
    print('O Mago Profanado então ruge violentamente com dezenas de vozes ao mesmo tempo.')
    print("Ao redor da criatura, as páginas começam a girar mais violentamente e as runas começam a brilhar mais.")
    print("A criatura se reorganiza e sua forma cresce ainda mais.\n")

    time.sleep(2)
    print("O rugido começa a ficar cada vez mais estridente.")
    print("Na sua mente você começa a ouvir as dezenas de sussuros...\n")
    time.sleep(2)

    print("'Nós buscamos conhecimento...'")
    print("'Poder...'")
    print("'Imortalidade...'\n")

    print("'E encontramos... isto.'\n")
    
    print("'Você não entende, aprendiz...'")
    print("'Agora... nós SOMOS o grimório.'\n")

    time.sleep(2)
    print("Uma voz grossa se destaca e você ouve...\n")
    time.sleep(2)

    print("'Venha...'")

    print("'Junte-se a nós.'")

    print("'Seu conhecimento será... nosso também.'\n")
    time.sleep(2)
    
    print('Você sente que as vozes estão te corrompendo.\n')

    print("O que você faz?\n")

    print("1- Resistir ao ataque mental e continuar atacando.")
    print("2- Usar magia para silenciar as vozes.")
    print("3- Concentrar energia e atacar o grimório novamente.\n")

    show_life(vida)

    escolhaFaseDois = input('> ')
    time.sleep(1)

    if(escolhaFaseDois =='1'):
        print()
        print("Você tenta ignorar as vozes")
        print("Se preparando para lançar mais feitiços.")
        print("As vozes aumentam, como uma tentativa de que você perca a concentração.\n")
        time.sleep(2)
        
        print("Porém você resiste, e continua lançando sua magia em direção ao Arcano.")
        print("Seus feitiços estão sendo efetivos...")
        print("O corpo da criatura foi danificado.\n")
        time.sleep(2)

        print("Entretando, o sangue descendo do seu nariz e ouvidos, comprova o fato que você também não saiu impune.\n")

        vida, dano = random_damage(vida, armor)

        print(f"Você recebeu {dano} de dano.")
        show_life(vida)
        print()
   
    elif(escolhaFaseDois =='2'):
        print()
        print("Concentrando mana no seu cajado, você lança seu feitiço: Calmaria")
        print("Um feitiço que invoca uma área onde o som não faz efeito.")
        print("Ao seu redor, uma pequena esfera no tom de azul claro perpetua.\n")
        time.sleep(2)
        print("Você sente as vozes no interior da sua mente irem embora.")
        print("Se estabilizando, você redireciona seu olhar ao profanado.\n")

        print("A criatura se contorce mais uma vez, como se o feitiço também tivesse afetado ele mesmo.\n")
    
    elif(escolhaFaseDois =='3'):
        print()
        print()
        print("Ignorando as vozes pulsando na sua cabeça.")
        print("Você ergue seu cajado preparando para lançar mais um feitiço.")
        print("As vozes aumentam, como uma tentativa de que você perca a concentração.\n")
        time.sleep(2)
        
        print("Porém você resiste, e continua lançando sua magia em direção ao Arcano.\n")

        print('Raio Arcano\n')

        print("O feixe de energia sai em direção ao grimório da criatura.")
        print("O choque entre magia e grimório acontece, e a efetividade é comprovada com a contorção do profanado.\n")
        time.sleep(2)

        print("Entretando, o sangue descendo do seu nariz e ouvidos, comprova o fato que você também não saiu impune.\n")

        vida, dano = random_damage(vida, armor)

        print(f"Você recebeu {dano} de dano.")
        show_life(vida)
        print()
 
    else: 
        logout()


    #3º E ULTIMA FASE DO BOSS
    time.sleep(2)

    print()
    print("A criatura recua alguns passos após seus golpes.")
    print("Por um instante... ela parece instável.\n")
    time.sleep(2)
   
    print("O grimório em seu núcleo começa a pulsar de forma irregular.")
    print("As páginas ao redor da entidade desaceleram...")
    print("...e então começam a girar novamente.")
    print("Muito mais rápido que antes.\n")
    time.sleep(2)

   
    print("Duas runas antigas surgem no ar ao redor da criatura.")
    print("Uma aura sombria sai delas e vai de encontro ao corpo da criatura")
    print("Como se as runas estivessem alimentando o Arcano Profanado.\n")
    time.sleep(2)


   
    print("A entidade se curva para frente.")
    print("Sua forma começa a distorcer.\n")

    print("Por um breve momento, ecos distantes atravessam o salão.\n")
    
    print("'Isso... precisa acabar...'\n")

    print("'Controle... está falhando...'\n")
    time.sleep(2)


    print("O grimório então se abre completamente.")
    print("Todas as páginas se espalham no ar como um vendaval arcano.")
    print("As páginas começam a se fundir novamente ao corpo da entidade.\n")
    time.sleep(2)

    print("Mas agora sua forma mudou.")
    print("Runas quebradas percorrem toda sua estrutura.")
    print("A energia arcana ao redor dela pulsa de forma caótica.")
    print("A forma da entidade se expande, alimentada por energia instável.")
    print("A pressão mágica no salão aumenta drasticamente.\n")
    time.sleep(2)


    print("O Arcano Profanado entra em um estado final e descontrolado.")
    print("A batalha atinge seu clímax.\n")
    time.sleep(2)

    print("O profanado direciona seu olhar a você e levanta os braços")
    print("A energia se reune totalmente no grimório localizado no centro da criatura.")
    print("Como se fosse lançar um feitiço devastador.\n")

    print("O que você faz?\n")

    print("1- Liberar todo seu poder contra o profanado")
    print("2- Atacar diretamente o grimório.")
    print("3- Tentar destruir as runas ao redor da criatura.\n")

    show_life(vida)
    escolhaFaseTres = input("> ")
    time.sleep(1)

    if (escolhaFaseTres =='1'):
        print()
        print("O poder do Arcano Profanado cresce de forma descontrolada.")
        print("Runas quebradas percorrem seu corpo como rachaduras em vidro.")
        print("O grimório em seu centro vibra violentamente.")
        print("As páginas giram tão rápido que se tornam apenas um borrão de energia arcana.\n")
        time.sleep(2)

        print("Você sente a pressão mágica esmagar o ar ao seu redor.")
        print("A criatura está reunindo tudo o que resta.\n")

        time.sleep(2)
        print("Por um momento... tudo fica em silêncio.\n")
        time.sleep(2)

        print("Então você faz o mesmo.\n")
        print("Você sabe que este é último golpe, tanto para você, quanto para o Arcano Profanado.")
        print("Você ergue seu cajado preparando para lançar um dos seus feitiços supremos: Lança Prismática\n")
        time.sleep(2)

        print("Runas arcanas começam a girar ao seu redor, o ar se distorce e um feixe multicolorido surge em suas mãos.")
        print("A energia cresce em intensidade, cada cor da lança pulsa como se fosse um fragmento de estrela.\n")
        time.sleep(2)
        
        print("Novamente você começa a ouvir as vozes na sua cabeça...\n")
        time.sleep(2)
     
        print("'Venha então, aprendiz.'\n")

        print("'Mostre-me... o limite do seu poder.'\n")
        time.sleep(2)

        print("AS vozes somem e o Arcano Profanado finalmente lança seu feitiço, um feixe de pura energia em sua direção.")

        print("Aceitando o desafio, você dispara a Lança Prismática contra o Arcano Profanado!\n")
        time.sleep(2)

        print("As magias se chocam violentamente, gerando uma festa de cores e uma onda de choque que faz a sala enorme tremer.")
        print("Porém o embate é decidido, sua Lança Prismática perfura o feixe de energia disparado pela criatura.\n")

        print("Ao perceber isso, o Arcano Profanado abre os braços... parece esperar pelo seu fim.")
        
        print("Na sua mente você ouve novamente uma voz, porém dessa vez, uma voz calma e gentil.\n")
        time.sleep(2)

        print("Nada mal para um novato... Obrigado...\n")
        time.sleep(2)

        print("Então sua magia atinge a criatura, consumindo todo seu corpo.")
        print("Primeiro as páginas.")
        print("Depois as runas.")
        print("A forma monstruosa antes vista, desapareceu, só uma coisa sobrou.\n")

        print("O grimório... lentamente caindo no chão.")

        print("A pressão mágica e a presença maligna presentes naquele lugar somem.\n")
        time.sleep(2)


        print("Você derrotou o Arcano Profanado\n")
        time.sleep(2)

        print("A sobrecarga da mana usada no seu último golpe retorna, evidenciada pela tosse com sangue que você libera.")

        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)

    elif (escolhaFaseTres =='2'):
        print()
        print("Seu olhar se fixa no centro da criatura.")
        print("No grimório.")
        print("Ignorando os ataques da entidade, você avança.")
        print("Erguendo seu cajado em direção ao profanado. Você solta o feitiço: Raio Arcano\n")
        time.sleep(2)
      
        print("O Arcano Profanado percebe.")

        print("'Não...'\n")

        print("'NÃO TOQUE NO GRIMÓRIO!'\n")
        time.sleep(2)

        print("Você reúne toda a força que ainda resta, acumulando mais poder ainda no seu feitiço.")
        print("O feitiço chega ao seu destino, o grimório racha.")
        print("Uma fissura atravessa sua capa antiga.\n")
        time.sleep(2)
        
        print("Por um instante... nada acontece.")
        print("Então as runas começam a brilhar.")

        print("Uma.")
        print("Depois outra.")
        print("Até que todas vão se acendendo em uma espécie de cadeia.\n")

        print("A energia acumulada começa a escapar.")
        print("As páginas se rasgam.")
        print("O ar ao redor vibra violentamente.\n")
        time.sleep(2)

        print("BOOOMM!")

        print("Uma explosão arcana atravessa o salão.")
        print("Você é arremessado violentamente para trás, o choque é tremendo e seu corpo sofre com isso.\n")
        time.sleep(2)
       
        print("Quando a luz desaparece...")
        print("A entidade não está mais lá.\n")

        print("No chão, apenas uma coisa repousa...")
        print("O grimório...\n")
        time.sleep(2)

        print("O Arcano Profanado foi derrotado.")
        time.sleep(2)

        print('Você se levanta, o dano causado pela explosão é significativo, você mal consegue se manter de pé.')
        vida, dano = random_damage(vida, armor)

        print(f'Você recebeu {dano} de dano.')
        show_life(vida)
        print()
   
    elif (escolhaFaseTres =='3'):
        print()
        print("Seu olhar percorre a sala. mas sua atenção é capturada por algo.")
        print("As duas runas que brilham intensamente ao redor da critura, uma de cada lado.")
        print("A mesma energia que envolve o Arcano Profanado flui delas.\n")
        time.sleep(2)
        
        print("Então você entende.")
        print("A criatura está sendo alimentada por essas runas.\n")


        print("Em vez de atacar a entidade...")
        print("Você ataca a primeira runa.\n")
        
        print("O símbolo se parte.")
        print("A energia da sala vacila.\n")
        time.sleep(2)

        print("O Arcano Profanado recua e ruge em dor.\n")
        
        print("'O que pensa que está fazendo...?'\n")

        print("Mesmo com dezenas de vozes mescladas em uma, você conseguia sentir o desespero embutido nela\n")
        time.sleep(2)
        
        print("Se havia desespero, significa que a estratégia está dando certo.")
        print("Sem perder tempo você logo se concentra na runa remanescente.\n")

        print("Sem muitos esforços...")
        print("Você destrói a segunda runa.\n")
        time.sleep(2)
    
        print("A energia que sustentava o ritual desaparece.")
        time.sleep(2)

        print("As vozes na sua cabeça retornam a ecoar.\n")

        print("'NÃO! NÃO! NÃO!'\n")

        print("'NÓS... DERROTADOS POR UM MERO APRENDIZ!'\n")

        print("Rancor e lamento emanavam das vozes...\n")

        print("Dentre as inúmeras vozes, surgiu uma outra... uma gentil e calma.")
        time.sleep(2)

        print("'Obrigado...'\n")
        time.sleep(2)

        print("Sem o poder das runas...")
        print("A criatura arcana perdeu sua força.\n")

        print("O corpo do Arcano Profanado se desfaz lentamente em tinta e papel, deixando uma única coisa para trás...\n")
        time.sleep(2)
        
        print("O grimório...\n")
        time.sleep(2)
        
        print("A pressão mágica e a presença maligna presentes naquele lugar somem.\n")
        print("A sala finalmente fica em silêncio.")
  
    else:
        logout()

# FINAIS DO MAGE PATH
def mage_end():
    print()
    print("Você se aproxima do grimório.\n")

    print("O motivo de todo esses acontecimentos...")
    print("Algo tão poderoso a alguns momentos atrás, agora inofensivo.\n")
    time.sleep(2)

    print("Porém você detecta que o grimório só está em um estado de 'hibernação'")
    print("Se você deixar o grimório ali, só será questão de tempo, para o grimório voltar a o que era antes.")
    time.sleep(2)

    print("Sabendo disso, você não pode simplesmente deixar o grimório.\n")
    print("O que você faz?\n")

    print("1- Destruir o grimório")
    print("2- Levar o grimório para a Academia Raya Lucaria")
    print("3- Se apossar do grimório\n")


    escolhaFinal = input("> ")
    time.sleep(1)


    if(escolhaFinal =='1'):
        print()
        print("Você ergue seu cajado diante do grimório.")
        print("Se ele causou tudo isso... então precisa ser destruído.\n")
        time.sleep(2)

        print("Você desfere um golpe direto contra a capa do livro.")
        print("O impacto ecoa pela sala.")
        time.sleep(2)

        print("Mas o grimório... não se parte.")
        print("Nem mesmo um arranhão.\n")
        time.sleep(2)

        print("Runas começam a surgir lentamente em sua superfície.")
        print("Como se o grimório tivesse despertado.")
        time.sleep(2)

        print("Uma energia fria percorre o ar ao seu redor.")
        print("Você tenta se afastar...\n")
        time.sleep(2)

        print("Mas já é tarde demais.\n")

        print("As páginas do grimório se abrem sozinhas.")
        print("Uma força invisível puxa você em direção a ele.")
        print("Sua visão começa a escurecer.")
        print("A energia arcana envolve seu corpo.\n")
        time.sleep(2)


        print("Então você entende... o grimório não pode ser destruído.")
        print("Ele apenas... coleta.\n")
        time.sleep(2)

        print("As páginas começam a girar ao seu redor.\n")

        print("Cada uma preenchida com nomes.")
        print("Magos.")
        print("Aprendizes.")
        print("Aqueles que tentaram controlar seu poder.\n")
        time.sleep(3)

        print("Agora... mais um nome é adicionado.\n")

        print("Sua voz ecoa junto às outras.")

        print("'Mais um...'")

        print("'Mais uma mente para o grimório...'\n")


        print("Quando tudo termina...")

        print("O grimório se fecha lentamente.\n")
        time.sleep(2)

        print("Esperando...\n")

        print("Esperando pelo próximo mago curioso.\n")

    elif(escolhaFinal =='2'):
        print()
        print("Você observa o grimório em silêncio.\n")

        print("Destruí-lo pode não ser possível.")
        print("E deixá-lo aqui seria apenas adiar outra tragédia.\n")
        time.sleep(2)

        print("Existe apenas um lugar capaz de lidar com algo assim.")
        print("A Academia Raya Lucaria, onde você faz parte.\n")
        time.sleep(2)

        print("Você cuidadosamente fecha o grimório.")
        print("Por um momento... as páginas parecem resistir.")
        print("Mas logo tudo fica em silêncio.\n")
        time.sleep(2)

        print("Você o envolve em tecido e o leva consigo.")
        print("A jornada até a academia é longa.")
        print("E durante todo o caminho...")
        print("você sente como se algo estivesse observando.\n")
        time.sleep(2)

        print("Dias depois, as torres de Raya Lucaria finalmente surgem no horizonte.")
        print("Os magos da academia recebem o grimório com cautela.\n")
        time.sleep(2)

        print("Runas de contenção são imediatamente preparadas.")
        print("Correntes arcanas envolvem o livro.")
        print("Selos antigos são gravados ao redor dele.\n")
        time.sleep(2)

        print("Um dos magos anciões da academia observa o grimório em silêncio.")
        print("'Uma relíquia perigosa...'")
        print("'Mas também... uma fonte incomparável de conhecimento.'\n")
        print("diz ele.")
        time.sleep(2)

        print("O grimório é então trancado nas profundezas da biblioteca proibida.")
        print("Longe de olhos curiosos.")
        print("Longe de mãos imprudentes.\n")
        time.sleep(2)

        print("Enquanto você deixa a academia...")
        print("um leve som ecoa de dentro da biblioteca.")
        print("Como o virar de uma página...\n")
        time.sleep(2)

        print("Talvez...")
        time.sleep(2)
        print("Talvez ainda não tenha acabado...")

    elif(escolhaFinal =='3'):
        print()
        print("Você observa o grimório em silêncio.\n")
        print("Destruí-lo parece impossível.")
        print("E entregá-lo para outros... significaria perder um poder incomparável.\n")
        time.sleep(2)

        print("Então você toma sua decisão.")
        print("Você estende a mão.")
        print("E segura o grimório.\n")

        print("Por um instante... nada acontece.")
        print("Então as páginas se abrem sozinhas.\n")

        print("Runas antigas começam a brilhar.")
        print("A energia arcana invade seu corpo como uma tempestade.\n")
        time.sleep(2)

        print("As vozes tentam surgir.")
        print("porém elas não o consomem.")
        print("elas se curvam.\n")
        time.sleep(2)

        print("'Um novo portador...'")
        print("'Um novo mestre...'\n")

        print("Você fecha o grimório, agora sem poder mágico, virando apenas mais um livro comum.")
        print("Você absorveu todo o poder que o grimório continha.")
        print("E pela primeira vez... o poder responde apenas a você.\n")
        time.sleep(2)

        print("Dias depois, você deixa a Academia Raya Lucaria.")
        print("Sem explicações.")
        print("Sem despedidas.\n")
        time.sleep(2)

        print("Com o passar dos anos, seu poder cresce.")
        print("Feitiços antes considerados impossíveis se tornam triviais.")
        print("Reinos começam a temer seu nome, Velkarys\n")
        time.sleep(3)

        print("Décadas passam.")
        print("Séculos talvez.")
        print("Mas algo muda com o tempo.\n")
        time.sleep(2)

        print("A cada ano... as vozes ficam mais fortes.")
        print("Mais presentes.")
        print("Mais difíceis de ignorar.\n")
        time.sleep(2)

        print("O conhecimento que o grimório concedeu é infinito.")
        print("Mas seu preço também é.\n")
        time.sleep(2)

        print("Lentamente... sua mente começa a mudar.")
        print("Seus pensamentos.")
        print("Seus desejos.")
        print("Seu propósito.")
        print("Até mesmo sua aparência muda...\n")

        time.sleep(2)

        print("O mundo deixa de parecer algo a ser protegido.")
        print("E passa a parecer... algo a ser governado.\n")
        time.sleep(2)

        print("Era após era, sua figura se torna uma lenda.")
        print("Um arquimago impossível de derrotar.")
        print("Um soberano das artes arcanas.\n")
        time.sleep(2)

        print("Até que um novo nome começa a surgir nas histórias.\n")

        print("O Rei Demônio, Velkarys...\n")
        time.sleep(2)

        print("Nas profundezas de uma fortaleza...")
        print("no coração da terra dos demônios")
        print("um trono se encontra no centro de uma sala")
        print("E sobre ele...\n")
        time.sleep(2)

        print("Aquele que um dia foi um mago...")
        print("agora aguarda o próximo herói.")
        print("Alguém forte o suficiente para desafiá-lo.\n")

    else: 
        logout()

    time.sleep(4)
    print("\n=== FIM ===\n")

    restart()

