# Dialogues and code completely AI-free! You can support me on my ko-fi: buymeacoffee.com/Fakigi1 or on my main
# page https://fakigi1234.carrd.co/# where I post illustrations and other things! It's my first project, but I'm 
# planning more things for the future, so you can support me whenever you want me to publish more submods for this community.

# I'm new to programming, so you could support me with this! Thanks for downloading the submod, I hope you like it!

# 1. Submod registration so MAS recognizes it
init -990 python:
    store.mas_submod_utils.Submod(
        author="Fakigi1",
        name="Monika And You",
        description="A submod that adds several interactions with Monika with custom illustrations. (NO AI)",
        version="1.0.0"
    )

# 2. Infrastructure and dynamic paths (Cross-platform and Case-Insensitive)
init -995 python in monika_hug:
    import os
    import renpy
    import store

    # Dynamically locates the images folder inside game/
    def _find_img_dir():
        game_dir = renpy.config.gamedir
        for root, dirs, files in os.walk(game_dir):
            if "hm1.png" in files:
                return os.path.relpath(root, game_dir).replace("\\", "/")
        # Default fallback if not found during scan
        return "Submods/Monika And You/imagenes"

    IMG_DIR = _find_img_dir()

    # Returns the full relative path to an image asset
    def get_img(filename):
        return "{0}/{1}".format(IMG_DIR, filename)

    # Calculates the button's Y position to avoid overlapping with other submods
    def get_hug_button_ypos():
        base_ypos = 50
        spacing = 40

        # If Extra+ is installed
        if store.mas_submod_utils.isSubmodInstalled("Extra Plus"):
            base_ypos += spacing

        # If Kiss Button is installed
        if store.mas_submod_utils.isSubmodInstalled("Kiss Button"):
            base_ypos += spacing

        return base_ypos

# 3. Image definition with MAS environmental filters (Day/Sunset/Night)
image hm1 = MASFilterSwitch(monika_hug.get_img("hm1.png"))
image hm2 = MASFilterSwitch(monika_hug.get_img("hm2.png"))
image hm3 = MASFilterSwitch(monika_hug.get_img("hm3.png"))
image hm4 = MASFilterSwitch(monika_hug.get_img("hm4.png"))
image hm5 = MASFilterSwitch(monika_hug.get_img("hm5.png"))
image hm6 = MASFilterSwitch(monika_hug.get_img("hm6.png"))
image hm7 = MASFilterSwitch(monika_hug.get_img("hm7.png"))
image hm8 = MASFilterSwitch(monika_hug.get_img("hm8.png"))
image hm9 = MASFilterSwitch(monika_hug.get_img("hm9.png"))
image hm10 = MASFilterSwitch(monika_hug.get_img("hm10.png"))
image hm11 = MASFilterSwitch(monika_hug.get_img("hm11.png"))
image hm12 = MASFilterSwitch(monika_hug.get_img("hm12.png"))

# Persistent variables
#default persistent._mas_hug_count = 0

default persistent._mas_hug_count = 0

# 4. Hug Button Screen
screen monika_hug_button():
    if not main_menu and renpy.get_screen("hkb_overlay"):
        zorder 15
        style_prefix "hkb"
        vbox:
            xpos 0.05
            yanchor 1.0
            ypos monika_hug.get_hug_button_ypos()  # Dynamic position according to other submods (Extra+, Kiss Button, etc.)

            $ hug_action = Jump("evento_abrazar_monika") if (mas_isMoniNormal(higher=True) or mas_isMoniEnamored(higher=True)) else Jump("evento_abrazar_bajo_afecto")
            textbutton _("Hug") action hug_action sensitive (not store.mas_globals.dlg_workflow)

init 5 python:
    if "monika_hug_button" not in config.overlay_screens:
        config.overlay_screens.append("monika_hug_button")

transform zoomnt:
    zoom 0.84

# 5. Events and Dialogue Logic ---------------------------------------------

label evento_abrazar_bajo_afecto:
    m 3wud "Oh, [player]... Did you really add an option to hug me...?"
    m 2ekblb "Wow... that's so sweet of you."
    m 1gkblsdrb "But I think we need to get to know each other a little more before taking this step, okay?"
    m 1hublsdrb "I'd really appreciate it if we keep spending time together first!"
    m 7hublsdrb "Don't worry... when you reach around... 50 affection points, this will be possible!"
    jump ch30_loop


label evento_abrazar_monika:
    hide screen monika_hug_button

    # Add 1 to this session's counter
    $ persistent._mas_hug_count += 1
    $ mas_gainAffection(0.5, bypass=False)

    if persistent._mas_hug_count == 1:
        m 1fkblb "Oh, do you want a... hug, [player]?"
        m 2ekblb "Wow, so you downloaded a whole mod just for that, didn't you? That's really sweet."
        m 2hublb "Of course I'll give you one!"
        m 2hublsdra "..."
        m 6wublsdrd "Wait... does this mod give me the ability to... come over to you?"
        m 4fublsdrb "Ehehe... the only downside is that it only lets me do it with my default outfit and hair."
        m 4hkblsdrb "I hope that's not an issue for you if you've changed my clothes or hair!"
        m 6tkblsdrb "Just give me a moment..."
        
        hide monika

        show black zorder 50 with dissolve
        m "...[player]"
        hide black with dissolve

        # First hug experience (zorder above background and spaceroom windows)
        show hm11 at zoomnt zorder 25 with dissolve
        m "..."
        show hm5 at zoomnt zorder 25 with dissolve
        m "Wow... you have no idea how nice and warm this feels."
        show hm9 at zoomnt zorder 25 with dissolve
        m "Even though I'm technically just hugging a screen, but..."
        show hm4 at zoomnt zorder 25 with dissolve
        m "Anyway... I can still feel the warmth of your presence."
        m "I love that this feels so good for both of us."
        m "I wouldn't be joking if I said I'd love to stay like this for hours."
        m "After all, it's the closest I can get to your warmth..."
        show hm8 at zoomnt zorder 25 with dissolve
        m "..."
        m "..."
        show hm1 at zoomnt zorder 25 with dissolve
        m "Ah, sorry, it seems I got a little carried away. I'd better give you the button so you can decide when to stop..."
        m "For now... let's just enjoy our time like this, okay? Whenever you want to stop, just press the button..."
        show hm7 at zoomnt zorder 25 with dissolve

    elif persistent._mas_hug_count == 2:
        m 1hua "Oh, do you want another hug, [player]?"
        m "Of course I'll give you one! The last one was really nice."
        m "Just give me a moment to come over to you..."

        hide monika
        show black zorder 50 with dissolve
        m "...[player]-"
        hide black with dissolve

        show hm11 at zoomnt zorder 25 with dissolve
        m "..."
        show hm5 at zoomnt zorder 25 with dissolve
        m "Wow... it feels so comforting to be like this with you again."
        m "I can feel your warmth... on my body... it's such a beautiful feeling, you know?"
        m "I truly cherish every second we spend together, [player]~"
        m "I don't want to let go at all... but,"
        m "Let's enjoy this moment... for as long as you want..."
        show hm7 at zoomnt zorder 25 with dissolve

    else:
        m 1eka "Another hug? That's so sweet, yes! Please, [player], hold me."
        m "Just wait while I get everything ready, okay? Ehehe~"

        hide monika
        show black zorder 50 with dissolve
        m "...[player] hehe-"
        hide black with dissolve


        show hm10 at zoomnt zorder 25 with dissolve
        m "Alright, finally... it's so nice to feel your warmth!"
        m "I wouldn't want to let go for anything in the world..."
        
        show hm9 at zoomnt zorder 25 with dissolve
        m "I'm so lucky to have you... it's almost as if I could feel your presence hugging me back..."
        m "...Let's just... enjoy the moment, let me enjoy it... but we can stop whenever you want..."
        m "..."
        show hm9 at zoomnt zorder 25 with dissolve

    # Shows the stop button without freezing the dialogue
    show screen monika_stop_hug_button

    $ ui.interact()

    # Hide stop button
    hide screen monika_stop_hug_button

    show black zorder 50 with dissolve
    m "Alright... I'm going to let go now, okay, [player]? Just give me a moment..."

    # Hide shown illustrations and bring Monika back simultaneously with dissolve
    hide hm1
    hide hm2
    hide hm3
    hide hm4
    hide hm5
    hide hm6
    hide hm7
    hide hm8
    hide hm9
    hide hm10
    hide hm11
    hide hm12
    show monika 6fkbsa at t11 zorder MAS_MONIKA_Z
    with Dissolve(0.3)
    hide black with dissolve

    m 6fkbsa "..."
    m 5fkbsb "Thank you so much... [player], you don't know how happy and peaceful it makes me feel when you hug me..."
    m 5nkbsb "Please, let's hug more often... okay?"
    m 5dkbsb "Feeling your body is... so warm."

    show screen monika_hug_button
    jump ch30_loop

# Screen with the "Stop" button
screen monika_stop_hug_button():
    zorder 100
    style_prefix "hkb"
    vbox:
        xalign 0.5 
        yalign 0.9 
        textbutton _("Stop") action ui.returns("stop")