# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mestre = Character("Mestre")
define pai = Character("Pai")
define Jogador = Character("Jogador")

image menuBackground = "images/menuBackground.jpg"
image background = "images/background.jpg"
image jogador = "images/jogador"
image mestre = "images/mestre.jpg"
image pai = "images/pai.jpg"
# The game starts here.

label start:

    $ teste = True

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene menuBackground:
        zoom 1.25

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "Olá, jogador!"
    "Você está pronto para trilhar uma jornada unica?"
    menu:
        "Sim, estou pronto!": 
            jump iniciar
        "Ainda não":
            jump start

label iniciar:

    scene background
    with dissolve

    show mestre
    with dissolve

    mestre "Bem vindo!!"

    # This ends the game.

    return
