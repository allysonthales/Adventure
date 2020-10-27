# The script of the game goes in this file.
init python:
    import random # Get the random functionality for Python

    def getNumber(x):
        options = range(x) # Create a list of numbers
        return random.choice(options) 

# Declare characters used by this game. The color argument colorizes the
# name of the character.

screen menu1:
    imagemap:
        ground "images/normal.jpg"
        hover "images/emcima.jpg"

        hotspot(1112, 2, 135, 143) clicked Jump("iniciar")
        hotspot(1111, 153, 135, 143) clicked Jump("menu")
        hotspot(1111, 303, 135, 143) clicked Jump("exit")


define mestre = Character("Mestre", color = '#00ff37', image = "mestreNaLogo")
define pai = Character("Pai", image = "paiNaLogo")
define protagonista = Character("[nomeDoProtagonista]", color = '#2200ff', image = "protagonistaNaLogo")
define guarda = Character("Guarda", image = "guardaNaLogo")
define meninaInicial = Character("Desconhecida", image = "meninaInicialNaLogo")
define menina = Character("Kath", image = "meninaNaLogo")

image side mestreNaLogo = "mestreside2.png"
image side guardaNaLogo = "guarda2.png"
image side protagonistaNaLogo = "jogador2.png"
image side meninaNaLogo = "menina.png"
image side meninaInicialNaLogo = "menina_inicial.png"
image side paiNaLogo = "pai.png"





# The game starts here.

label start:

    $vida = 5

    # atributos guarda
    $guarda_agressividade = 5
    $guarda_carisma = 1
    $guarda_sorte = 3

    $opcao = 0

    # Status
    $machucado = 0
    $cansado = 0

    # variaveis auxiliares para o resultado
    $resultado_protagonista = 0
    $resultado_rival = 0

    play music "/audio/backgroundMusic.mp3"
    call screen menu1
label sobre:



label iniciar:

    stop music fadeout 1.0
    scene background
    with dissolve

    mestre "Bem vindo!! Eu irei ser o mestre de seu jogo hoje."
    mestre "Primeiro, me diga seu nome."
    $nomeDoProtagonista = renpy.input("Qual é o seu nome?")
    if nomeDoProtagonista == "":
        mestre "hmnnn, um jogador misterioso. Tudo bem, te chamarei de protagonista."
        $nomeDoProtagonista = "protagonista"
    mestre "Excelente %(nomeDoProtagonista)s, espero que você tenha uma experiência incrivel hoje."
    mestre "Você pode distribuir 5 pontos em 'agressividade', 'carisma' e 'sorte'."
    mestre "Esses pontos serão determinantes para os resultados de suas escolhas, ao longo da jornada"
    mestre "Quantos pontos você deseja adicionar em {b}Agressividade{/b}?"

    #Variaveis auxiliares da escolha
    $ok = 1
    while ok:
        $agressividade_ok = 1
        $carisma_ok = 1
        $sorte_ok = 1
        $pontos = 5
        while agressividade_ok: 
            $agressividade = int(renpy.input("Quantos pontos em Agressividade?"))
            if (agressividade >= 0) and (agressividade <= 5):
                $agressividade_ok = 0
                $pontos -= agressividade
            else:
                "Valor invalido, tente novamente um valor entre 0 e 5"

        mestre "Você ainda tem %(pontos)s para distribuir"
        while carisma_ok:
            $carisma = int(renpy.input("Quantos Pontos em Carisma?"))
            if carisma >= 0 and carisma <= pontos:
                $carisma_ok = 0
                $pontos -= carisma
            else:
                "Valor invalido, tente novamente um valor entre 0 e %(pontos)s"
        mestre "Otimo, você ainda tem %(pontos)s para distribuir"
        while sorte_ok:
            $sorte = int(renpy.input("Quantos pontos em Sorte?"))
            if sorte >= 0 and sorte <= pontos:
                $sorte_ok = 0
                $pontos -= sorte
            else:
                "Valor invalido, tente novamente um valor entre 0 e %(pontos)s"
        $ok = 0


    mestre "Certo, agora você tem:"
    mestre "%(agressividade)s pontos em Agressividade, %(carisma)s pontos em Carisma e %(sorte)s pontos em Sorte"

    jump s1

label s1:
    mestre "Você irá se aventurar nas terras de BLABLA e tomará decisões como um jovem morador de uma vila."
    mestre "Esta vila fica localizada ao extremo norte de um reino imperial, e você é o filho do chefe desta vila"
    mestre "Na vila, todo dia é quase sempre igual, e você, como filho do chefe da vila, tem muitas responsabilidades, mas essa tranquilidade está preste a acabar…"
    mestre "Alguns soldados aparecem do lado de fora da vila, o que não é algo comum, aliás, nunca tinham visitado aquela vila por estar tão longe do reino. Eles estão se aproximando do portão principal."
    mestre "Você observa enquanto os guardas se aproximam da vila"
    jump s2

label s2:

    protagonista "Olá, me chamo Tillamethe e sou o filho do chefe desta vila, em que posso ajudá-los?"
    guarda "Olá meu jovem, Somos da guarda real de Scar e estamos em missão, atrás de um criminoso que estaria se escondendo em sua vila."
    guarda "Gostaríamos de sua cooperação."
    mestre "O que você faz?"
    menu:
        "Você não permite a entrada, até que seu pai esteja ciente da situação":
            jump s3
        "Você permite uma entrada amigável":
            jump s4

label s3:
    mestre "Claramente o líder da guarda fica incomodado com sua resposta, mas sua face muda rapidamente para um sorriso sem graça e diz:"
    guarda "Vamos meu jovem, não dificulte as coisas para você."
    mestre "Você precisa escolher:"
    menu:
        "mantém sua decisão (Utiliza seus pontos de agressividade)":
            jump s5
        "Muda de ideia e libera a passagem":
            jump s4

label s4:

    mestre "O líder dos guardas agradece e faz um sinal para seus guardas começarem procurar pela vila."
    jump s6

label s5:

    $resultado_protagonista = getNumber(agressividade)
    $resultado_rival = getNumber(guarda_agressividade)
    "Seu numero de combate foi: %(resultado_protagonista)s"
    "O numero de combate do guarda foi: %(resultado_rival)s"
    if resultado_protagonista >= resultado_rival:
        "Você ganhou a disputa"
        mestre "O guarda está claramente irritado, e não para de encarar você"
        jump s6
    else:
        "Você perde a disputa"
        mestre "Você percebe o sorriso falso sumindo lentamente do rosto do líder dos guardas"
        mestre "e em um movimento muito rápido, ele desfere um chute na altura do seu peito."
        mestre "Você recebeu o status de {b}MACHUCADO{/b}"
        mestre "Os guardas começam a entrar na vila."
        $machucado = True
        jump s6

label s6:

    mestre "Enquanto os guardas entram na vila, o chefe da vila, seu pai, aparece e está claramente bem irritado."
    pai "O que vocês fazem aqui?"
    pai "Saiam dessa vila, vocês e seu rei sabem que não são bem vindos aqui. Fora!"
    pai "FORA!!"
    mestre "Você nunca tinha visto seu pai tão nervoso assim"
    mestre "Para a surpresa de todos, o líder dos guardas ordenou que todos saíssem, e enquanto saiam da vila, disse:"
    guarda "Não se preocupe, não vai demorar para vocês se arrependerem disso."
    pai "Vamos filho, vamos para casa."
    mestre "e assim vocês foram para casa."
    jump s7

label s7:

    mestre "Chegando em casa, seu pai prepara duas bebidas quentes, entrega uma para você e deixa a outra em cima da mesa."
    mestre "Você se assusta quando percebe que tem alguém saindo de baixo da mesa e sentando na cadeira."
    mestre "parece que tinha uma jovem garota escondida ali e ela está bem assustada, mas claramente está tentando esconder isso, tentando passar um ar de coragem e destemida."
    meninaInicial "Obrigada"
    mestre "Você olha para seu pai e ele parece bem nervoso e diz:"
    pai "Filho, não temos muito tempo, ela vai te contar o que está acontecendo."
    mestre "enquanto termina de falar, seu pai vai para a porta e fica verificando se ninguém se aproxima."
    mestre "Você olha para a garota, sentada e tomando chá, e pergunta:"
    protagonista "Quem é você?"
    jump s8

label s8:

    menina "Me chamo Kath, sou aluna de um velho amigo de seu pai."
    menina "Fui enviada até aqui porque estamos em uma situação bem crítica"
    menina "e o reino está atrás deste pergaminho que carrego, contendo a localização do livro secreto."
    menu:
        "conte mais sobre esse amigo do meu pai":
            jump s9
        "conte mais sobre esse livro":
            jump s10

label s9:

    menina "O meu mentor é Alucard, um amigo do seu pai."
    menina "Eles estudaram juntos na universidade, ambos se especializando em mitologia nórdica"
    menu:
        "estudou com meu pai? mas ele nunca saiu da vila":
            jump s11
        "e esse livro?":
            jump s12

label s10:

    menina "É um livro muito valioso, onde contém o segredo de como liberar os poderes da coroa élfica."
    menina "Poderes esse que poderiam tornar seu usuário em um exército de um homem só."
    menu:
        "Isso só pode ser lenda":
            jump s13
        "E onde está essa coroa?":
            jump s14

label s11:

    menina "Seu pai era um dos melhores alunos, e ia até o desconhecido em busca de mais informações sobre os elfos."
    menina "Inclusive, foi em uma incursão que ele encontrou sua mãe."
    menu:
        "Como assim, encontrou?":
            jump s15

label s12:

    menina "É um livro muito valioso, onde contém o segredo de como liberar os poderes da coroa élfica."
    menina "poderes esse que poderiam tornar seu usuário em um exército de um homem só."
    menu:
        "Isso só pode ser lenda":
            jump s13
        "e onde está essa coroa?":
            jump s14

label s13:

    menina "Não é lenda!"
    menina "Houve muito estudo para que tivéssemos uma pista válida, mas agora isso nos colocou em risco."
    menu:
        "Que tipo de risco?":
            jump s15

label s14:

    menina "Precisamos ler atentamente o que está escrito para decifrar"
    menina "Eu ainda não consegui, por isso vim buscar ajuda."
    jump s15

label s15:

    mestre "Neste momento, seu pai corre em sua direção, tira a garota da cadeira e leva vocês para a saída dos fundos."
    mestre "Enquanto correm sem entender, ouvem gritos e cavalos correndo."
    pai "Os guardas estão invadindo e incendiando a vila"
    pai "Vocês precisam fugir, Tillamethe, fuja com ela, saiam da vila pelo buraco que tem ao norte do muro da vila."
    mestre "Você não consegue responder seu pai, e vê uma flecha o atingindo na perna, seu pai cai e diz"
    pai "rápido, vocês não tem tempo!!"
    mestre "Guardas que entraram na casa correm em sua direção. Qual é sua decisão?"
    menu:
        "tentar carregar seu pai":
            jump s16
        " levar a garota até o muro e fugir":
            jump s17

label s16:

    if machucado == True:
        mestre "Você não consegue carregar seu pai, os guardas o alcançam e desfere um golpe de espada em seu ombro."
        mestre "Você perde 1 de vida"
        $vida -= 1
        jump s15
    else:
        mestre "Você consegue carregar seu pai até o muro."
        mestre "Praticamente o arrastando, mas claramente ele não vai conseguir andar. Seu pai diz:"
        pai "vão os dois, precisamos que vocês consigam impedir que Scar obtenha os poderes da coroa! VÃO!"
    jump s19

label s17:

    mestre "Você corre até o muro e mostra a passagem para Kath, olha pra trás e vê que um guarda está amarrando seu pai."
    mestre "você precisa decidir:"
    menu:
        "volta para tentar salvar seu pai":
            jump s18
        "passa pelo muro com Kath":
            jump s19

label s18:

    mestre "você volta e empurra o guarda, ao se virar e tentar levantar seu pai, você leva um golpe de espada no ombro."
    mestre "você está morto e perde 1 vida."
    $vida -= 1
    jump s17

label s19:

    mestre "Você passa pelo muro com Kath, bastante confuso com o que aconteceu nos últimos minutos."
    mestre "mas entende que agora irá ser responsável por algo muito importante."
    jump s20


label exit:

   # quit(confirm=None) #não ta funcionando <<


    # This ends the game.

    return
