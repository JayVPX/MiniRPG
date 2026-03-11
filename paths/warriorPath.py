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

    if(escolha_caminho == '1'):
        print("\nVocê decide não perder tempo e avança diretamente para os portões do castelo.")
        print("Os portões entreabertos permite que você entre no castelo sem menores problemas...\n")

        print("\n=== ENTRADA DO TRONO DO ABISMO (CASTELO) ===")
        # print("Assim que atravessa o limiar, três Cães Infernais surgem das sombras, rosnando com fúria.")
        # print("Seus olhos ardem em chamas e suas presas brilham como ferro em brasa.")
        # print("O combate é inevitável.\n")

    elif(escolha_caminho == '2'):
        print("\nVocê observa as muralhas e decide procurar uma entrada alternativa.")
        print("Após explorar, encontra uma escada quebrada que leva até os telhados.")
        print("Com esforço, você escala e alcança as alturas do castelo.\n")


    elif(escolha_caminho == '3'):
        print("\nVocê decide seguir o resquício de energia divina.")
        print("Ele o guia até uma viela escondida, onde ruínas antigas repousam.")
        print("Entre as sombras, você encontra um Antigo Templo, esquecido pelo tempo.")
        print("Apesar de destruído, ainda há uma aura de santidade no local.")
        print("Talvez aqui você encontre respostas... ou poder.\n")

    else:
        logout()

    return vida, escolha_caminho

# 1º caminho:  Templo Antigo
def warrior_old_temple(armor: bool, helpedCivilian: bool):
    print()

# 2º caminho: Telhado do Castelo
def warrior_rooftop(vida: bool, armor: bool, helpedCivilian: bool):
    print()

#3º caminho: Sala de Entrada do Castelo
def warrior_castle_entrance(vida: bool, armor: bool, helpedCivilian: bool):
    print()