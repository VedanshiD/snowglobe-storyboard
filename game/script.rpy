# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
label start:
"--OUT OF SERVICE--\n A interactive horror game"
"YOU WAKE UP IN AN ELEVATOR AND YOUR MEMORY IS COMPLETELY FOGGY.    YOUR VISION SEEMS TO BE SHIFTING, AND YOUR HEAD IS THROBBING WITH PAIN."
# The game starts here.
transform bg_zoom:
    truecenter
    zoom 0.65
label scene1:
    define blink = Fade(0.05, 0.4, 0.1, color="#000")
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg rsoom.jpg") to the
    # images directory to show it.
    scene bg inelevator with fade
    scene bg inelevator with blink
    scene bg inelevator with blink
    "YOU BLINK AS YOUR VISION SLOWLY COMES INTO FOCUS WHILE THE OVERHEAD LIGHTS ABOVE YOU FLICKER"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    y "where am i...? oh god, is that blood?"
    # These display lines of dialogue.
    "⊥⋏⫑⋂⊏⋌ ⊥⨀ ⫑⨀⩪ =⋌⨀⩞⊏⊏⊥"
    #show elevator
    #blinking
    y "huh? i have no idea what that language is... i feel like i should know it, but i don't. my head hurts so much."
    "..." with hpunch
    y "what the...? what was that?"

    # This ends the game.
    return
