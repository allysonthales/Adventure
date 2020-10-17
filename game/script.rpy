# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

screen menu1:
    imagemap:
        ground "images/normal.jpg"
        hover "images/emcima.jpg"

        hotspot(1112, 2, 135, 143) clicked Jump("iniciar")
        hotspot(1111, 153, 135, 143) clicked Jump("menu")
        hotspot(1111, 303, 135, 143) clicked Jump("exit")


define mestre = Character("Mestre", color = '#00ff37')
define pai = Character("Pai")
define protagonista = Character("[nomeDoProtagonista]", color = '#2200ff')

image menuBackground = "images/menuBackground.jpg"
image background = "images/background.jpg"
image jogadorImagem = "images/jogador"
image mestre = "images/mestre.jpg"
image pai = "images/pai.jpg"



# The game starts here.

label start:

    play music "/audio/backgroundMusic.mp3"
    call screen menu1

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

    show mestre at right
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

    #if (agressividade + carisma + sorte) <= 0 && pontos == 0:

    mestre "Certo, agora você tem:"
    mestre "%(agressividade)s pontos em Agressividade, %(carisma)s pontos em Carisma e %(sorte)s pontos em Sorte"



        

    mestre "Você irá se aventurar nas terras de BLABLA e tomará decisões como um jovem morador de uma vila."
    mestre "Esta vila fica localizada ao extremo norte de um reino imperial, e você é o filho do chefe desta vila"
    mestre "Na vila, todo dia é quase sempre igual, e você, como filho do chefe da vila, tem muitas responsabilidades, mas essa tranquilidade está preste a acabar…"


    # This ends the game.

    return
