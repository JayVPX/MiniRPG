from utils import *
import time


#Inicio do Caminho 
def warrior_start(vida: int, armor: bool):
    time.sleep(2)
    print("\n=== PORTÕES DA FORTALEZA DE VELKARYS ===\n")

    print("Diante de você se erguem os imensos muros de Velkarys.")
    print("Não é apenas uma fortaleza... mas uma cidade inteira aprisionada atrás de muralhas negras.\n")
    time.sleep(2)
    print("Torres de pedra escura perfuram o céu encoberto por nuvens vermelhas, enquanto chamas demoníacas queimam em grandes brasões ao longo das muralhas.")
    print("O ambiente ao redor da fortaleza também não é amigável, a floresta negra vive ao redor, consumindo qualquer luz que ouse repousar.\n")
    time.sleep(2)


    print("Mesmo do lado de fora, é possível ouvir os ecos distantes de criaturas marchando e o som metálico de armas sendo forjadas.")
    print("Velkarys não é apenas um refúgio... é o coração do império demoníaco.\n")
    time.sleep(2)


    print("Além dos portões colossais, você consegue ver os telhados sombrios de uma cidade inteira dominada pelos servos do Rei Demônio.")
    print("No centro de tudo, elevando-se acima das torres e construções, está o castelo principal —")
    print("uma estrutura colossal onde o próprio Rei Demônio governa.\n")
    time.sleep(2)


    print("Se a profecia é verdadeira... é aqui que tudo termina.\n")

    print("Guardando o portão principal, você enxerga dois guardas.")
    print("Vestimenta militar simples, armas empunhadas e uma aura sombrio emanando deles.")
    print('Você sabe o que aqueles guardas são...\n')
    time.sleep(2)

    print('Soldados Demoníacos...\n')

    print("Sua entrada está bloqueada por eles...\n")
    time.sleep(2)

    print("O que você faz?\n")

    print("1- Avançar contra os soldados")
    print("2- Contornar a fortaleza pela Floresta Negra")
    print("3- Procurar outro jeito de entrar\n")

    show_life(vida)
    escolha = input("> ")
    time.sleep(1)
    
    if escolha == "1":
        print("\nVocê ergue sua arma e avança contra os soldados demoníacos!")
        print("")
        time.sleep(2)
        print("Eles respondem com gritos mórbidos e investem contra você.\n")
        time.sleep(2)

        print("O combate é brutal, lâminas negras contra sua força e coragem.")
        print("Com grande habilidade, você consegue desarmar o primeiro soldado e desferir um golpe em seu peito, derrotando-o")
        print("O segundo soldado aproveita esse momento e também te desfere um golpe.\n")
        time.sleep(2)
    
        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)

        print("\nSe recuperando rapidamente do golpe, você gira sua espada cortando a cabeça do segundo soldado.")

        print("\nApesar dos ferimentos, você consegue derrotar os soldados, o caminho pelo portão principal está livre para você.")
        print("Você segue em frente...")    

    elif escolha == "2":
        print("\n === FLORESTA NEGRA ===\n")
        print("\nVocê decide evitar o confronto direto e se embrenha na Floresta Negra.")
        time.sleep(2)
        print("O ambiente é sufocante, a luz do sol parece não passar pelas árvores retorcidas, sombras vivas parecem observar cada passo.\n")
        time.sleep(2)

        print("De repente, criaturas menores surgem da escuridão\n")
        time.sleep(2)

        print("Quadrúpedes, garras afiadas, presas salivando... E olhos... Olhos brilhando em carmesim")
        print("Você encontrou uma alcateia de Lobos Sombrios.\n")
        time.sleep(2)
       
        print("Você sente o olhar predatório daquelas criaturas sob você, a sede de sangue emanada por eles podia ser sentida a quilômetros")
        print("E o pior de tudo, a sede era pelo seu sangue.")
        print("Você precisa lutar para sobreviver!\n")
        time.sleep(2)

        print("O que você faz?\n")

        print("1- Usar luz sagrada")
        print("2- Ceifar lobos com sua espada\n")
        show_life(vida)

        escolha_sub = input('> ')
        time.sleep(1)

        if(escolha_sub =='1'):
            print("\nO verdadeiro dom de um guerreiro as vezes pode ser a inteligência ao invés da força...")
            print("Você percebe que por serem criaturas nativas da floresta negra, onde a luz mal existe, elas podem ser sensíveis a ela.\n")
            time.sleep(2)

            print("Apostando nisso, você fecha seus olhos iniciando orações a Luminarie, concentrando mana você então solta o seu milagre: \n")
            time.sleep(2)
            print("'Illuminare'\n")
            time.sleep(2)

            print("Das suas mãos, sai um brilho cegante...")
            print("Os lobos antes famintos, agora ficam atordoados e assustados, parece que você estava certo.")
            print("Você vê os lobos fugindo para o fundo da floresta, desaparecendo na escuridão que só nela habita.\n")
            time.sleep(2)

            print("Aliviado com a retirada dos lobos, você segue seu caminho...")
            print("Mas sendo cauteloso para não se afastar das muralhas da fortaleza, e acabar adentrando mais a fundo da floresta.\n")
        elif(escolha_sub =='2'):
            print('\nErguendo sua espada, você ruge, talvez como forma de reunir coragem, ou até mesmo para tentar assustar os lobos.')
            print("Se fosse para o segundo caso, infelizmente não funcionou, os lobos não se sentem intimidados e avançam em direção a você.")
            print("E você não fica atrás, rugindo ainda mais alto, com a coragem e honra do escolhido pela luz você avança em confronto contra as feras.\n")
            time.sleep(2)

            print("...mordidas")
            time.sleep(2)
            print("...arranhões")
            time.sleep(2)
            print("...cortes de espada\n")
            time.sleep(2)
        
            print("Por alguns minutos, era apenas isso que podia ser ouvido na silenciosa Floresta Negra")
            print("Mas chegou ao fim, e o silêncio novamente reinou naquele recinto.\n")

            print("No lugar onde acontecera a luta, agora retrata um homem em pé, e aos seus pés, corpos de lobos... Todos mortos.")
            print("Você venceu os Lobos Sombrios\n")
            time.sleep(2)

            print("Porém a luta não foi tão fácil, você saiu ferido.")
            vida, dano = random_damage(vida, armor)

            print(f"Você recebeu {dano} de dano.")
            show_life(vida)

            time.sleep(2)
            print("\nOlhando para as carcaças dos Lobos Sombrios, você não consegue não pensar em como um casaco com a pele deles deve ser confortável.")
            print("Mas deixando esse pensamento quase que imediatamente, você continua seu caminho...")
            print("Mas sendo cauteloso para não se afastar das muralhas da fortaleza, e acabar adentrando mais a fundo da floresta.\n")

        else:
             logout()

    elif escolha == "3":
        print("\nVocê observa os arredores, procurando uma alternativa.\n")
        time.sleep(2)
        
        print("Entre as pedras e muralhas da fortaleza, você vê pilhas de caixas cobertas por pano...")
        print("Estranhnado essa situação, você vai em direção ao lugar... ")
        print("Levando a mão ao pano você o retira, apenas para encontrar uma abertura subterrânea.")
        print("Uma passagem... provavelmente usada por contrabandistas.\n")
        time.sleep(2)

        print("Ao entrar, você sente o cheiro de mofo e ouve passos furtivos.")
        print("Um mercador sombrio aparece, oferecendo ajuda em troca de algo.\n")
        print("O que você faz?\n")
        print("1- Pagar com parte da sua energia vital")
        print("2- Recusar e enfrentar o mercador\n")
        show_life(vida)

        escolha_sub = input("> ")
        time.sleep(1)

        if escolha_sub == "1":
            print("\nA proposta não parece tão ruim... ")
            print("Você então a aceita.\n")
            time.sleep(2)

            print("O mercador estende sua mão, como se esperasse por um aperto.")
            print("Você fica confuso mas ainda assim estende sua mão e apertar a mão do mercador.\n")
            time.sleep(2)

            print("Uma luz começa a brilhar no contato das suas mãos, e você sente uma parte da sua energia vital indo embora.")
            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)

            print("\nO mercador sorri, solta um feitiço que parece ser para desativar algo e abre caminho para você, revelando uma entrada secreta para dentro da fortaleza.\n")
           
        elif escolha_sub == "2":
            print("Você recusa a oferta e se prepara para lutar contra o mercador.")
            print("Puxando a espada da bainha, você a atravessa no corpo do individúo a sua frente.")
            print("O mercador não teve tempo de reação, você sente a vida se esvaindo dele, mas não antes de perceber que ele está sorrindo...\n")
            time.sleep(2)

            print("Ignorando isso, você segue para em frente.")
            print("Em meio ao corredor, ao pisar em uma parte, um círculo mágico aparece em seus pés, antes mesmo de você conseguir ter reação...\n")
            time.sleep(2)

            print('BOOOMM!\n')

            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)
   
            
            print("\nUma pequena explosão acontece e você foi ferido.")
            print("Uma armadilha... provavelmente colocado pelo mercador para quem se negar a pagar")
            print("Talvez fosse melhor ter aceitado a oferta...\n")
            time.sleep(2)

            print("Ignorando esses pensamentos, você segue em direção a saída do esconderijo...\n")

        else:
            logout()
    
    else: 
        logout()
    
    return vida, escolha


# Eventos se Decidir entrar na Fortaleza
def warrior_entering_fortress(vida: int, armor: bool):
        print()

        print("\n === INTERIOR DA FORTALEZA DE VELKARYS ===\n")

        print("Agora dentro do coração da capital demoníaca")
        print("Você se prepara para seguir seu caminho ao Castelo no centro da fortaleza.\n")
        time.sleep(2)

        print("Porém seu caminho é interrompido...\n")
        time.sleep(2)

        print("Passos pesados são ouvidos, você então percebem, surgindo em meio as inúmeras casas simples ao seu redor...")
        print("Uma criatura humanóide, gigante e bípede.\n")
        time.sleep(2)

        print("Pele e olhos vermelhos, dentes tão longos que sobressaem de sua boca.")
        print("Na mão carrega consigo uma clava\n")
        time.sleep(2)

        print("A criatura lhe encara, da sua boca escorre baba.")
        print("Ela parece faminta.\n")
        time.sleep(2)

        print("E o alimento delicioso dela é você...\n")
        time.sleep(2)

        print("Você encontrou o Carniceiro Demoníaco\n")
        time.sleep(2)

        print("O Carniceiro Demoníaco ruge alto, fazendo o ar vibrar.")
        print("Ele ergue sua enorme clava acima da cabeça.\n")
        time.sleep(2)


        print("Com um salto monstruoso, ele tenta esmagar você.\n")

        print("O que você faz?\n")

        print("1- Utilizar poder sagrado e bloquear")
        print("2- Desviar do golpe")
        print("3- Avançar antes que o golpe caia\n")

        show_life(vida)
        escolha = input("> ")
        time.sleep(1)

        if(escolha =='1'):
            print('\nVocê fecha seus olhos pedindo mais uma vez, a proteção de Luminarie, a Deusa da Luz...')
            print("E ela lhe atende.\n")
            time.sleep(2)
            
            print("Poder sagrado toma conta do seu corpo.")
            print("Você acumula ele em seu escudo.\n")
            time.sleep(2)

            print("Erguendo seu escudo você se prepara para receber o golpe da poderosa criatura.\n")
            time.sleep(2)

            print("E acontece...\n")
            time.sleep(2)

            print("Clava e Escudo se chocam, uma onda de poeira se levanta, e o chão ao seu redor quebra com o impacto do golpe.")
            print("Porém você permanece de pé e intacto, graças ao poder sagrado.\n")
            time.sleep(2)

            print("O Carniceiro aparenta estar atordoado da colisão das armas.")
            print("E a pequena cortina de poeira levantada pelo choque te dá a chance perfeita para contra atacar.\n")
            time.sleep(2)

            print("O que você faz?\n")

            print("1- Banha sua espada em poder sagrado e ataca")
            print("2- Atacar cegamente o corpo da criatura")
            print("3- Cortar as mãos do carniceiro\n")

            show_life(vida)
            escolha_two = input("> ")
            time.sleep(1)

            if (escolha_two =='1'): 
                print("\nAinda rezando para sua Deusa, você dilui seu poder sagrado em sua espada.")
                print("Sua espada começa a brilhar em um tom dourado.\n")
                time.sleep(2)

                print("A cortina de poeira dificulta a visão mas você ainda consegue enxergar o corpo do carniceiro.")
                print("Você então decide atravessar sua espada no corpo da criatura.\n")
                time.sleep(2)

                print("Você mira no pescoço da criatura e crava sua espada.")
                print("O grito de dor do Carniceiro Demoníaco é ouvido.\n")
                time.sleep(2)

                print("A cortina de fumaça se esvai.\n")
                time.sleep(2)

                print("Você mirou no pescoço, mas acabou acertando no abdomem da criatura.")
                print("O carniceiro, mesmo com sua espada cravada em sua barriga, levanta sua clava.")
                print("Porém o poder sagrado enfraqueceu demais ele.\n")

                time.sleep(2)
                print("A tentativa de contra golpe falha, a criatura falece ali mesmo, com a espada atravessada em seu torso\n")


                print("Você derrotou o Carniceiro Demoníaco.\n")
                time.sleep(2)

                print("Você retira a espada do corpo da criatura, vendo ela desabar ao chão.\n")
                time.sleep(1)
                
                print("Ao guardar a espada de volta na bainha, você tosse sangue...\n")
                time.sleep(1)
                
                print("O efeito colateral de usar muito poder sagrado te atinge.\n")
                vida, dano = random_damage(vida, armor)

                print(f"Você recebeu {dano} de dano.")
                show_life(vida)
                time.sleep(1)


                print("\nIgnorando os colaterais, você vira as costas e encara seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...")

            elif(escolha_two =='2'): 
                print("\nA cortina de poeira dificulta a visão mas você ainda consegue enxergar o corpo do carniceiro.")
                print("Você então decide atravessar sua espada no corpo da criatura.\n")
                time.sleep(2)

                print("Você mira no pescoço da criatura e crava sua espada.")
                print("O grito de dor do Carniceiro Demoníaco é ouvido.\n")
                time.sleep(2)

                print("A cortina de fumaça se esvai.\n")
                time.sleep(2)

                print("Você mirou no pescoço, mas acabou acertando no abdomem da criatura.")
                print("O carniceiro, mesmo com sua espada cravada em sua barriga, levanta sua clava.\n")
          

                time.sleep(2)
                print("Ele consegue desferir o golpe em você, te arremessando para longe.\n")
                vida, dano =random_damage(vida, armor)
                print(f"Você recebeu {dano} de dano.")
                show_life(vida)

                print("\nPorém aquele foi o último esforço da criatura antes de falecer.")
                print("Seu corpo desaba ao chão, com sua espada ainda atravessada em seu torso.")
               
                print("Você derrotou o Carniceiro Demoníaco.\n")
                time.sleep(2)

                print("Calmamente, você se levanta e caminha até o corpo.")
                print("Você retira a espada do corpo da criatura, guardando-a de volta na bainha.\n")
                time.sleep(2)

                print("\nVocê vira as costas e encara seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...")               

            elif(escolha_two =='3'):
                print("\nA cortina de poeira dificulta a visão mas você consegue enxergar as mãos da criatura a sua frente")
                print("Pensando que a melhor estratégia é desarmar a criatura.")
                print("Você rapidamente realiza dois cortes diagonais.\n")
                time.sleep(2)
                
                print("A nuvem de poeira se esvai, e junto dela os membros superiores do carniceiro também.")
                print("A criatura ruge pela tremenda dor, eleva os dois braços amputados enquanto cai de joelhos no chão.")
                print("Situação semelhante quando alguém chora e leva os braços ao rosto para limitar a angústia.\n")
                time.sleep(2)

                print("Uma cena desesperadora, até para um demônio.")
                print("Mas você não se deixa abalar com isso.\n")
                time.sleep(2)
                
                print("Aproveitando a situação, você decide dar o golpe de misericórdia na criatura.")
                print("Sem muito receio você desliza sua espada pelo pescoço do demônio.\n")
                time.sleep(2)

                print("Sangue é espirrado, a cabeça junto do corpo desabam ao chão.\n")
            

                print("Você derrotou o Carniceiro Demoníaco.\n")
                time.sleep(2)

                print("\nVocê vira as costas e encara seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...")   
          
            else:
                logout()

        elif (escolha =='2'):
            print("\nVocê tenta desviar do golpe.")
            print("Mas o Carniceiro muda o trajeto da clava, acertando na horizontal.")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print(f"Você é arremessado para longe\n")
            print(f"Você recebeu {dano} de dano")

            show_life(vida)
            time.sleep(2)

            print("Você se levanta, ofegante, e repara em algo estranho...")
            print("Do lado esquerdo do peito da criatura há uma corrente.")
            print("Ela liga o peito até a parte de trás da cabeça.")
            print("Um possível ponto fraco.\n")
            time.sleep(2)

            print("Você se recupera do golpe e ergue sua arma.")
            print("O Carniceiro Demoníaco caminha lentamente em sua direção, babando de fome.\n")
            time.sleep(2)

            print("O que você faz?\n")
            print("1- Usar poder sagrado para aprisioná-lo")
            print("2- Esperar a criatura agir e contra-atacar")
            print("3- Se esconder pelas casas e tentar surpreendê-lo\n")

            show_life(vida)
            escolha_sub = input("> ")
            time.sleep(1)
            
            if(escolha_sub == '1'):
                print("\nVocê fecha os olhos e concentra sua fé nos céus.")
                print("Luminarie atende seus pedidos e você invoca o feitiço 'Carcer Divinus'.")
                print("Correntes de luz prendem o Carniceiro, queimando sua pele demoníaca.\n")
                time.sleep(2)

                print("Ele tenta escapar, mas você intensifica ainda mais o milagre.")
                print("Aproveitando o momento de vulnerabilidade, você corta a corrente em seu peito.")
                print("A criatura desliga como se fosse uma máquina, caindo morta diante de você.\n")
               

                print("Você derrotou o Carniceiro Demoníaco\n")
                time.sleep(2)

                vida, dano = random_damage(vida, armor)

                print("Você tosse sangue, colateral do uso intenso do milagre.")
                print(f"Você recebeu {dano} de dano")
                show_life(vida)
                time.sleep(2)

                print("\nIgnorando os colaterais, você vira as costas e encara seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...")

            elif(escolha_sub == '2'):
                print("\nVocê mantém a calma e espera o próximo ataque.")
                print("O Carniceiro ergue a clava e avança novamente.")
                time.sleep(2)

                print("Dessa vez, você já conhece seus movimentos.")
                print("Com precisão, desvia e contra-ataca rapidamente, quebrando a corrente em seu peito.")
                print("A criatura desliga como se fosse uma máquina, caindo morta diante de você.\n")

                print("Você derrotou o Carniceiro Demoníaco.\n")
                time.sleep(2)
                
                print("Você vira as costas e encara seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...")   

            elif(escolha_sub == '3'):
                print("\nVocê corre e se esconde entre as casas ao redor.")
                print("Entrando numa das casas de três andares no recinto")
                print("O Carniceiro fareja o ar e segue seu cheiro\n")
                time.sleep(2)

                print("Inteligência não é o forte dele. Ele começa a destruir toda a estrutura da casa.")
                print("As paredes tremem, o teto racha, e a casa começa a desabar.\n")
                time.sleep(2)

                print("Você corre em direção à saída, mas parte dos destroços caem sobre você.")
                vida, dano = random_damage(vida, armor)

                print(f"Você recebe {dano} de dano.")
                show_life(vida)
                time.sleep(2)

                print("\nO Carniceiro, porém, não tem a mesma sorte.")
                print("Soterrado pelos destroços, ele não resiste e morre esmagado.\n")  
                
                print("Você derrotou o Carniceiro Demoníaco.")

                print("Se recuperando dos danos, você vira as costas e encara seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...") 
            
            else: 
                logout()

        elif(escolha == '3'):
            print("\nVocê avança para atacar antes que o golpe caia.")
            print("Com agilidade, você desvia do impacto principal e consegue cortar a criatura.")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print(f"Mesmo assim, o golpe lhe acerta de raspão.")
            print(f"Você recebeu {dano} de dano")
            show_life(vida)
            time.sleep(2)

            print("\nAo se recuperar, você percebe uma corrente estranha.")
            print("Ela sai do lado esquerdo do peito da criatura e vai até atrás da cabeça.")
            print("Um possível ponto fraco.\n")
            time.sleep(2)

            print("O que você faz agora?\n")
            print("1- Atacar a corrente diretamente.")
            print("2- Usar poder sagrado para aprisioná-lo.")
            print("3- Cortar as pernas da criatura.\n")

            show_life(vida)
            escolha_sub = input("> ")
            time.sleep(1)

            if(escolha_sub == '1'):
                print("\nVocê decide que a melhor defesa é o ataque.")
                print("Avança rapidamente contra a criatura, mirando cegamente o ponto fraco.")
                time.sleep(2)

                print("O Carniceiro percebe sua investida e tenta interceptar com um golpe.")
                print("Você ergue o escudo e suporta o impacto.")
                print(f"O choque é brutal, porém você consegue se manter no lugar.")
                time.sleep(2)

                vida, dano = random_damage(vida, armor)
                print(f"Você recebeu {dano} de dano")
                show_life(vida)
                time.sleep(2)

                print("\nAproveitando a guarda baixa do Carniceiro, você desfere um golpe certeiro.")
                print("Sua espada destrói a corrente e a criatura desliga como uma máquina.")
                print("Ela cai morta aos seus pés.\n")

                print("Você derrotou o Carniceiro Demoníaco.")
                time.sleep(2)

                print("Dando uma última olhada para o corpo, você vira de costas.")
                print("encarando seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...") 
            
            elif(escolha_sub =='2'):
                print("\nVocê fecha os olhos e concentra sua fé nos céus.")
                print("Luminarie atende seus pedidos e você invoca o feitiço 'Carcer Divinus'.")
                print("Correntes de luz prendem o Carniceiro, queimando sua pele demoníaca.\n")
                time.sleep(2)

                print("Ele tenta escapar, mas você intensifica ainda mais o milagre.")
                print("Aproveitando o momento de vulnerabilidade, você corta a corrente em seu peito.")
                print("A criatura desliga como se fosse uma máquina, caindo morta diante de você.\n")
               

                print("Você derrotou o Carniceiro Demoníaco\n")
                time.sleep(2)

                vida, dano = random_damage(vida, armor)

                print("Você tosse sangue, colateral do uso intenso do milagre.")
                print(f"Você recebeu {dano} de dano")
                show_life(vida)
                time.sleep(2)

                print("\nIgnorando os colaterais, você vira as costas e encara seu último desafio...")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...")
            
            elif(escolha_sub == '3'):
                print("\nVocê avança em alta velocidade contra a criatura.")
                print("Ela tenta desferir um golpe, mas você desliza entre suas pernas.")
                time.sleep(2)

                print("Enquanto passa, você corta uma das pernas fora.")
                print("A criatura cai apoiada em um joelho, rugindo de dor.")
                time.sleep(2)

                print("Você aproveita e corta a única perna de apoio restante.")
                print("O Carniceiro cai agonizando, incapaz de se levantar.")
                time.sleep(2)

                print("Você sobe sobre seu corpo e crava sua espada na parte de trás da cabeça, onde a corrente se conecta.")
                print("Instantaneamente, a criatura desliga e morre.\n")

                print("Você derrotou o Carniceiro Demoníaco.\n")
                time.sleep(2)

                print("Saindo de cima do corpo da criatura, você trava seu olhar em outro lugar.")
                print("...o Trono do Abismo, o castelo do Rei Demônio.")
                print("Você segue seu caminho até lá então...") 
        
            else: 
                logout()

        else: 
            logout()

        return vida

# Eventos se Decidir entrar na Florest Negra
def warrior_black_forest(vida: int, armor: bool, helpedCivilian: bool):
        purifiedBeast = False
        time.sleep(2)
        print()
        print("Há quanto tempo você caminha?")
        print("Você não sabe...")
        print("Minutos? Talvez até horas... É díficil sentir o tempo passar naquela floresta.")
        print("Você está absorvido em pensamentos...\n")
        time.sleep(2)

        print("Até ouvir um grito...\n")
        time.sleep(2)

        print("'SOCORRO!'\n")
        time.sleep(2)

        print("O pedido de ajuda desesperado te tira do seu transe.")
        print("Novamente você escuta os gritos.\n")
        time.sleep(2)

        print("'POR FAVOR, ALGUÉM NOS AJUDE, SOCORROO!!'\n")
        time.sleep(2)

        print("Os gritos viam da floresta, eram próximos de onde você estava.")
        print("Uma onda de adrenalina atinge seu corpo, os pedidos atingem a sua alma.\n")
        time.sleep(2)
        
        print("O que você faz?\n")
        
        print("1- Ir até os gritos")
        print("2- Ignorar e seguir seu caminho\n")

        show_life(vida)
        escolha = input("> ")
        time.sleep(1)

        if (escolha =='1'):
            print('\nUm herói não consegue ignorar pedidos de socorro.')
            print("sem pensar duas vezes você dispara em alta velocidade na direção dos gritos.")
            print("Passando entre as árvores, você chega ao destino das vozes.\n")
            time.sleep(2)

            print("\n=== VILAREJO ARRUINADO ===\n")

            print("Uma criatura monstruosa anda entre as casas destruídas.")
            print("Seu corpo lembra o de um lobo... mas muito maior.")
            print("Chifres negros crescem de sua cabeça.")
            print("Sua pele parece feita de sombra viva.\n")
            time.sleep(2)

            print("Aquela criatura é a Besta Abissal\n")

            print("A criatura avança sobre um grupo de aldeões encurralados.")
            print("Eles não têm para onde correr.")
            time.sleep(2)


            print("Nesse momento...")
            print("O olhar de um dos aldeões cruza com o seu.\n")
            time.sleep(2)

            print("Os olhos dele se arregalam.")
            print("A esperança surge em seu rosto.\n")
            time.sleep(2)            

            print("'Por favor...'\n")

            print("'Nos ajude...'\n")
            time.sleep(2)

            print("O que você faz?\n")

            print("1- Ajudar os aldeões")
            print("2- Ignorar e continuar sua missão\n")

            show_life(vida)

            escolha_sub = input("> ")
            time.sleep(1)

            if(escolha_sub == '1'):
                vida, purifiedBeast = warrior_abssal_beast(vida, armor)

            elif(escolha_sub == '2'):
                print("\nVocê fecha os olhos por um instante...")
                time.sleep(2)
                print("E decide que sua missão é maior do que salvar alguns aldeões.")
                print("Sem olhar para trás, você continua seu caminho pela floresta.\n")
                time.sleep(2)

                print("Enquanto se afasta, os gritos de dor e desespero ecoam em seus ouvidos.")
                print("A Besta Abissal massacra os aldeões sem piedade.")
                time.sleep(2)

                print("Você sente o peso da culpa em seu coração.")
                print("Mas também sente sua determinação se fortalecer, nada irá desviá-lo de derrotar o Rei Demônio.\n")
                time.sleep(2)

                print("No entanto, ao ignorar os aldeões, você perde a chance de receber ajuda futura.")
                print("O vilarejo não terá sobreviventes para apoiá-lo na batalha final.\n")
                time.sleep(2)

                print("Você segue sozinho, carregando o fardo da sua escolha.")
                helpedCivilian = False
                time.sleep(2)
                print("Após alguns minutos caminhando, você encontra uma espécie de buraco na muralha da fortaleza")
                print("Sem perder muito tempo você passa por ela.")
                print("Agora você está dentro da Fortaleza de Velkarys\n")
          
            else: 
                logout()

        elif(escolha =='2'):
            print('\nVocê pensa em ir, porém seu corpo exita')
            print("O receio e a ansiedade ocupam totalmente a sua mente\n")
            time.sleep(2)
            
            print("Essas vozes vindo do fundo dessa floresta")
            print("Podem nem ser de 'alguém' que precisa mesmo de ajuda")
            print("As chances de serem uma armadilha ou um monstro são grandes.\n")
            time.sleep(2)

            print("Isso, um monstro...")
            print("Com certeza é um monstro\n")
            time.sleep(2)

            print("Você decide que essa é a verdade.\n")
            time.sleep(2)
            
            print("A coragem não adianta se a morte é a consequência...")
            print("Você não pode morrer assim, o mundo precisa do seu herói\n")
            time.sleep(2)

            print("Virando de costas contra os gritos de desespero, você segue seu caminho...\n")

            helpedCivilian = False

            time.sleep(2)
            print("Após alguns minutos caminhando, você encontra uma espécie de buraco na muralha da fortaleza")
            print("Sem perder muito tempo você passa por ela.")
            print("Agora você está dentro da Fortaleza de Velkarys\n")
      
        else:
             logout()
    
        return vida, helpedCivilian, purifiedBeast

# MobFight da Floresta Negra
def warrior_abssal_beast(vida: int, armor: bool):
    purifiedBeast = False
    print()
    print("O aldeão não foi o único...")
    print("A Besta Abissal percebe sua presença.")
    print("Seus olhos carmesim se fixam em você.\n")
    time.sleep(2)

    print("Com um rugido monstruoso, ela abandona os aldeões e dispara na sua direção.")
    print("A velocidade da criatura é absurda.\n")
    time.sleep(2)

    print("O que você faz?\n")
    print("1- Erguer escudo e bloquear ataque")
    print("2- Desviar e tentar contra-atacar")
    print("3- Usar poder sagrado para conter a criatura\n")
    show_life(vida)

    escolha = input("> ")
    time.sleep(1)

    if(escolha == '1'):
        print("\nVocê ergue seu escudo com firmeza.")
        print("A criatura colide contra você com força brutal.")
        time.sleep(2)

        print("O impacto é forte demais, seus braços ardem com a pressão.")
        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)
        time.sleep(2)

        print("Mesmo sentindo a dor, você aproveita a abertura e golpeia a criatura algumas vezes.")
        print("A Besta recua, soltando um rugido ensurdecedor.")
        time.sleep(2)

        print("Ao observar, você percebe um ponto fraco brilhando em seu peito, uma mancha de energia sombria.\n")
        print("O que você faz?\n")
        print("1- Atacar diretamente o ponto fraco")
        print("2- Derrubar a besta no chão")
        print("3- Usar poder sagrado para atacar\n")

        show_life(vida)
        escolha_sub = input("> ")
        time.sleep(1)

        if(escolha_sub == '1'):
            print("\nVocê corre em direção à criatura, mirando diretamente o ponto fraco em seu peito.")
            print("Sua lâmina atravessa a mancha de energia sombria, causando um ferimento profundo.\n")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print("Mas frente a frente, a criatura contra-ataca violentamente.")
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)
            time.sleep(2)

            print("\nVocê recua, ofegante, mas vê a Besta cambalear e finalmente cair ferida no chão.")


        elif(escolha_sub == '2'):
            print("\nVocê investe violentamente contra a criatura com seu escudo.")
            print("O impacto é brutal, colidindo com a Besta e a deixando atordoada.\n")
            time.sleep(2)

            print("Sem forças para resistir, ela cai ao chão, exausta e ferida.")


        elif(escolha_sub == '3'):
            print("\nSe concentrando na conexão com a Deusa da Luz e imerso em rezas você invoca o poder sagrado..")
            print("Runas de luz surgem ao seu redor, formando um feixe radiante.")
            time.sleep(2)

            print("Você dispara o feitiço contra o peito da criatura.")
            print("A energia divina atinge em cheio, mas a resistência da Besta é feroz.\n")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print("A criatura consegue avançar e atingi-lo antes de cair")
            print(f"Você recebeu {dano} de dano")
            show_life(vida)
            time.sleep(2)

            print("\nMesmo ferido, você vê a criatura cambalear e desabar ao chão, derrotada.")

        else:
            logout()

    elif(escolha == '2'):
        print("\nVocê espera o ataque da criatura com calma.")
        print("No instante em que ela salta, você desvia com sucesso.")
        time.sleep(2)

        print("A poeira levanta quando a Besta colide com o chão.")
        print("Você aproveita o momento e encurta a distância.")
        print("Agora você está ao lado da criatura.\n")
        time.sleep(2)

        print("O que você faz?\n")
        print("1- Empurrar a besta contra uma parede")
        print("2- Cortar o tendão da perna traseira")
        print("3- Saltar sobre suas costas\n")

        show_life(vida)
        escolha_sub = input("> ")
        time.sleep(1)

        if(escolha_sub == '1'):
            print("\nVocê investe com força total contra a criatura, empurrando-a contra a parede.")
            print("O impacto ecoa pelo vilarejo arruinado.")
            time.sleep(2)

            print("Sem hesitar, você desfere várias espadadas no corpo da Besta Abissal.")
            print("O sangue sombrio escorre, mas num momento de desespero a criatura se solta do seu aperto.\n")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print("A criatura desfere um golpe em você.")
            print(f"Você recebeu {dano} de dano")
            show_life(vida)
            time.sleep(2)

            print("\nVocê recua, ofegante, enquanto a criatura cambaleia e finalmente cai sem forças no chão.")

        elif(escolha_sub == '2'):
            print("\nVocê rapidamente desliza por trás da criatura, mirando suas pernas traseiras.")
            print("Com precisão, você corta um dos tendões.\n")
            time.sleep(2)

            print("A criatura urra de dor, mas reage com um coice desesperado.")
            vida, dano = random_damage(vida, armor)
            print(f"As garras rasgam sua pele.")
            print(f"Você recebeu {dano} de dano")
            show_life(vida)
            time.sleep(2)

            print("Você é jogado para trás, mas vê a criatura mancando e exausta.")
            print("Logo, ela desaba no chão, sem forças para continuar.\n")

        elif(escolha_sub == '3'):
            print("\nVocê escala rapidamente pelas costas da criatura.")
            print("Ela tenta te atacar, mas não consegue alcançar.\n")
            time.sleep(2)

            print("Com firmeza, você finca sua espada nas costas da Besta Abissal.")
            print("Ela solta um grito monstruoso e se eleva, como um touro tentando expulsar o toureiro.\n")
            time.sleep(2)

            print("O esforço funciona, você é lançado ao chão.")
            print("Apesar da queda, você não sofre ferimentos.\n")
            time.sleep(2)

            print("A criatura cambaleia, solta um último rugido e desaba ao chão, derrotada.\n")
 
        else: 
            logout()

    elif(escolha == '3'):
        print("\n Se concentrando na conexão com a Deusa da Luz e imerso em rezas você invoca o poder sagrado.")
        print("Runas de luz surgem ao seu redor, formando um círculo brilhante.")
        time.sleep(2)

        print("'Carcer Divinus', uma milagre divino para aprisionar a criatura.")
        print("Correntes de luz envolvem a Besta Abissal, mas ela resiste violentamente.\n")
        time.sleep(2)

        print("O que você faz?\n")
        print("1- Intensificar o poder do milagre.")
        print("2- Usar vantagem e atacar o peito da criatura.\n")

        show_life(vida)
        escolha_sub = input("> ")
        time.sleep(1)
        
        if(escolha_sub == '1'):
            print("\nVocê intensifica o poder do milagre, canalizando mais da sua energia vital.")
            vida, dano = random_damage(vida, armor)
            print("Você sacrifica parte da sua energia.")
            print(f"Você recebeu {dano} de dano")
            show_life(vida)
            time.sleep(2)

            print("\nAs correntes brilham incessantemente, queimando a criatura com luz sagrada.")
            print("A Besta Abissal urra em agonia, sua pele de sombra se desfaz em fumaça.\n")
            time.sleep(2)

            print("Depois de um tempo, as correntes se desfazem e a criatura cai exausta ao chão.\n")

        elif(escolha_sub == '2'):
            print("\nVocê aproveita que a criatura está imobilizada e se aproxima rapidamente.")
            print("Com precisão, você desfere um golpe certeiro no peito da Besta Abissal.\n")
            time.sleep(2)

            print("O ataque é bem-sucedido, mas a dor faz a criatura se contorcer violentamente.")
            print("As correntes do milagre se quebram em estilhaços de luz.\n")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print("A criatura acerta você com suas garras")
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)
            time.sleep(2)

            print("\nMesmo ferido, você vê a criatura cambalear e cair exausta ao chão.\n")
       
        else:
            logout()
        
    else: 
        logout()
  
    time.sleep(2)
 
    #AÇÃO FINAL DO BOSS  
    print("\nA Besta Abissal está vulnerável.")
    print("Ela respira pesado e sua sombra começa a falhar.\n")
    time.sleep(2)
    print("Esta é sua chance de acabar com isso.\n")

    print("O que você faz?\n")

    print("1- Decapitar a criatura")
    print("2- Perfurar o coração")
    print("3- Purificar com luz sagrada\n")
   
    show_life(vida)
    escolha_final = input("> ")
    time.sleep(1)

    if(escolha_final == '1'):
        print("\nVocê se aproxima sem hesitar.")
        print("Com um movimento firme, sua espada desliza pelo pescoço da criatura.")
        time.sleep(2)

        print("A cabeça da Besta Abissal rola pelo chão, enquanto o corpo cai imóvel.")
        print("Você guarda sua espada na bainha e encara o silêncio que resta.\n")
        time.sleep(2)

        print("Você derrotou a Besta Abissal.\n")

    elif(escolha_final == '2'):
        print("\nVocê se aproxima e enfia sua espada no coração da criatura.")
        time.sleep(2)

        print("Num último ato de sobrevivência, a Besta crava suas presas em seu ombro.")
        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)
        time.sleep(2)

        print("\nMesmo ferido, você sente a criatura perder suas forças.")
        print("Ela desfalece diante de você, imóvel.\n")
        time.sleep(2)

        print("Você derrotou a Besta Abissal.\n")

    elif(escolha_final == '3'):
        print("\nVocê sente que a Besta foi corrompida pelo poder dos demônios e pela floresta.")
        print("Com fé, você reza para Luminarie, pedindo piedade por aquela alma perdida.\n")
        time.sleep(2)

        print("Você invoca o milagre divino: Sanctitas.")
        print("O corpo da criatura é envolto em luz, e sua aura maligna começa a se dissipar.\n")
        time.sleep(2)

        print("A pelugem negra dá lugar a um tom dourado escuro.")
        print("Seus olhos carmesim agora brilham em azul, como reflexo do céu.\n")
        time.sleep(2)

        print("A criatura recém purificada se levanta sobre as quatro patas, parece que o milagre também a curou.")
        print("Ela se aproxima e lambe seu rosto, em sinal de agradecimento.")
        print("Em seguida, se vira e desaparece na floresta.\n")
        time.sleep(2)

        print("Você purificou a Besta Abissal.\n")

        purifiedBeast = True

    else:
        logout()
   
    # FINAL COM ALDEÕES MOSTRANDO ENTRADA NA MURALHA
    print("\nA vila está salva. O seu trabalho ali acabou.")
    time.sleep(2)

    print("Você vira de costas, pronto para seguir sua missão.")
    print("Mas antes de partir, os aldeões correm até você.\n")
    time.sleep(2)

    print("'Herói... obrigado!' dizem em uníssono, com lágrimas e sorrisos.")
    print("Eles o convidam para suas casas, oferecendo gratidão e descanso.\n")
    time.sleep(2)

    print("Você balança a cabeça e responde com firmeza:")
    print("'Não posso. Ainda tenho uma missão maior... preciso entrar na Fortaleza de Velkarys.'\n")
    time.sleep(2)

    print("Os aldeões se entreolham, surpresos e preocupados.")
    print("Um deles, um homem mais velho, dá um passo à frente e fala:")
    time.sleep(2)

    print("'Se é isso que deseja... eu conheço uma passagem secreta.'")
    print("'Ela fica na muralha, não muito longe daqui. Poucos sabem dela.'\n")
    time.sleep(2)

    print("Guiado pelo aldeão, você atravessa o vilarejo destruído e chega até uma fenda escondida na muralha.")
    print("A entrada é estreita, mas suficiente para passar despercebido.\n")
    time.sleep(2)

    print("=== INTERIOR DA FORTALEZA DE VELKARYS ===")

    print("Você atravessa a passagem e sente o ar pesado mudar.")
    print("Finalmente, seus pés pisam no interior da Fortaleza de Velkarys.\n")
    time.sleep(2)

    print("O seu objetivo final, o Castelo do Rei Demônio está agora visível aos seus olhos...")
    print("Você segue em direção a ele.\n")

    return vida, purifiedBeast

# Caminho em Comum PreBoss
def warrior_three_way(vida: int, armor: bool):
    print("\nApós longos minutos de caminhada, finalmente...")
    print("Diante de você se ergue o Trono do Abismo.")
    print("O Castelo do Rei Demônio, uma fortaleza colossal de pedra negra, coroada por torres retorcidas que parecem tocar o céu encoberto.\n")
    time.sleep(2)

    print("As muralhas exalam uma aura sufocante, e cada janela brilha com chamas demoníacas.")
    print("O ar é pesado, e até mesmo o chão parece pulsar com energia maligna.\n")
    time.sleep(2)

    print("Mas ao se aproximar, algo inesperado acontece...")
    print("Você sente um resquício fraquíssimo de energia divina.")
    print("Um fio de luz quase imperceptível, que se arrasta até uma das vielas próximas ao castelo.\n")
    time.sleep(2)

    print("O que você faz?\n")
    print("1- Entrar diretamente no castelo")
    print("2- Procurar outro jeito de entrar no castelo")
    print("3- Seguir os resquícios de poder divino\n")

    show_life(vida)
    escolha_caminho= input("> ")
    time.sleep(1)

    if(escolha_caminho not in ['1', '2', '3']):
        logout()
  

    return vida, escolha_caminho

# 1º caminho:  Templo Antigo
def warrior_old_temple(vida: int,armor: bool, helpedCivilian: bool):
    print("\nVocê decide seguir o resquício de energia divina.")
    print("Ele o guia até uma viela escondida, onde ruínas antigas repousam.")
    print("Entre as sombras, você encontra um Antigo Templo, esquecido pelo tempo.\n")
    time.sleep(2)
        
    print("Apesar de destruído, ainda há uma aura de santidade no local.")
    print("Talvez aqui você encontre respostas... ou poder.\n")

    time.sleep(2)
    
    print("=== ANTIGO TEMPLO DIVINO ===")
    
    print("\n Ao entrar no recinto, você observa ao redor.")

    print('Há estátuas representando os Deuses...')
    print("Todas destruídas, algumas faltando cabeças, outras membros.\n")

    print("Os assentos de madeira, há muito já consumido pelos cupins, recebiam neles apenas teias de aranha.")
    print("No centro, o altar se encontra, recebendo a única luz solar do recinto do teto quebrado.\n")
    
    print("Dói seu coração ver o lar dos Deuses devastado desse jeito.\n")
    
    print("O que você faz?\n")
    print("1- Rezar no altar")
    print("2- Explorar o templo\n")
    
    show_life(vida)
    escolha = input('> ')
    time.sleep(1)
    
    if(escolha =='1' and helpedCivilian == True):
        print('\n Você caminha lentamente ao altar central')
        print("Ajoelhando no altar, sua mente se ocupa com orações a Luminarie.\n")
        time.sleep(2)
        
        print("'Ó grande portadora da Luz, senhora da Justiça, a mais amada e benevolente dos Deuses...'")
        time.sleep(1) 
        print("'Ouça minhas preçes, abençoe a minha jornada.'")
        time.sleep(1) 
        print("'Que a coragem e a honra, seja meu escudo para proteger os inocentes.'")
        time.sleep(1) 
        print("'A minha vida está em tuas mãos.'")
        time.sleep(1) 
        print("E se por ventura, a morte seja meu destino...")
        time.sleep(1) 
        print("Que eu seja recebido no paraíso pelo seu colo acolhedor.")
        time.sleep(1) 
        print("Lux benedicat...")
        time.sleep(2)
        
        print("...\n")
        time.sleep(1)
        print("...\n")
        time.sleep(1)
        
        print("...\n")
        time.sleep(1)
        
        print("Seu corpo brilha em dourado")
        print("Você sente o poder sagrado se apoderar de seu corpo.")
        print("Suas preces foram atendidas\n.")
        time.sleep(2)

        print("Uma voz gentil e doce invade sua cabeça\n")
        
        print("'Portador da luz... que essa benção ajude o seu caminho'")
        print("'Lux benedicat... minha criança.'\n")        
        time.sleep(2)
        
        print("A voz some, e com ela a luz que lhe cirulava também")
        print("Você sente seu corpo está mais rígido.\n")
        time.sleep(2)
        
        print("Você recebeu a benção da Deusa.\n")
        armor = True
        time.sleep(2)
        
        print("O poder sagrado te protege e você tomará menos dano dos inimigos.")
        print("Um barulho se cria no templo antigo, voce percebe que de frente ao altar, surgiu uma passagem.")
        print("Você entende que aquilo é mais um presente dos Deuses, confiante você passa pela entrada.")
    
    elif(escolha =='1' and helpedCivilian == False):
        print('\n Você caminha lentamente ao altar central')
        print("Ajoelhando no altar, sua mente se ocupa com orações a Luminarie.\n")
        time.sleep(2)
        
        print("'Ó grande portadora da Luz, senhora da Justiça, a mais amada e benevolente dos Deuses...'")
        time.sleep(1) 
        print("'Ouça minhas preçes, abençoe a minha jornada.'")
        time.sleep(1) 
        print("'Que a coragem e a honra, seja meu escudo para proteger os inocentes.'")
        time.sleep(1) 
        print("'A minha vida está em tuas mãos.'")
        time.sleep(1) 
        print("E se por ventura, a morte seja meu destino...")
        time.sleep(1) 
        print("Que eu seja recebido no paraíso pelo seu colo acolhedor.")
        time.sleep(1) 
        print("Lux benedicat...")
        time.sleep(2)
        
        print("...\n")
        time.sleep(1)
        print("...\n")
        time.sleep(1)
        print("...\n")
        time.sleep(2)
        
        print("O silêncio se faz presente. Nada acontece.") 
        print("Você levanta desapontado.\n")
        time.sleep(2)
        
        print("Mas então...") 
        print("Um barulho se cria no templo antigo, voce percebe que de frente ao altar, surgiu uma passagem.")
        print("Você entende que aquilo é mais um presente dos Deuses, confiante você passa pela entrada.")
    
    elif(escolha =='2'):
        print('\nVocê começa a andar e explorar o templo.')
        print("Buscando por respostas para perguntas que você não sabe as respotas\n")
        time.sleep(2)
        
        print("Seu olhar curioso paira sobre os locais do templo.")
        print("Porém você não acha nada\n")
        time.sleep(2)
        
        print("Ao virar de costas e preparado para sair do templo...")
        print("Você sente novamente resquícios de poder sagrado.")
        time.sleep(2)
        
        print("Retomando sua atenção ao templo")
        print("Você sente os requícios indo em direção a uma parede atrás do altar central da capela.\n")
        time.sleep(2)
        
        print("Ao enconstar sua mão na parede, ela começa a tremer")
        print("Uma passagem é aberta.\n")
        time.sleep(2)
        
        print("Você entende que aquilo é mais um presente dos Deuses, confiante você passa pela entrada.\n")

        print("Você entra num corredor reto e escuro, sem muita escolha você percorre ele")
        print("Após alguns minutos andando você chega no final do corredor. Mas ele está fechado, não há nada, nenhum porta.\n")
        time.sleep(2)
        
        print("Você se aproxima da parede, e a toca")
        print("No momento em que o contato acontece, a parede começa a tremer, e na sua frente uma passagem é aberta.\n")
        time.sleep(2)

        print("Confiantemente você passa por aquela saída, sem saber que você chegou no seu destino final.")
    else:
        logout()
    
    return vida, armor
        
# 2º caminho: Telhado do Castelo
def warrior_rooftop(vida: int, armor: bool, helpedCivilian: bool, beastPurified: bool):
    print("\nVocê observa as muralhas e decide procurar uma entrada alternativa.")
    print("Após explorar, encontra uma escada quebrada que leva até os telhados.")
    print("Com cuidado, você começa a subir.\n")
    time.sleep(2)

    print("=== TELHADOS DO CASTELO ===\n")

    print("Cada degrau range sob seu peso...")
    print("Mas você consegue chegar ao topo do castelo.\n")
    time.sleep(2)

    print("O vento sopra forte entre as torres.")
    print("Diversas gárgulas observam o pátio... imóveis.\n")

    time.sleep(2)

    print("Você dá alguns passos...")
    print("CRACK.\n")
    time.sleep(2)
    
    print("Um barulho pesado se faz presente.")
    print("Você então observa a origem do som\n")
    time.sleep(2)

    print("Duas gárgulas ganham vida e começam a se mexer\n")

    print("Você encontrou as Gárgulas Gêmeas\n")

    print("Sem perder tempo elas começam a avançar em sua direção.")
    time.sleep(2)

    # LUTA 2x2 CASO VOCÊ TENHA PURIFICADO A BESTA ABISSAL
    if(beastPurified == True):
        print("\nAntes que as gárgulas avancem, você escuta um latido atrás de si.")
        print("Você se vira e vê a Antiga Besta Abissal, agora purificada.")
        print("Ela corre até você e se posiciona ao seu lado, pronta para lutar.\n")
        time.sleep(2)

        print("O combate que seria um 2x1 agora se tornou um 2x2.")
        print("O lobo avança contra uma das gárgulas, enquanto a outra vem em sua direção.\n")
        time.sleep(2)

        print("O que você faz?\n")
        print("1- Golpear diretamente a gárgula")
        print("2- Usar poder sagrado contra ela")
        print("3- Desviar para o lado e contra-atacar\n")

        show_life(vida)
        escolha_gargula = input("> ")
        time.sleep(1)

        if(escolha_gargula == '1'):
            print("\nVocê ergue sua espada e espera o salto da gárgula.")
            print("No instante certo, desfere um corte vertical.\n")

            print("Sua lâmina atravessa a cabeça de pedra, rachando-a em duas.")
            print("A gárgula se desfaz em pó e despenca telhado a baixo.\n")

            print("Fazendo chover uma poeira sob o castelo demoníaco.")

        elif(escolha_gargula == '2'):
            print("\nVocê canaliza sua energia divina através da sua fé.")
            print("Olhando para a gárgula você conjura seu milagre: \n")

            time.sleep(2)
            print("'Flammae divinae'\n")
            time.sleep(2)

            print("A gárgula é envolta em chamas sagradas.")
            print("Seu corpo pedra se torna pó dourado e ela se desfaz instantaneamente.\n")
        
        elif(escolha_gargula =='3'):
            print("\nVocê espera a gárgula vir em sua direção.")
            print("A gárgula rapidamente cumpre a sua expectativa")
            print("Ela pula em mergulha em sua direção!\n")

            print("Você espera o momento certo e rola para o lado.")
            print("Porém o gárgula arrasta suas garras pela suas costas.\n")

            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano")
            show_life(vida)

            print("\nA gárgula pousa próximo a você")
            print("Como os ferimentos não foram graves, você rapidamente se recupera\n")

            print("Desferindo um corte vertical você corta a gárgula no meio.")
            print("A gárgula é dividida em dois, e sua pele de pedra se desfaz em pó na sua frente.")

        else:
            logout()
        
        time.sleep(2)
        print("Ao derrotar a gárgula, você então direciona seu olhar para onde se encontra a outra luta.")
        print("O Lobo contra a Gárgula, mas a luta parecia também estar acabando.\n")
        time.sleep(2)

        print("No chão se encontrava a Gárgula, e sobre ela o Lobo cravava suas garras no peito da estátua de pedra viva")
        print("A antiga Besta Abissal, termina o combate, arrancando a cabeça da Gárgula com sua boca.\n")
        time.sleep(2)

        print("O corpo da gárgula se desfaz em poeira. Deixando um orbe mágico no chão.")
        print("O lobo purificado então traz o orbe até a você e lhe entrega.\n")
        time.sleep(2)

        print("Ele te encarava como se esperasse um 'Bom trabalho'")
        print("Você esboça um sorriso e faz carinho na cabeça da grande besta.\n")
        time.sleep(2)

        print("Porém o orbe na sua mão se quebra, e um círculo mágico te cerca.")
        print("O grande lobo começa a ficar latir inquietamente\n")
        time.sleep(2)

        print("Sem ter o que fazer, você apenas troca olhares com a grande besta aliada.")
        print("Como uma maneira de deixá-lo tranquilo, você acena a cabeça, como se dissesse que tudo vai ficar bem.\n")
        time.sleep(2)

        print("Essa foi a última cena que o Lobo Guardião viu.")
        print("O círculo mágico sumiu, e junto dele você também.")
        print("Você foi teleportado...")
    
    # LUTA 2x1 CASO VOCÊ NÃO TENHA PURIFICADO OU N FOI PELO CAMINHO DA FLORESTA NEGRA
    elif (beastPurified ==False):
        print("Sem aliados ao seu lado, será um combate 2x1.\n")
        time.sleep(2)

        print("A primeira gárgula salta em sua direção, tentando lhe esmagar com suas garras.\n")
        print("O que você faz?\n")
        print("1- Golpear diretamente com sua espada")
        print("2- Usar poder sagrado contra ela")
        print("3- Bloquear com o escudo e contra-atacar\n")

        show_life(vida)
        escolha_gargula = input('> ')
        time.sleep(1)

        # 1º Gárgula
        if(escolha_gargula == '1'):
            print("\nVocê ergue sua espada e espera a gárgula se aproximar.")
            print("Quando ela está prestes a atacar, você também desfere seu golpe.")
            print("Ambos entram em um embate de força, você contra a gárgula.\n")
            time.sleep(2)

            print("Porém, a criatura utiliza da ponta afiada de sua cauda.")
            print("Ela desfere um golpe em seu peito, atravessando sua armadura.\n")
            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)
            time.sleep(2)

            print("Você então reúne mais força em sua espada.")
            print("O impacto destrói a mão pedregosa da gárgula.\n")
            time.sleep(2)

            print("Com um corte limpo vertical, você a divide em dois.")
            print("A criatura se desfaz em pó diante de você.\n")
            time.sleep(2)

            print("Mas ela deixa um objeto para trás.\n")
            print("Um orbe...\n")

            print("Você se agacha e pega o orbe.")

        elif(escolha_gargula == '3'):
            print("\nVocê firma seus pés no chão e ergue seu escudo para o impacto.")
            print("A gárgula colide contra você com força brutal.\n")
            time.sleep(2)

            print("Mas algo incrível acontece: a mão pedregosa da criatura se quebra.")
            print("Você aproveita a abertura e atravessa sua espada no peito da gárgula.")
            print("Ela se desfaz em pó, com sua lâmina ainda cravada em seu corpo.\n")
            time.sleep(2)

            print("Mas ela deixa um objeto para trás.\n")
            print("Um orbe...\n")

            print("Você se agacha e pega o orbe.")



        elif(escolha_gargula=='2' and helpedCivilian == False):
            print("\nVocê fecha os olhos em preces a Luminarie, pedindo mais poder.")
            print("Mas suas preces não são atendidas... ou melhor, foram ignoradas.\n")
            time.sleep(2)

            print("Aproveitando sua confusão, a gárgula desfere um golpe contra você.")
            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)
            time.sleep(2)

            print("\nA dor o desperta. Você contra-ataca rapidamente.")
            print("Com um corte horizontal, você divide a criatura ao meio.\n")
            time.sleep(2)

            print("Ela se desfaz em pó diante de você, sobrando apenas um objeto para trás.\n")

            print("Um orbe...\n")

            print("Você se agacha e pega o orbe, mas sua mente parece estar em outro lugar.")
            time.sleep(2)

            print("Sua mente está ocupada pensando no porquê suas preces não terem sido atendidas")

        elif(escolha_gargula =='2' and helpedCivilian == True):
            print("\nVocê fecha os olhos em preces a Luminarie, pedindo mais poder.")
            print("Suas preces foram atendidas, luz dourada começa a circular em sua volta.\n")
            time.sleep(2)

            print("Olhando para a gárgula você conjura seu milagre: \n")

            time.sleep(2)
            print("'Flammae divinae'\n")
            time.sleep(2)

            print("A gárgula é envolta em chamas sagradas.")
            print("Seu corpo de pedra se torna pó dourado e ela se desfaz instantaneamente.\n")
            time.sleep(2)

            print("Mas ela deixa um objeto para trás.\n")
            print("Um orbe...\n")
            time.sleep(2)

            print("Você se agacha e pega o orbe.")
            time.sleep(2)

        else:
            logout()        

        
        time.sleep(2)
        print("\nSua atenção agora é tomada pela segunda gárgula.")
        print("Ela se ergue aos céus utilizando suas asas e começa a cuspir uma onda de chamas em sua direção.\n")
        time.sleep(2)

        print("O que você faz?\n")
        print("1- Bloquear as chamas com o escudo")
        print("2- Correr das chamas\n")

        show_life(vida)
        escolha_segunda = input("> ")
        time.sleep(1)

        # 2º Gárgula
        if(escolha_segunda == '1'):
            print("\nVocê se aproxima do chão para minimizar as áreas de contato.")
            print("Ergue seu escudo diante de si, firme e preparado.\n")
            time.sleep(2)

            print("As ondas de chama atingem seu escudo.")
            print("O calor é infernal, mas sua defesa resiste.")
            print("Você não se fere, permanecendo firme contra o ataque.\n")

        elif(escolha_segunda == '2'):
            print("\nVocê tenta desviar das chamas, correndo para outro lugar.")
            print("As ondas se aproximam rapidamente e você se joga para esquivar.\n")
            time.sleep(2)

            vida, dano = random_damage(vida, armor)
            print(f"As chamas ainda atingem parte da sua perna")
            print(f"Você recebeu {dano} de dano")
            show_life(vida)
            time.sleep(2)
            time.sleep(2)

            print("\nAs queimaduras ardem intensamente, mas você se mantém de pé.")
            print("A gárgula continua sobrevoando, mas agora você está pronto para contra-atacar.\n")

        else:
            logout

        print("\nApós cuspir fogo, a gárgula agora voa em sua direção.\n")
        time.sleep(2)

        print("O que você faz?\n")
        print("1- Cortar as asas da gárgula")
        print("2- Confrontar diretamente")
        print("3- Lançar seu escudo contra a gárgula\n")

        show_life(vida)
        escolha_final_gargula = input("> ")
        time.sleep(1)

        if(escolha_final_gargula == '1'):
            print("\nA gárgula se aproxima rapidamente, voando contra você.")
            print("Você salta e realiza um corte preciso em suas asas.")
            print("Sem equilíbrio e sem capacidade de voo, ela desmorona perto da beira do telhado.\n")
            time.sleep(2)

            print("Você aproveita a chance e a empurra telhado abaixo.")
            print("A criatura despenca e se desfaz em pó ao atingir o chão.\n")

            print("Você derrotou as Gárgulas Gêmeas\n")

        elif(escolha_final_gargula == '2'):
            print("\nVocê e a gárgula disparam em direção um do outro.")
            print("O choque entre suas armas ecoa pelo telhado.\n")
            time.sleep(2)

            print("Vocês se atravessam no impacto.")
            print("A gárgula é partida ao meio e seu corpo vira pó.\n")
            vida, dano = random_damage(vida, armor)
            time.sleep(2)
           
            print("Mas você não saiu ileso, as garras da gárgula lhe feriram.")
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)

            print("\nVocê derrotou as Gárgulas Gêmeas\n")


        elif(escolha_final_gargula == '3'):
            print("\nVendo a gárgula vindo em alta velocidade, você pega seu escudo.")
            print("Acumula o máximo de força possível e o lança contra ela.\n")
            time.sleep(2)

            print("A gárgula não consegue desviar e recebe o ataque em cheio.")
            print("O escudo é mais duro que sua pele pedregosa.")
            print("Ele atravessa o corpo da gárgula, destruindo-a totalmente.\n")

            print("Você derrotou as Gárgulas Gêmeas\n")

        else:
            logout()

        time.sleep(2)
        print("Após a morte da segunda gárgula, o orbe que você pegou começa a brilhar.")
        print("Ele se quebra em suas mãos e um círculo mágico surge ao seu redor.\n")
        time.sleep(2)

        print("Você sente o chão desaparecer sob seus pés.")
        print("O círculo mágico o envolve completamente.")
        print("Em um instante, você é teletransportado...\n")

    return vida
   
#3º caminho: Sala de Entrada do Castelo
def warrior_castle_entrance(vida: int, armor: bool, helpedCivilian: bool, beastPurified: bool):
        time.sleep(2)
        print("\nVocê decide não perder tempo e avança diretamente para os portões do castelo.")
        print("Os portões entreabertos permite que você entre no castelo sem menores problemas...\n")

        print("\n=== ENTRADA DO TRONO DO ABISMO (CASTELO) ===")

        print("\nA entrada é uma sala imensa.")
        print("No centro, três criaturas caninas gigantes dormem pesadamente.")
        time.sleep(2)

        print("\nVocê encontrou Trio de Cães Infernais.\n")

        print("Do outro lado da sala, há um portão enorme, guardado por eles.\n")
        time.sleep(2)

        print("Logo você entende: aqueles cães são os guardas que defendem a sala antes do Trono real demoníaco.\n")
        time.sleep(2)

        print("O que você faz?\n")
        print("1- Aproveitar a vulnerabilidade e atacar")
        print("2- Tentar passar por eles sorrateiramente\n")

        show_life(vida)
        escolha = input("> ")
        time.sleep(1)

        if(escolha == '1' and beastPurified == True):
            print("\nVocê parte para o ataque contra as criaturas, aproveitando que estão dormindo.")
            print("Você se aproxima dos três cães e enfia sua espada em um deles.")
            print("O cão esfaqueado late de dor, acordando os outros.\n")
            time.sleep(2)

            print("Você tenta retirar a espada, mas o cão ainda não morreu.")
            print("Prontamente, você enfia a lâmina mais fundo até atingir seu coração.")
            print("Ele cai morto, mas o tempo gasto foi suficiente para outro cão fincar suas garras em você.\n")
            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)
            time.sleep(2)

            print("Você se livra das garras e recua.")
            print("Os dois cães remanescentes o encurralam, prontos para atacar.\n")
            time.sleep(2)

            print("De repente, você ouve um latido.")
            print("Um vulto dourado passa e ataca um dos Cães Infernais.")
            print("É a antiga Besta Abissal, purificada, que agora luta ao seu lado.\n")
            time.sleep(2)

            print("A luta está equilibrada: você contra um cão, e a Besta contra o outro.")
            print("O cãe infernal parte para cima de você em alta velocidade.\n")

            print("O que você faz?\n")

            print("1- Avançar com espada")
            print("2- Lançar escudo contra a criatura")
            print("3- Usar poder sagrado para enfrentá-lo")
            print("4- Desviar e contra-atacar")

            show_life(vida)
            escolha_cao = input("> ")
            time.sleep(1)
            
            if(escolha_cao == '1'):
                print("\nA criatura marcha em velocidade incrível contra você.")
                print("Você ergue sua espada, ruge o nome de Luminarie e avança contra o cão.\n")
                time.sleep(2)
                
                print("Ao se aproximarem, você desliza por baixo da criatura.")
                print("Sua espada arranca as patas da direita, fazendo o cão desabar.")
                print("Você se levanta e enfia sua espada na cabeça do Cão, matando-o.\n")
                time.sleep(2)

            elif(escolha_cao == '2'):
                print("\nVocê espera a criatura encurtar a distância.")
                print("Ergue seu escudo e segura-o com toda a força.\n")
                time.sleep(2)

                print("No momento certo, você gira e arremessa o escudo contra o cão.")
                print("Ele não consegue esquivar e recebe o choque em cheio, caindo atordoado.\n")
                time.sleep(2)

                print("Você aproveita o momento oportunuo e sobe encima da criatura.")
                print("Sua espada vai em encontro com a cabeça do cão, o matando-o")

            elif(escolha_cao == '3'):
                print("\nVocê fecha os olhos em preces a Luminarie, pedindo mais poder.")
                print("Suas preces foram atendidas, luz dourada começa a circular em sua volta.\n")
                time.sleep(2)

                print("Olhando para a criatura você conjura seu milagre: \n")

                time.sleep(2)
                print("'Flammae divinae'\n")
                time.sleep(2)

                print("O Cão Infernal é envolta em chamas sagradas.")
                print("Seu corpo é consumido pelas chamas\n")
                time.sleep(2)

                print("Sem forças o cão desaba, já sem vida")
                print("Sobrando apenas um corpo carbonizado.\n")
                time.sleep(2)

            elif(escolha_cao == '4'):
                print("\nVocê espera a criatura encurtar a distância, pronto para esquivar.")
                print("Mas o cão acelera ainda mais, surpreendendo você.")
                print("Ele morde seu ombro com força.\n")
                vida, dano = random_damage(vida, armor)
                print(f"Você recebeu {dano} de dano.")
                show_life(vida)
                time.sleep(2)

                print("Aproveitando a guarda baixa do cão, você atravessa sua espada em seu coração.")
                print("Ele cai morto diante de você.\n")
            
            else: 
                logout()
            
            time.sleep(2)
            print("Após matar o Cão Infernal, você direciona seu olhar para o Lobo Guardião.")
            print("A antiga Besta Abissal também terminou sua batalha, carregando a cabeça do Cão em sua boca.\n")
            time.sleep(2)

            print("Você derrotou o Trio de Cães Infernais")

            print("Mas a vitória não foi impune. O lobo está ferido.")
            print("Você se aproxima e ele te olha como se pedisse desculpas por não poder acompanhá-lo na próxima porta.\n")
            time.sleep(2)

            print("Você esboça um sorriso e acaricia sua cabeça.")
            print("Ordena que ele saia do castelo, pois era perigoso.")
            print("O pedido é aceito. Você vê o lobo mancando e saindo do castelo.\n")
            time.sleep(2)

            print("Você desvia o olhar dele e retorna ao portão à sua frente.")
            print("Você abre o portão e segue em direção a sala real do Trono do Abismo...\n")    
       
        elif(escolha =='1' and beastPurified == False):
            print("\nVocê parte para o ataque contra as criaturas, aproveitando que estão dormindo.")
            print("Você se aproxima dos três cães e enfia sua espada em um deles.")
            print("O cão esfaqueado late de dor, acordando os outros.\n")
            time.sleep(2)

            print("Você tenta retirar a espada, mas o cão ainda não morreu.")
            print("Prontamente, você enfia a lâmina mais fundo até atingir seu coração.")
            print("Ele cai morto, mas o tempo gasto foi suficiente para outro cão fincar suas garras em você.\n")
            vida, dano = random_damage(vida, armor)
            print(f"Você recebeu {dano} de dano.")
            show_life(vida)
            time.sleep(2)

            print("Você se livra das garras e recua.")
            print("Os dois cães remanescentes o encurralam, prontos para atacar.\n")
            time.sleep(2)

            print("O que você faz?\n")
            print("1- Usar milagre divino e atacá-los")
            print("2- Confiar na espada e enfrentar de frente")
            print("3- Provocar os cães\n")

            show_life(vida)
            escolha_cao_dupla = input("> ")
            time.sleep(1)
            
            if(escolha_cao_dupla == '1' and helpedCivilian == True):
                print("\nVocê rapidamente clama por ajuda de Luminarie através de orações.")
                print("Suas preces foram atendidas, uma aura dourada envolve seu corpo.\n")
                time.sleep(2)

                print("Olhando para uma das criaturas que marcha em sua direção, você conjura:")
                print("'Carcer Divinus'\n")
                time.sleep(2)

                print("Correntes douradas circulam em volta da criatura, queimando sua pele.")
                print("Você força as correntes em seu pescoço, quebrando-o.\n")
                time.sleep(2)

                print("Achando que você estava de guarda baixa, o outro cão avança.")
                print("Mas você apenas murmura: 'Flammae divinae'\n")
                time.sleep(2)

                print("O corpo do canino demoníaco é coberto por chamas douradas.")
                print("Rugindo de dor, a criatura falece, sobrando apenas um corpo carbonizado.\n")
                time.sleep(2)

                print("Você derrotou o Trio de Cães Infernais.\n")

            elif(escolha_cao_dupla == '1' and helpedCivilian == False):
                print("\nVocê rapidamente clama por ajuda de Luminarie através de orações.")
                print("Silêncio é sua resposta. Suas preces não foram atendidas.\n")
                time.sleep(2)

                print("Confuso, você hesita. Aproveitando o momento, uma das criaturas avança.")
                print("Por puro reflexo, você consegue desviar e recuar.\n")
                time.sleep(2)

                print("Ao escapar do golpe, seus olhos passam pela sala.")
                print("Você percebe correntes no chão e tochas nas paredes.")
                print("Os cães continuam atrás de você, babando e famintos.\n")
                time.sleep(2)

                print("O que você faz?\n")
                print("1- Ceifar os cães com sua espada")
                print("2- Utilizar das correntes da sala")
                print("3- Utilizar da tocha da sala\n")

                escolha_ambiente = input("> ")
                time.sleep(1)
            
                if(escolha_ambiente == '1'):
                    print("\nVocê decide confiar apenas em sua espada.")
                    print("Avança contra os cães e desfere cortes brutais.\n")
                    time.sleep(2)

                    print("Mas você também recebe danos")
                    vida, dano = random_damage(vida, armor)
                    print(f"Você recebeu {dano} de dano")
                    print("Após um combate intenso, ambos caem mortos e se desfazem em pó.\n")
                    time.sleep(2)
                    print("Você derrotou o Trio de Cães Infernais")


                elif(escolha_ambiente == '2'):
                    print("\nVocê pega as correntes soltas no chão.")
                    print("Quando um cão avança, você enrola em seu pescoço e o estrangula.")
                    print("O outro tenta atacar, mas você aproveita e crava sua espada em sua garganta.\n")
                    time.sleep(2)
                    
                    print("Ambos caem derrotados, deixando apenas cinzas no chão.\n")
                    print("Você derrotou o Trio de Cães Infernais")
                    
                elif(escolha_ambiente == '3'):
                    print("\nVocê corre até uma das tochas acesas na parede.")
                    print("Arranca-a e lança contra os cães.")
                    print("O fogo espalha-se pelo chão, forçando-os a recuar.\n")

                    print("Um deles tropeça nas chamas e você aproveita para cravar sua espada em seu peito.")
                    print("O outro tenta atacar, mas você gira e desfere um corte horizontal, matando-o também.\n")
                    time.sleep(2)

                    print("Você derrotou o Trio de Cães Infernais")


                else: 
                    logout()
            
            elif(escolha_cao_dupla == '2'):
                print("\nVocê decide confiar apenas em sua espada.")
                print("Avança contra os cães sem medo, enfrentando-os de frente.\n")
                time.sleep(2)

                print("O primeiro cão salta e você o corta verticalmente, partindo-o em dois.")
                print("O segundo aproveita e morde seu braço, mas você suporta a dor.\n")
                vida, dano = random_damage(vida, armor)
                print(f"Você recebeu {dano} de dano.")
                show_life(vida)
                time.sleep(2)

                print("Com um rugido de determinação, você atravessa sua espada no coração do último cão.")
                print("Ele cai morto, se desfazendo em pó.\n")

                print("Você derrotou o Trio de Cães Infernais.")
           
            elif(escolha_cao_dupla ==  '3'):
           
                print("\nVocê bate sua espada contra o escudo, provocando os cães.")
                print("Eles avançam furiosos, saltando ao mesmo tempo.\n")
                time.sleep(2)

                print("No salto, você gira sua lâmina em um arco poderoso.")
                print("Dois corpos caninos são cortados ao meio, se desfazendo em cinzas.")
                print("Você derrotou o Trio de Cães Infernais.")  
           
            else: 
                logout()

            print("Após derrotar as bestas, você caminha em direção ao último portão.")
            print("Receio e medo aparecem no seu coração, porém você tenta esquecer desses pensamentos respirando fundo...")
            print("Você abre o portão e segue em direção a sala real do Trono do Abismo...\n")    
       
        elif(escolha == '2' and beastPurified == True):
            
            print("\nVocê tenta passar pelo canto da sala até chegar ao portão.")
            print("Mas ao se aproximar, escuta rosnados raivosos.\n")
            time.sleep(2)

            print("Você se vira e vê os três Cães Infernais acordados.")
            print("Seu cheiro os despertou.\n")
            time.sleep(2)

            print("Antes que você pense em como lutar contra três inimigos, algo acontece.")
            print("Os três cães começam a se fundir em um só.\n")
            time.sleep(2)

            print("Sobrando apenas um cão, bem maior e mais monstruoso, agora com três cabeças.")
            print("É um Cérbero.\n")
            time.sleep(2)

            print("A criatura de três cabeças o encara com fome.")
            print("Antes que ela ataque, um vulto dourado passa e a joga para longe.")
            print("É a antiga Besta Abissal, purificada, que se posiciona ao seu lado.\n")
            time.sleep(2)

            print("Com uma troca de olhares, você entende que ela quer.")
            print("Como forma de devolver o favor, ela quer enfrentar a besta de três cabeças em seu lugar.\n")
            time.sleep(2)

            print("'Você tem certeza?'  você pergunta receoso para o Lobo Guardião.")
            print("Sua pergunta é respondida com lambidas no seu rosto.\n")
            time.sleep(2)
            
            print("O lobo uiva para você e acena com a cabeça.")
            print("Como se dissesse para você ir embora.\n")
            time.sleep(2)

            print("Mesmo receoso, você aceita a proposta.")
            print("Ao levar as mãos a grande porta sua frente, o Cérbero ruge ferozmente.")
            print("O Lobo Guardião, antiga Besta Abissal, ruge em resposta e parte para cima da criatura de três cabeças.\n")
            time.sleep(2)

            print("As bestas caninas se encontram e começa o embate mortal delas.")
            print("Você decide aproveitar e não deixar o sacríficio do lobo ser em vão.\n")
            time.sleep(2)
            
            print("Abrindo o último portão, o portão que dá acesso a sala real do castelo.")
            print("Sem exitar você passa por ela.\n")

        elif(escolha == '2' and beastPurified == False):
            print("\nVocê tenta passar pelo canto da sala até chegar ao portão.")
            print("Mas ao se aproximar, escuta rosnados raivosos.\n")
            time.sleep(2)

            print("Você se vira e vê os três Cães Infernais acordados.")
            print("Seu cheiro os despertou.\n")
            time.sleep(2)

            print("Antes que você pense em como lutar contra três inimigos, algo acontece.")
            print("Os três cães começam a se fundir em um só.\n")
            time.sleep(2)

            print("Sobrando apenas um cão, bem maior e mais monstruoso, agora com três cabeças.")
            print("É um Cérbero.\n")
            time.sleep(2)

            print("A criatura de três cabeças o encara com fome e avança contra você.\n")
            
            print("O que você faz?\n")
            print("1- Usar as correntes da sala ")
            print("2- Utilizar a tocha da parede para atacar")
            print("3- Confiar na espada e atacar de frente")
            print("4- Usar o portão como armadilha\n")

            show_life(vida)
            escolha_cerbero_one = input("> ")
            time.sleep(1)

            # ROUND 1 
            if(escolha_cerbero_one == '1'):
                print("\nVocê pega rapidamente as correntes soltas no chão.")
                print("Quando uma das cabeças avança, você enrola a corrente em seu pescoço.")
                print("Mas o Cérbero é muito mais forte do que você imaginava.\n")
                time.sleep(2)

                print("Ele puxa a corrente com violência, arrastando você pelo chão.")
                vida, dano = random_damage(vida, armor)
                print(f"Você recebeu {dano} de dano.")
                show_life(vida)
                time.sleep(2)
                print("Mesmo ferido, você aproveita a proximidade e crava sua espada em uma das cabeças.")
                print("O Cérbero ruge em dor, mas continua vivo.\n")

            elif(escolha_cerbero_one == '2'):
                print("\nVocê arranca uma tocha da parede e a lança contra o Cérbero.")
                time.sleep(1)
                print("As chamas atingem uma das cabeças, queimando seus olhos.")
                time.sleep(1)
                print("A criatura ruge em dor, mas continua avançando.\n")

            elif(escolha_cerbero_one == '3'):
                print("\nVocê ergue sua espada e avança contra o Cérbero.")
                print("O choque é brutal, você corta uma das cabeças, mas as outras duas o atacam.\n")
                vida, dano = random_damage(vida, armor)
                print(f"Você recebeu {dano} de dano.")
                show_life(vida)

            elif(escolha_cerbero_one == '4'):
                print("\nVocê corre até o portão e espera o Cérbero avançar.")
                time.sleep(1)
                print("No momento certo, abre parcialmente o portão e se esquiva.")
                time.sleep(1)
                print("A criatura colide contra a estrutura, ficando atordoada.\n")

            else: 
                logout()

            print("O Cérbero, mesmo ferido, ainda ruge e parte para um ataque final.\n")
            print("O que você faz?\n")
            print("1- Cravar sua espada no coração da criatura")
            print("2- Usar poder sagrado para destruí-la")
            print("3- Aproveitar o ambiente e esmagar a criatura contra o portão\n")
           
            show_life(vida)
            escolha_cerbero_two = input("> ")
            time.sleep(1)

            if(escolha_cerbero_two == '1'):
                print("\nVocê reúne todas as forças e avança contra o Cérbero.")
                print("Com um golpe certeiro, você crava sua espada em seu coração.")
                print("A criatura ruge uma última vez antes de cair morta, se desfazendo em cinzas.\n")

            elif(escolha_cerbero_two == '2'):
                print("\nVocê canaliza sua fé e invoca um milagre poderoso.")
                print("'Lux Divina!'")
                print("Um círculo de luz envolve o Cérbero, queimando suas três cabeças ao mesmo tempo.")
                print("A criatura se desfaz em cinzas diante de você.\n")

            elif(escolha_cerbero_two == '3'):
                print("\nVocê aproveita o portão quebrado e força o Cérbero contra ele.")
                print("Com um empurrão poderoso, a criatura é esmagada contra a estrutura.")
                print("O impacto destrói suas três cabeças, e ela se desfaz em pó.\n")

            else:
                logout

            time.sleep(2)
            print("Você derrotou o Cérbero sozinho.")
            print("Ferido e exausto, mas vitorioso, você se aproxima do portão à frente.")
            print("Pronto para abri-lo e seguir em direção ao Trono do Abismo...\n")
       
        else: 
            logout()     

        return vida

def warrior_final_boss(vida: int, armor: bool, helpedCivilian: bool, beastPurified: bool):
    time.sleep(2)
    print("\n=== SALA REAL DO TRONO DO ABISMO ===\n")
    time.sleep(2)

    print("Você atravessa o portão pesado e adentra a sala final.")
    print("O ambiente é colossal: pilares negros se erguem até o teto, cobertos por runas demoníacas que brilham em vermelho pulsante.")
    print("O chão é de pedra rachada, exalando calor e fumaça como se o próprio inferno respirasse sob seus pés.\n")
    time.sleep(2)

    print("No centro, um trono feito de ossos e ferro retorcido domina a visão.")
    print("Atrás dele, uma muralha de chamas eternas ilumina a sala com um brilho infernal, projetando sombras distorcidas que parecem se mover por conta própria.\n")
    time.sleep(2)

    print("O ar é pesado, sufocante, e cada passo ecoa como um desafio.\n")
    time.sleep(2)

    print("Sentado no trono, ergue-se lentamente o REI DEMÔNIO.")
    print("outrora um mago que caminhava entre os homens, agora um ser supremo corrompido pela escuridão absoluta.\n")
    time.sleep(2)

    print("Sua forma é colossal, com pele de obsidiana e veias incandescentes que brilham como lava.")
    print("Chifres curvados se erguem de sua cabeça, e suas asas negras se abrem, cobrindo quase toda a sala.")
    print("Seus olhos ardem como brasas, e sua voz ecoa como trovão:\n")
    time.sleep(2)

  
    print("'Aprecio sua coragem, herói...'\n")
    time.sleep(1)

    print("'Lembra muito a minha há algumas eras atrás.'\n")
    time.sleep(1)

    print("'A diferença é que comparado a ser o Herói, eu era alguém mais insignificante'\n")
    time.sleep(1)
    
    print("'Mas as coisas mudam não é? Aqui estou eu, alguém que era insignificante contra o herói dessa geração.'\n")
    time.sleep(1)
    
    print("'Já que veio até aqui, nobre tolo, te darei o que quer'\n")
    time.sleep(1)

    print("'Você provará o verdadeiro poder de Velkarys, a Mão do Abismo.'\n")
    
    time.sleep(2)

    print("Em suas mãos, ele carrega uma espada flamejante, forjada no fogo eterno, capaz de cortar não apenas carne, mas também alma.")
    print("Cada movimento dele faz o chão tremer, e a sensação é de que o próprio castelo se curva diante de sua presença.\n")
    time.sleep(2)

    print("O confronto final está prestes a começar...")

    print("O Rei Demônio avança com sua espada flamejante, o calor é sufocante.\n")
    
    print("O que você faz?\n")
    print("1- Bloquear com escudo e contra-atacar")
    print("2- Derrubar um pilar sobre ele")
    print("3- Tentar desviar e atacar pelas costas\n")

    show_life(vida)

    escolha_one = input("> ")
    time.sleep(1)
    if(escolha_one == '1'):
        print("\nVocê decide que o melhor ataque é a defesa.")
        print("Firmando seus pés no chão, você aguarda o Rei Demônio.\n")
        time.sleep(2)
        
        print("Velkarys então desce o golpe com sua espada flamejante.")
        print("Você ergue seu escudo com o máximo de força que você consegue.\n")
        time.sleep(2)
        
        print("O impacto é colossal, faíscas e brasas saem da colisão.")
        time.sleep(2)

        print("Porém o Rei Demônio não para, ele continua atacando continuamente.")
        print("A força é tanta que seus braços ficam dormentes.\n")
        time.sleep(2)

        print("Com esforço sobre-humano, você resiste e tenta contra-atacar")
        print("Você brande sua espada e desfere cortes ao Rei Demônio.")
        print("Atingindo seus braços, você pode ver brasas sendo arrancadas de sua carne.\n")
        time.sleep(2)

        print("Rugindo em fúria, o Rei Demônio ainda consegue realizar cortes em você e te dá um chute na barriga.")
        print("Fazendo você voar para trás.\n")
        vida,dano = random_damage(vida, armor)
        
        print(f"Você recebeu {dano} de dano")
        show_life(vida)
        
    elif(escolha_one == '2'):
        print("\nAntes do Rei Demônio te atacar, você corre em direção aos pilares e se esconde atrás deles")
        print("Ao ver que Velkarys se aproxima, confuso com a sua súbita fuga.")
        print("Você derruba o pilar sob ele.\n")
        time.sleep(2)
        
        print("O peso atinge o Rei Demônio, que ruge em fúria.")
        print("Você aproveita a distração e distribui cortes em seu peito.\n")
        time.sleep(2)

        print("Pego de surpresa e frustrado o Rei Demônio recua.")
        
    elif(escolha_one == '3'):
        print("\nVocê tenta desviar e atacar pelas costas.")
        print("Com agilidade, você rola pelo chão e se levanta atrás do Rei Demônio, acreditando ter encontrado uma abertura.")
        time.sleep(2)

        print("Mas seus olhos ardentes já previam sua movimentação.")
        print("Ele gira com velocidade sobrenatural, sua espada flamejante corta o ar em um arco devastador.\n")
        time.sleep(2)

        print("O impacto é brutal, a lâmina incandescente rasga sua defesa e o lança contra um dos pilares da sala.")
        print("O choque faz o chão tremer, e você sente o calor da espada queimando sua carne.\n")
        time.sleep(2)

        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)
        time.sleep(2)

        print("Mesmo ferido, você se levanta com esforço, apoiando-se na espada.")
        print("Você respira fundo, ignorando a dor, e se prepara para continuar a luta.")

    else:
        logout()
    
    time.sleep(2)
    print("O Rei Demônio solta uma risada sombria, como se estivesse se divertindo com a situação.")
    print("'Você é previsível, herói... mas ainda resiste. Isso me agrada.'\n")
    time.sleep(2)
    
    print("O Rei Demônio ergue sua mão e conjura uma magia negra, runas brilham no ar.\n")
    print("O que você faz?\n")
    print("1- Invocar um milagre divino para repelir a magia")
    print("2- Avançar diretamente com sua espada")
    print("3- Usar o portão quebrado como cobertura\n")
    show_life(vida)
    escolha_two = input("> ")
    time.sleep(1)
    
    if(escolha_two == '1' and helpedCivilian == True):
        print("\nVocê clama por Luminarie e ergue sua espada ao céu.")
        print("Runas douradas se formam ao seu redor, e uma explosão de luz divina rompe a na sua espada.")
        time.sleep(2)

        print("Você direciona sua espada ao Rei Demônio e seu feitiço.")
        print("'Radius Lucis'")
        print("Um feixe de luz puramente sagrado sai da sua espada.\n")
        time.sleep(2)
        print("O choque entre luz e trevas faz a sala inteira tremer.")
        print("O Rei Demônio é atingido em cheio, sua pele de obsidiana se despedaça em fragmentos incandescentes.")
        print("Ele ruge em dor, o som ecoa como mil trovões.\n")
    
    elif(escolha_two == '1' and helpedCivilian == False):
        print("\nVocê clama por Luminarie e ergue sua espada ao céu.\n")
        time.sleep(2)
         
        print("...\n")
        time.sleep(2)
         
        print("...\n")
        time.sleep(2)
         
        print("...\n")
        time.sleep(2)

        print("Suas preces não foram ouvidas.")
        print("Sem ter tempo para reagir, você é atingido em cheio pelo feitiço do Rei Demônio.\n")
         
        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano")
        show_life(vida)
        print()
        
        print("Você é arremessado com o impacto.\n")
        time.sleep(2)
        
        print("Enquanto levanta, você consegue ouvir as risadas de Velkarys se espalhar pela sala.\n")

        print("'Parece que sua amada Deusa te abandonou, pequeno Herói.' diz ele em tom de deboche")

    elif(escolha_two == '2'):
        print("\nVocê avança com sua espada, ignorando o medo.")
        print("Mas o Rei Demônio ergue a mão e libera sua magia negra.")
        time.sleep(2)

        print("Runas vermelhas explodem no ar, e uma onda de energia sombria o atinge em cheio.")
        print("Seu corpo é lançado contra o chão, o impacto faz o sangue ferver e a sala vibrar.\n")
        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)

        print("Enquanto levanta, você consegue ouvir as risadas de Velkarys se espalhar pela sala.\n")
        
    elif(escolha_two == '3'):
        print("\nVocê corre até o portão quebrado e se esconde atrás dele.")
        print("A magia negra explode contra a estrutura, estilhaços voam por toda a sala.")
        time.sleep(2)

        print("Você sente o calor da explosão, mas permanece vivo.")
        print("O Rei Demônio observa com desprezo, intacto, como se zombasse da sua tentativa de defesa.\n")

        print("'Patético... Sé só isso que você tem herói, a morte é a melhor solução...'")
    
    else:
        logout()
        
    time.sleep(1)
    print("'Lutando para sobreviver como um inseto...'\n")
    time.sleep(1)
    
    print("diz Velkarys com nojo evidente.\n")
    time.sleep(1)
    
    print("'Insetos devem ser queimados...'\n")
    time.sleep(1)

    print("O Rei Demônio abre suas asas negras e lança uma onda de fogo que consome toda a sala.\n")
    
    print("O que você faz?\n")
    
    print("1- Saltar sobre as chamas e atacar")
    print("2- Usar correntes da sala para prendê-lo")
    print("3- Tentar resistir ao fogo com o escudo\n")
    show_life(vida)

    escolha_three = input("> ")
    time.sleep(1)
    
    if(escolha_three == '1'):
        print("\nVocê salta sobre as chamas, sentindo o calor rasgar sua pele como lâminas incandescentes.")
        print("O ar é sufocante, mas sua coragem o impulsiona além do medo.")
        time.sleep(2)

        print("Com um grito de determinação, você atravessa o fogo e crava sua espada no peito do Rei Demônio.")
        print("O impacto é devastador, o som ecoa como trovões dentro da sala.")
        print("O Rei Demônio urra em fúria, suas asas negras se agitam violentamente.\n")

    elif(escolha_three == '2'):
        print("\nVocê corre até as correntes enferrujadas que jazem no chão da sala.")
        print("Com rapidez, tenta enrolá-las em torno das pernas do Rei Demônio.")
        time.sleep(2)

        print("Por um instante, parece que você conseguiu prendê-lo.")
        print("Mas sua força é descomunal: ele se liberta com facilidade e puxa você junto.")
        print("Seu corpo é arrastado pelo chão como se fosse nada, ossos e músculos protestam contra o impacto.\n")
        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano.")
        show_life(vida)

    elif(escolha_three == '3'):
        print("\nVocê ergue seu escudo contra a onda de fogo, tentando resistir ao calor infernal.")
        print("As chamas colidem com o metal, o impacto é tão forte que o chão treme.")
        time.sleep(2)

        print("Mas o calor é insuportável: o escudo começa a derreter nas bordas, o metal se contorce.")
        print("Seu braço é queimado pelas chamas que atravessam a defesa, a dor é lancinante.\n")
        vida, dano = random_damage(vida, armor)
        print(f"Você recebeu {dano} de dano")
        show_life(vida)

        print("Você resiste, mas o escudo agora está parcialmente destruído.")
        print("O Rei Demônio observa com um sorriso cruel, como se saboreasse sua agonia.\n")

    else:
        logout()
    
    time.sleep(2)
    print("'Foi divertido enquanto durou, garoto'\n")
    print("Determinado a acabar com o embate.\n")
    time.sleep(2)
    
    print("O Rei Demônio ergue sua espada flamejante e a enterra no chão com força descomunal.")
    print("O impacto faz a sala inteira tremer, rachaduras se espalham pelo piso.\n")
    time.sleep(2)

    print("Ao redor dele surgem cinco círculos mágicos, cada um brilhando com uma cor distinta.")
    print("Fogo, Água, Terra, Ar e Vento, os elementos primordiais dançam em torno da criatura.\n")
    time.sleep(2)

    print("Os círculos começam a girar e se fundem em um só, multicolorido, como um arco-íris distorcido.")
    print("A energia é tão intensa que o ar vibra e o som ecoa como mil sinos quebrados.\n")
    time.sleep(2)

    print("Mas não termina aí, um sexto círculo surge, negro como a noite sem estrelas.")
    print("O clima fica sombrio, a sala mergulha em trevas, e até as chamas eternas parecem vacilar.\n")
    time.sleep(2)

    print("O Rei Demônio funde a magia multicolorida com o círculo negro.")
    print("Uma aura apocalíptica envolve seu corpo, e você sente que o próximo ataque destruirá tudo.\n")
    time.sleep(2)

    print("O que você faz, Herói?\n")
    time.sleep(2)
    print("1- Sacrificar-se\n")

    escolha_final = input("> ")
    time.sleep(1)

    if(escolha_final == '1' and helpedCivilian == False):
        print("\nVocê respira fundo e entende que não há outra escolha.")
        print("Com coragem, decide entregar sua vida para salvar o mundo.\n")
        time.sleep(2)

        print("Você reúne todas as forças restantes e avança contra o Rei Demônio.")
        print("Ele libera sua magia devastadora, um feixe multicolorido envolto em trevas.")
        print("Mas você não recua, você é o herói daquele mundo.\n")
        time.sleep(2)

        print("Você clama pela benção de Luminarie, uma última vez.\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)

        print("Suas preces não foram atendidas, mesmo assim você não para")
        print("Se jogando de frente a magia, recebendo ela de braços abertos.\n")
        time.sleep(2)

        print("O choque é indescritível, seu corpo e a magia mortal colidem, a sala inteira se despedaça.")
        print("Você segue firme, enfrentando a magia, passo por passo")
        time.sleep(2)
        
        print("Porém seu corpo vai pagando o preço, sendo despedaçado também.")
        print("Sua resistêcia e determinação são impressionante, você alcança o Rei Demônio, que te encara incrédulo.\n")
        time.sleep(2)
        
        print("Sua lâmina atravessa o coração do Rei Demônio ao mesmo tempo que sua magia consome você.\n")
        time.sleep(2)

        print("Ambos caem. O castelo treme com o choque final.")
        print("Os círculos mágicos se desfazem, e as chamas eternas se apagam.")
        print("O silêncio toma conta do Trono do Abismo.\n")
        time.sleep(2)
        
        print("Suas pálpebras pesam... O teto daquela sala vai ficando embaçado em sua visão.")
        print("Então essa é a sensação de morrer?\n")
        time.sleep(2)
        
        print("Pensando na morte, foi como você chegou nela.")
        print("Você fecha seus olhos pela última vez, um sorriso permanece no seu rosto.\n")
        time.sleep(2)

        print("O Rei Demônio foi derrotado, mas ao custo da sua própria vida.")
        print("Seu sacrifício será lembrado como a vitória final contra a escuridão.\n")
        time.sleep(2)

        print("O mundo está livre do Abismo, graças ao seu último ato de coragem.\n")
        time.sleep(2)

        restart()

    elif(escolha_final == '1' and helpedCivilian == True and beastPurified == False):
        print("\nVocê respira fundo e entende que não há outra escolha.")
        print("Com coragem, decide entregar sua vida para salvar o mundo.\n")
        time.sleep(2)

        print("Você reúne todas as forças restantes e avança contra o Rei Demônio.")
        print("Ele libera sua magia devastadora, um feixe multicolorido envolto em trevas.")
        print("Mas você não recua, você é o herói daquele mundo.\n")
        time.sleep(2)

        print("Você clama pela benção de Luminarie, uma última vez.\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)

        print("Na sua cabeça uma voz acolhedora e gentil vibra.\n")
        time.sleep(2)

        print("'Vá minha criança, você consegue...'")
        print("Era a voz de Luminarie, a Deusa da Luz e da Justiça")
        time.sleep(2)
        
        print("Suas preces foram atendidas")
        print("Seu corpo explode em energia dourada.\n")
        time.sleep(2)

        print("Sua espada é tomada por chamas douradas")
        print("Com sua Deusa ao seu lado, nada pode te deter.\n")
        time.sleep(2)

        print("Você então, grita reunindo toda sua coragem e força e avança.")
        print("Se jogando de frente a magia, recebendo ela de braços abertos.\n")
        time.sleep(2)

        print("O choque é indescritível, seu corpo e a magia mortal colidem, a sala inteira se despedaça.")
        print("Você segue firme, enfrentando a magia, passo por passo")
        time.sleep(2)
        
        print("Porém seu corpo vai pagando o preço, sendo despedaçado também.")
        print("Sua resistêcia e determinação são impressionante, você alcança o Rei Demônio, que te encara incrédulo.\n")
        time.sleep(2)
        
        print("Sua lâmina atravessa o coração do Rei Demônio ao mesmo tempo que sua magia consome você.\n")
        time.sleep(2)

        print("Ambos caem. O castelo treme com o choque final.")
        print("Os círculos mágicos se desfazem, e as chamas eternas se apagam.")
        print("O silêncio toma conta do Trono do Abismo.\n")
        time.sleep(2)
        
        print("Suas pálpebras pesam... O teto daquela sala vai ficando embaçado em sua visão.")
        print("Então essa é a sensação de morrer?\n")
        time.sleep(2)
        
        print("O Rei Demônio foi derrotado, mas ao custo da sua própria vida.")
        print("Seu sacrifício será lembrado como a vitória final contra a escuridão.\n")
        time.sleep(2)

        print("O mundo está livre do Abismo, graças ao seu último ato de coragem...\n")
        time.sleep(2)

        print("Você fecha seus olhos pela última vez, um sorriso permanece no seu rosto.")
        print("Então esse é meu o fim?\n")
        time.sleep(2)

        print("...\n")
        time.sleep(2)
        
        print("...\n")
        time.sleep(2)
        
        print("...\n")
        time.sleep(2)

        print("'Não minha criança, não é...'")
        print("A voz de Luminarie invade sua mente.\n")

        print("Você então abre os olhos")
        print("Em sua frente você vê a Deusa.\n")
        time.sleep(2)

        print("Seus cabelos brancos reluzem como prata, seus olhos dourados brilham como a maior das luzes sagradas que você já viu.")
        print("Dona de uma beleza radiante, vestia trajes simples de linho, mas portava a elegância de uma verdadeira divindade.\n")
        time.sleep(2)

        print("Você percebe que seu corpo está radiando energia sagrada.")
        print("A Deus estava te curando, cada ferimento lentamente se fechava, cada dor se dissipava.\n")
        time.sleep(2)

        print("Antes que pudesse agradecer, ela fala com você:\n")
        time.sleep(2)

        print("'Estou orgulhosa de você, minha criança... Obrigada.'\n")
        time.sleep(2)

        print("Sua imagem começa a se desfazer em várias partículas de luz, como estrelas se dispersando no céu.")
        print("Mas antes de desaparecer completamente, você consegue ver o sorriso em seu rosto.\n")
        time.sleep(2)

        print("Você encara o teto enquanto ainda está deitado, sentindo seus ferimentos abertos lentamente curar.")
        print("O cansaço das batalhas te atropelam, você fecha os olhos.")
        print("Mas dessa vez não para aceitar a morte mas celebrar a vida, e a sua vitória.\n")
        time.sleep(4)
        
        restart()

    elif(escolha_final == '1' and beastPurified == True and helpedCivilian == True):
        print("\nVocê respira fundo e entende que não há outra escolha.")
        print("Com coragem, decide entregar sua vida para salvar o mundo.\n")
        time.sleep(2)

        print("Você reúne todas as forças restantes e avança contra o Rei Demônio.")
        print("Ele libera sua magia devastadora, um feixe multicolorido envolto em trevas.")
        print("Mas você não recua, você é o herói daquele mundo.\n")
        time.sleep(2)

        print("Você clama pela benção de Luminarie, uma última vez.\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)
      
        print("...\n")
        time.sleep(2)

        print("Na sua cabeça uma voz acolhedora e gentil vibra.\n")
        time.sleep(2)

        print("'Vá minha criança, você consegue...'")
        print("Era a voz de Luminarie, a Deusa da Luz e da Justiça")
        time.sleep(2)
        
        print("Suas preces foram atendidas")
        print("Seu corpo explode em energia dourada.\n")
        time.sleep(2)

        print("Sua espada é tomada por chamas douradas")
        print("Com sua Deusa ao seu lado, nada pode te deter.\n")
        time.sleep(2)

        print("Você então, grita reunindo toda sua coragem e força e avança.")
        print("Se jogando de frente a magia, recebendo ela de braços abertos.\n")
        time.sleep(2)

        print("O choque é indescritível, seu corpo e a magia mortal colidem, a sala inteira se despedaça.")
        print("Você segue firme, enfrentando a magia, passo por passo")
        time.sleep(2)
        
        print("Porém seu corpo vai pagando o preço, sendo despedaçado também.")
        print("Sua resistêcia e determinação são impressionante, você alcança o Rei Demônio, que te encara incrédulo.\n")
        time.sleep(2)
        
        print("Sua lâmina atravessa o coração do Rei Demônio ao mesmo tempo que sua magia consome você.\n")
        time.sleep(2)

        print("Ambos caem. O castelo treme com o choque final.")
        print("Os círculos mágicos se desfazem, e as chamas eternas se apagam.")
        print("O silêncio toma conta do Trono do Abismo.\n")
        time.sleep(2)
        
        print("Suas pálpebras pesam... O teto daquela sala vai ficando embaçado em sua visão.")
        print("Então essa é a sensação de morrer?\n")
        time.sleep(2)
        
        print("O Rei Demônio foi derrotado, mas ao custo da sua própria vida.")
        print("Seu sacrifício será lembrado como a vitória final contra a escuridão.\n")
        time.sleep(2)

        print("O mundo está livre do Abismo, graças ao seu último ato de coragem...\n")
        time.sleep(2)

        print("Você fecha seus olhos pela última vez, um sorriso permanece no seu rosto.")
        print("Então esse é meu o fim?\n")
        time.sleep(2)

        print("...\n")
        time.sleep(2)
        
        print("...\n")
        time.sleep(2)
        
        print("...\n")
        time.sleep(2)

        time.sleep(2)
        print("\nVocê sente um líquido entrar em sua via oral.")
        print("O gosto é doce, mas cítrico, e logo você sente suas forças voltarem.")
        print("Seus ferimentos começam a se curar lentamente.\n")
        time.sleep(2)

        print("Abrindo os olhos, você se depara com uma grande criatura quadrúpede.")
        print("Seu pelo é dourado escuro e seus olhos azuis brilham intensamente.")
        print("Era o Lobo Guardião, a antiga Besta Abissal, agora ao seu lado para te salvar.\n")
        time.sleep(2)

        print("Em sua boca, você percebe um frasco, uma poção de cura.")
        print("Ao ver você acordando, o lobo rapidamente começa a lamber seu rosto.")
        print("Você sorri, sentindo o afeto daquela criatura.\n")
        time.sleep(2)

        print("'Obrigado, amigão... você me salvou dessa vez.'")
        print("O lobo apenas uiva baixinho enquanto você acaricia sua cabeça lentamente.\n")
        time.sleep(2)

        print("E então, em sua mente, você ouve uma voz suave e poderosa")
        print("'Estou orgulhosa de você, minha criança... Obrigada.'")
        print("Era a voz de Luminarie. Você sorri em satisfação.\n")
        time.sleep(2)

        print("Virando sua atenção novamente ao lobo, você diz")
        print("'Vamos embora, amigão.'\n")
        time.sleep(2)

        print("O Lobo Guardião se abaixa e te coloca em suas costas.")
        print("Com passos firmes, vocês começam a se dirigir para fora do castelo.\n")
        time.sleep(2)

        print("'Pensando bem, eu ainda não te dei um nome, né?'")
        print("'Que tal Aurion, dourado como a luz dos milagres?'")
        print("Você diz com um sorriso.\n")
        time.sleep(2)

        print("O Lobo uiva feliz, aceitando o nome.")
        print("Você sorri e acaricia seu pescoço.\n")
        time.sleep(2)

        print("'Então é isso... vamos embora, Aurion. Vamos para casa.'\n")
        time.sleep(2)

        print("E assim vocês seguem caminho, um herói nas costas de um Lobo Guardião.")
        print("Sumindo juntos na imensidão do horizonte.\n")
        time.sleep(2)

        print("É assim que sua jornada termina...")
        time.sleep(4)

        restart()
    
    else:
        logout()

