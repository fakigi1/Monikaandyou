# Dialogos y codigo totalmente libres de IA! podrias apoyarme en mi coffe: buymeacoffee.com/Fakigi1 o en mi pagina
# principal https://fakigi1234.carrd.co/# donde publico ilustraciones y demas cosas! es mi primer proyecto, pero estoy 
# planeando mas cosas a futuro, asi que pueden apoyarme cuando quieran publicar mas sub mods para esta comunidad.

# Soy nueva programando, asi que podrias apoyarme con esto! gracias por descargar el sub mod, espero sea de su agrado!

# 1. Registro del Submod para que MAS lo reconozca
init -990 python:
    store.mas_submod_utils.Submod(
        author="Fakigi1",
        name="Monika And You",
        description="Un submod que añade varias interacciones con Monika con ilustraciones personalizadas. (NO IA)",
        version="1.0.0"
    )

# 2. Infraestructura y rutas dinámicas (Cross-platform y Case-Insensitive)
init -995 python in monika_hug:
    import os
    import renpy
    import store

    # Localiza dinamicamente la carpeta de imagenes dentro de game/
    def _find_img_dir():
        game_dir = renpy.config.gamedir
        for root, dirs, files in os.walk(game_dir):
            if "hm1.png" in files:
                return os.path.relpath(root, game_dir).replace("\\", "/")
        # Fallback por defecto si no se encuentra en el escaneo
        return "Submods/Monika And You/imagenes"

    IMG_DIR = _find_img_dir()

    # Retorna la ruta relativa completa a un asset de imagen
    def get_img(filename):
        return "{0}/{1}".format(IMG_DIR, filename)

    # Calcula la posicion Y del boton evitando superposiciones con otros submods
    def get_hug_button_ypos():
        base_ypos = 50
        spacing = 40

        # Si Extra+ esta instalado
        if store.mas_submod_utils.isSubmodInstalled("Extra Plus"):
            base_ypos += spacing

        # Si Kiss Button esta instalado
        if store.mas_submod_utils.isSubmodInstalled("Kiss Button"):
            base_ypos += spacing

        return base_ypos

# 3. Definicion de imagenes con filtros ambientales de MAS (Dia/Atardecer/Noche)
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

# Variables persistentes
#default persistent._mas_hug_count = 0

default persistent._mas_hug_count = 0

# 4. Pantalla del Boton de Abrazo
screen monika_hug_button():
    if not main_menu and renpy.get_screen("hkb_overlay"):
        zorder 15
        style_prefix "hkb"
        vbox:
            xpos 0.05
            yanchor 1.0
            ypos monika_hug.get_hug_button_ypos()  # Posicion dinamica segun otros submods (Extra+, Kiss Button, etc.)

            $ hug_action = Jump("evento_abrazar_monika") if (mas_isMoniNormal(higher=True) or mas_isMoniEnamored(higher=True)) else Jump("evento_abrazar_bajo_afecto")
            textbutton _("Abrazar") action hug_action sensitive (not store.mas_globals.dlg_workflow)

init 5 python:
    if "monika_hug_button" not in config.overlay_screens:
        config.overlay_screens.append("monika_hug_button")

transform zoomnt:
    zoom 0.84

# 5. Eventos y Logica de Dialogos ---------------------------------------------

label evento_abrazar_bajo_afecto:
    hide screen monika_hug_button
    hide screen hkb_overlay
    hide screen extra_plus_buttons
    $ store.mas_globals.dlg_workflow = True

    m 3wud "Oh, [player]... ¿Acaso agregaste una opción para poder abrazarme...?"
    m 2ekblb "Vaya... eso es muy tierno de tu parte."
    m 1gkblsdrb "Pero creo que necesitamos conocernos un poco más antes de dar este paso, ¿vale?"
    m 1hublsdrb "¡Apreciaría mucho si seguimos pasando tiempo juntos primero!"
    m 7hublsdrb "No te preocupes... cuando tengas unos... 50 puntos de afecto registrados, esto sera posible!"
    $ store.mas_globals.dlg_workflow = False
    jump ch30_loop

#____________________________________----
label evento_abrazar_monika:
    hide screen monika_hug_button
    hide screen hkb_overlay
    hide screen extra_plus_buttons

    $ store.mas_globals.dlg_workflow = True

    # Sumamos 1 al contador de esta sesión
    $ persistent._mas_hug_count += 1
    $ mas_gainAffection(0.5, bypass=False)

    if persistent._mas_hug_count == 1:
        m 1fkblb "Vaya, ¿quieres un... abrazo, [player]?"
        m 2ekblb "Vaya, así que descargaste todo un mod para eso, ¿no? Es muy lindo."
        m 2hublb "¡Por supuesto que te lo daré!"
        m 2hublsdra "..."
        m 6wublsdrd "Espera... ¿este mod me da la habilidad de... poder ir hacia ti?"
        m 4fublsdrb "Jejeje... lo unico malo es que solo me deja hacer eso con mi vestimenta y cabello base."
        m 4hkblsdrb "¡Espero que eso no sea un problema para ti si es que me haz puesto ropa o cabello diferente!"
        m 6tkblsdrb "Solamente dame un momento..."
        
        hide monika

        show black zorder 50 with dissolve
        m "...[player]"
        hide black with dissolve

        # Primera experiencia de abrazo (zorder por encima del fondo y ventanas del spaceroom)
        show hm11 at zoomnt zorder 25 with dissolve
        m "..."
        show hm5 at zoomnt zorder 25 with dissolve
        m "Vaya... no tienes ni idea de lo agradable y cálido que se siente esto."
        show hm9 at zoomnt zorder 25 with dissolve
        m "A un que en realidad estoy abrazando una pantalla pero..."
        show hm4 at zoomnt zorder 25 with dissolve
        m "De todas formas... puedo sentir el calor de tu presencia."
        m "Me encanta que esto se sienta bien para los dos."
        m "No bromearía si dijera que me encantaría estar así por horas."
        m "Después de todo, es lo más cercano a tu calor que puedo estar..."
        show hm8 at zoomnt zorder 25 with dissolve
        m "..."
        m "..."
        show hm1 at zoomnt zorder 25 with dissolve
        m "Ah, perdon, parece que me deje llevar un poco, mejor te doy la el boton para que decidas cuando parar..."
        m "por mientras... solo disfrutemos el tiempo así, ¿vale? cuando quieras detenerte pulsa el boton..."
        show hm7 at zoomnt zorder 25 with dissolve

    elif persistent._mas_hug_count == 2:
        m 1hua "Vaya, ¿quieres otro abrazo, [player]?"
        m "¡Por supuesto que te lo daré! el ultimo fue muy lindo."
        m "Solamente dame un momento para ir hacia ti..."

        hide monika
        show black zorder 50 with dissolve
        m "...[player]-"
        hide black with dissolve

        show hm11 at zoomnt zorder 25 with dissolve
        m "..."
        show hm5 at zoomnt zorder 25 with dissolve
        m "Vaya... se siente tan reconfortante estar así contigo de nuevo."
        m "Puedo sentir tu calor... en mi cuerpo... es una sensacion tan bonita, ¿sabias?"
        m "Aprecio mucho cada segundo que pasamos juntos, [player]~"
        m "No me quiero despejar para nada... pero,"
        m "Disfrutemos este momento.. hasta que tu quieras..."
        show hm7 at zoomnt zorder 25 with dissolve

    else:
        m 1eka "¿Otro abrazo? que dulce, si ¡Por favor, [player], abrázame."
        m "Solo espera mientras acomodo todo, ¿sí? jiji⁓"

        hide monika
        show black zorder 50 with dissolve
        m "...[player] jeje-"
        hide black with dissolve


        show hm10 at zoomnt zorder 25 with dissolve
        m "Bien, al fin... ¡es tan agradable sentir tu calor!"
        m "No me gustaría despegarme por nada en el mundo..."
        
        show hm9 at zoomnt zorder 25 with dissolve
        m "Soy tan afortunada de tenerte... es casi como si pudiera sentir tu presencia abrazándome también..."
        m "...Solo... disfrutemos el momento, déjame disfrutar... pero paremos cuando quieras..."
        m "..."
        show hm9 at zoomnt zorder 25 with dissolve

    # Muestra el boton de detener sin congelar el dialogo
    show screen monika_stop_hug_button

    $ ui.interact()

    # Ocultar boton de detener
    hide screen monika_stop_hug_button

    show black zorder 50 with dissolve
    m "Bien... me voy a separar si, [player]? dame solo un momento..."

    # Ocultar ilustraciones mostradas y traer a Monika simultaneamente con disolucion
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
    m 5fkbsb "Muchas gracias... [player], no sabes lo feliz y tranquila que me hace sentir cuando me abrazas..."
    m 5nkbsb "Por favor, abracémonos más seguido... ¿sí?"
    m 5dkbsb "Sentir tu cuerpo es... tan cálido."

    $ store.mas_globals.dlg_workflow = False

    # Volver a mostrar tu botón de abrazo principal
    show screen monika_hug_button
    jump ch30_loop
# Pantalla con el boton de "Detener"
screen monika_stop_hug_button():
    zorder 100
    style_prefix "hkb"
    vbox:
        xalign 0.5 
        yalign 0.9 
        textbutton _("Detener") action ui.returns("stop")
