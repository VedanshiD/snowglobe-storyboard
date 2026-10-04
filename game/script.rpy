define y = Character("You")

transform bg_zoom:
        truecenter
        zoom 0.65
define blink = Fade(0.05, 0.4, 0.1, color="#000")
label start:
"--OUT OF SERVICE--\n A interactive horror game"
"YOU WAKE UP IN AN ELEVATOR AND YOUR MEMORY IS COMPLETELY FOGGY.    YOUR VISION SEEMS TO BE SHIFTING, AND YOUR HEAD IS THROBBING WITH PAIN."
label scene1:
    scene bg inelevator at bg_zoom with fade
    scene bg inelevator at bg_zoom with blink
    scene bg inelevator at bg_zoom with blink
    "YOU BLINK AS YOUR VISION SLOWLY COMES INTO FOCUS WHILE THE OVERHEAD LIGHTS ABOVE YOU FLICKER"
    y "where am i...? oh god, is that blood?"
    "⊥⋏⫑⋂⊏⋌ ⊥⨀ ⫑⨀⩪ =⋌⨀⩞⊏⊏⊥"
    y "huh? i have no idea what that language is... i feel like i should know it, but i don't. my head hurts so much."
    "..." with hpunch
    y "what the...? what was that?"
    menu:
        "FLOOR 1":
            jump floor1
        "FLOOR 2":
            jump floor2
        "FLOOR 3":
            jump floor3
        "FLOOR 4":
            jump floor4
        "FLOOR 5":
            jump floor5
label floor1:
    scene bg floor1 at bg_zoom with fade
    return
label floor2:
    y "FLOOR 2"
    return
label floor3:
    y "FLOOR 3"
    return
label floor4:
    y "FLOOR 4"
    return
label floor5:
    y "FLOOR 5"
    return

    # This ends the game.
    return
