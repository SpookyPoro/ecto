# Aqui é o script principal do jogo :)

# Personagens

define anon = Character("?????")    # Pessoa desconhecida
define main = Character("Hector")   # O protagonista da história
define luci = Character("Lucid")    # Amiga de infância
define mary = Character("Mary")     # Pregadora de peças/tsundere
# define = Character("Wraith") #
# define = Character() #

# Flags

# Imagens
image maid = "ph maid"

# Aqui começa o jogo

label start:

    # Primeira cena, despertar do protagonista

    play sound cicada

    "..."

    scene bg sun
    with fade

    anon "Hector?"

    anon "Hector??"

    anon "Hector???"

    anon "Hector can you hear me?"

    anon "Hector...?"

    "Where am I?"

    "I can hear someone calling my name, but I have no idea of who can it be or even why I'm here."

    "The sun feels nice on my skin though, just a little too bright."

    stop sound fadeout 2.0

    anon "Hector, can you hear me?"

    "I recognize this voice. It's from an old friend of mine, Lucid."

    show maid
    with fade

    luci "Hector! Thank God you woke up!"

    "I try to get up but my arms couldn't exactly complete their task."

    main "Lucid! Is that you? What was I doing on the floor? I can't remember exactly..."

    "Lucid face was a mix of relief and guilty."

    luci "Well... It was... an accident..."

    "She said that while trying to hide a broom behind her back, with little success since the broom is really big for her small figure."


    # Fim do jogo
    return
