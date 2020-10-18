# The script of the game goes in this file.
init python:
    import random # Get the random functionality for Python
    def getNumber(x):
        options = range(x) # Create a list of numbers 0 to 49
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
define pai = Character("Pai")
define protagonista = Character("[nomeDoProtagonista]", color = '#2200ff', image = "protagonistaNaLogo")
define guarda = Character("Guarda", image = "guardaNaLogo")

image menuBackground = "images/menuBackground.jpg"
image background = "images/background.jpg"
image protagonista = "images/jogador.jpg"
image mestre = "images/mestre.jpg"
image pai = "images/pai.jpg"
image guarda = "images/guarda.png"

image side mestreNaLogo = "mestreside2.png"
image side guardaNaLogo = "guarda2.png"
image side protagonistaNaLogo = "jogador2.png"






# The game starts here.

label start:

    $test = getNumber(10)
    "%(test)s"

    play music "/audio/backgroundMusic.mp3"
    call screen menu1

    # atributos guarda
    $guarda_agressividade = 5
    $guarda_carisma = 1
    $guarda_sorte = 3

    $opcao = 0

    # Status
    $machucado = 0
    $cansado = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "Olá, %(nomeDoProtagonista)s!"
    "Você está pronto para trilhar uma jornada unica?"
    protagonista "sim"
    menu:
        "Sim, estou pronto!": 
            jump iniciar
        "Ainda não":
            jump start

label sobre:



label iniciar:

    stop music fadeout 1.0
    scene background
    with dissolve

    mestre "Bem vindo!! Eu irei ser o mestre de seu jogo hoje."
    mestre "Primeiro, me diga seu nome."
    $nomeDoProtagonista = renpy.input("Qual é o seu nome?")
    if nomeDoProtagonista == "":
        $nomeDoProtagonista = "protagonista"
    mestre "Excelente %(nomeDoProtagonista)s, espero que você tenha uma experiência incrivel hoje."
    mestre "Você pode distribuir 5 pontos em 'agressividade', 'carisma' e 'sorte'."
    mestre "Esses pontos serão determinantes para os resultados de suas escolhando, ao longo da jornada"
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
        "Você permite uma entrada amigavél":
            jump s4

label s3:
    mestre "Claramente o líder da guarda fica incomodado com sua resposta, mas sua face muda rapidamente para um sorriso sem graça e diz:"
    guarda "Vamos meu jovem, não dificulte as coisas para você."
    mestre "Você precisa escolher:"
    menu:
        "mantém sua decisão":
            jump s5
        "Muda de ideia e libera a passagem":
            jump s4

label s4:

    mestre "O líder dos guardas agradece e faz um sinal para seus guardas começarem procurar pela vila."
    jump s6

label s5:


label exit:

   # quit(confirm=None) #não ta funcionando <<


    # This ends the game.

    return
