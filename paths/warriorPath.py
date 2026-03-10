from utils import *
import time

def warrior_start(vida: int, armor: bool):
    time.sleep(2)
    print("\n=== PORTÕES DA FORTALEZA DE VELKARYS ===\n")

    print("Diante de você se erguem os imensos muros de Velkarys.")
    print("Não é apenas uma fortaleza... mas uma cidade inteira aprisionada atrás de muralhas negras.")
    print("Torres de pedra escura perfuram o céu encoberto por nuvens vermelhas, enquanto chamas demoníacas queimam em grandes brasões ao longo das muralhas.")
    print("O ambiente ao redor da fortaleza também não é amigável, a floresta negra vive ao redor, consumindo qualquer luz que ouse repousar.")
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
            print("Mas chegou ao fim, e o silêncio novamente reinou naquele rescinto.\n")

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

        escolha_sub = input("> ")
        time.sleep(1)

        if escolha_sub == "1":
            print("A proposta não parece tão ruim... ")
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


    
def warrior_black_forest(vida: int, armor: bool, helpedCivilian: bool):
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

            print("1- Ajudar os aldeões.")
            print("2- Ignorar e continuar sua missão.\n")

            show_life(vida)

            escolha_sub = input("> ")
            time.sleep(1)

            if(escolha_sub == '1'):
                print()

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

            print("Virando de costas contra os gritos de desespero, você segue seu caminho...")

            helpedCivilian = False
        else:
             logout()
        return vida, helpedCivilian

def warrior_entering_fortress(vida: int, armor: bool):
        print()

