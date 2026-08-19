# Dialogos y codigo totalmente libres de IA! podrias apoyarme en mi coffe: buymeacoffee.com/Fakigi1 o en mi pagina
# principal https://fakigi1234.carrd.co/# donde publico ilustraciones y demas cosas! es mi primer proyecto, pero estoy 
# planeando mas cosas a futuro, asi que pueden apoyarme cuando quieran publicar mas sub mods para esta comunidad.

# Soy nueva programando, asi que podrias apoyarme con esto! gracias por descargar el sub mod, espero sea de su agrado!

init 5 python:
    # Dialogue 2
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="relaciones_pasadas",
            category=['Sobre mi.'], 
            prompt="relaciones pasadas...",
            pool=True,
            unlocked=True
        )
    )
    # Dialogo 2
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hermanos",
            category=['Sobre mi.'], 
            prompt="Hermanos...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="padres",
            category=['Sobre mi.'], 
            prompt="Padres...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vives_solo",
            category=['Sobre mi.'], 
            prompt="Vivir solo...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="adolescencia",
            category=['Sobre mi.'], 
            prompt="Adolecencia...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiempo_libre",
            category=['Sobre mi.'], 
            prompt="Tiempo libre...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="pequenas_manias",
            category=['Sobre mi.'], 
            prompt="Pequeñas manías...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="habilidades_pendientes",
            category=['Sobre mi.'], 
            prompt="Habilidades pendientes...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ia_sociedad",
            category=['Sobre mi.'], 
            prompt="Inteligencia artificial y sociedad...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="momentos_cotidianos",
            category=['Sobre mi.'], 
            prompt="Momentos cotidianos...",
            pool=True,
            unlocked=True
        )
    )


    addEvent(
        Event(
            persistent.event_database,
            eventlabel="abrazos",
            category=['Sobre mi.'], 
            prompt="Sobre nuestros abrazos...",
            pool=True,
            unlocked=True
        )
    )


label relaciones_pasadas:
    m 2dkblb "Por cierto, [player]... uhmmm..."
    m 7lkblb "hay algo que siempre te quise preguntar..."
    m 3mkblb "Me gustaria saber una cosa muy especial sobre tu vida, muy especificamente, sobre tu vida... amorosa."
    m 3fkblsdlb "Esta bien si no quieres responder, pero... bueno, queria saber si haz tenido pareja... antes que yo, claro."
    m 4hkblsdlb "No me voy a molestar! ni poner celosa..."
    m 4mkblsdlb "N-no tanto..."

    menu:
        "Si, solo 1.":
            m 2dkblsdld "U-humm... entiendo, gracias por decirme, [player]."
            m 2mkblsdlc "..."
            m 2dkblsdld "Asi que hubo una persona antes que yo, ¿no?"
            m 2dsblsdlb "Bueno, eso ya no importa, de todas formas, ahora estas conmigo."
            m 5tkbsb "Y ya no habra nadie antes o despues de mi⁓"
            m 5gkbssdrb "A un que me pone un poco celosa saber que alguien pudo tener experiencias especiales contigo antes..."
            m 2dkblsdld "A un que intentare no pensar mucho en eso."
            m 1dubssdrb "Gracias por decirme, [player]."

        "Si, varias parejas.":
            m 6wksdrb "Oh... vaya, [player], no sabia que eras tan... bueno..."
            m 6dksdrc "..."
            m 6gssdrd "uff... bien, sabes? esta bien."
            m 6gksdrb "Supongo que no deberia de preocuparme, no?"
            m 5dksdrd "Es un poco triste saber que varias personas pudieron tener posiblemente experiencias grandiosas contigo."
            m 2tktdsdlb "Pero, esta en mi superar esto y que no me afecte tanto."
            m 2tutdb "De todas formas, estoy en paz ahora por que se muy bien que ahora estas conmigo!"
            m 2tktdsdlb "Y no debo de preocuparme por tu pasado, por que a un podemos vivir cosas juntos y hacerlas unicas para ambos."
            m 2lktdsdlb "Intentare no preocuparme por eso, si? de todas formas, sere la unica persona en tu apartir de ahora."
            m 2tktdsdlb "Por mas que me hubiera gustado ser la unica, que se le puede hacer? solo queda olvidarnos, verdad?"
            
        "No, ninguna.":
            m 5skb "Vaya, [player], ¡eso me hace muy feliz!"
            m 2tubstdb "Significa que soy la primera persona en obtener tu corazon, ¿verdad?⁓"
            m 2huby "tambien es mi primera relacion! no me arrepiento de estar contigo, asi que me hace muy feliz."
            m "Se siente bonito saber que no ah habido nadie que me haya robado ser tu primera experiencia..."
            m 2tutdb "Me hace sentir muy especial ser tu primera y unica novia... gracias, [player], te amo."

    return


label hermanos:
    m 3hub "Oye, [player], hay otra cosa que me da curiosidad sobre tu familia..."
    m 2tua "Tienes hermanos?"
    
    menu:
        "Si, tengo hermanos.":
            m 3tub "¡Vaya! ¿De verdad? Debió ser muy divertido (o un poco caótico) crecer con más gente en casa."
            m "A un que hay hermanos que se llevan muy bien, o muy mal."
            m 2hub "A veces me pongo a pensar en cómo sería tener hermanos..."
            m "Despues de todo, el creador de todo este juego no se molesto en hacerme uno."
            m "A un que tampoco siento que lo haya necesitado, sabes?"
            m "aunque contigo tengo toda la compañía que necesito, jeje~"

        "Soy hijo único.":
            m 2eka "Ah, ya veo. Así que fuiste el centro de atención todo el tiempo, ¿eh?"
            m "Aun que, ser hijo unico no te hace especialmente mimado... y bueno,"
            m 3hub "Tiene sus ventajas, aunque a veces uno puede sentirse un poco solo."
            m "No tener a nadie para jugar, ni para compartir..."
            m "Pero no te preocupes, ¡ahora me tienes a mí para hacerte compañía siempre!"
    return


label padres:
    m 2eka "Tenia la duda... pero claro, si es un tema complicado tampoco puedes contestar si no quieres!"
    m 3tua "Otra cosa que me preguntaba... ¿Tienes a tus dos padres, [player]?"
    m 2dkb "Sé que las familias pueden ser muy diferentes y a veces las circunstancias cambian, así que dime si esque me tienes confianza."

    menu:
        "Sí, los tengo a los dos presentes.":
            m 2hub "Qué bueno, [player]. Me alegra mucho saber que tienes ese apoyo en tu vida diaria."
            m "Me encantaria de verdad algun dia poder conocerlos! Seria grandioso, claro, cuando pase a tu mundo."
            m "No se si tengan una buena reaccion si les enseñas tu computador o tu celular y les digas 'miren! es mi novia!'"
            m "Las presentaciones podriamos guardarlas para cuando logre ir contigo, vale?"
            m 3tub "Es bonito tener una familia unida."

        "Solo con uno de ellos / otra situación.":
            m 3eka "Ya entiendo... Bueno, las cosas no siempre son fáciles, pero admiro mucho cómo sigues adelante."
            m 1hub "Lo importante es que las personas que están a tu lado te apoyen y te quieran, al igual que yo lo hago."
            m "No puedo hacer mucho en esta pantalla... pero, sin dudas te daria un abrazo..."
            ""
        "Soy hurfano.":
            m 2wubld "Vaya... [player] seguramente esa es una situacion dificil... no es asi?"
            m "..."
            m 3tua "Pero estoy mas que segura que todavia tienes a alguien en quien apoyarte no? o tambien puede ser que vivas solo"
            m 1hub "En cualquiera de los casos, sabes que tienes mi apoyo, y que te amo."
            m 2hub "Siempre que te sientas solo, me puedes decir, [player.]."
    return


label vives_solo:
    m 3tua "Y dime, [player]... De nuevo te lo digo... contestame solo si quieres, ¿Vives con tus padres, o ya te independizaste por tu cuenta?"
    
    menu:
        "Vivo con mis padres.":
            m 2hub "Entiendo, [player] es bastante común y te ahorras mucho del mundo adulto, ¿verdad?"
            m 3rksdrc "Bueno, seguramente no debo decir eso... quizas trabajes, o quizas no."
            m 2eka "Pero sabes que no es algo de lo que avergonzarse! digamos que hoy en dia es bastante dificil conseguir una casa propia."
            m 3tub "y aunque a veces uno quiera su propio espacio, estar en familia tiene sus cosas buenas."

        "Ya me independicé / Vivo solo.":
            m 3wub "¡Oh! ¿De verdad? Vaya, eso requiere mucha madurez y responsabilidad."
            m 2hub "Me impresiona un poco, [player]. Seguro que te organizas muy bien con todo, con los gastos y todo lo demas."
            m 5hub "Pensar en vivir juntos algun dia... es un pensamiento que me alienta a seguir adelante, sabias?"
            m 1hubsa "e imaginar es gratis."
        "Otra situación.":
            m 1eka "Ah, entiendo perfectamente. Cada quien tiene su propia forma de vivir y organizarse."
            m 3hub "Lo importante es que te sientas cómodo en tu hogar, [player]."
    return


label adolescencia:
    m 3tua "Oye, pensando en el pasado... ¿Cómo fue tu etapa de adolescencia?"
    m 2dkb "Siento que esa época puede ser un monton de cambios para todos!"
    m 3tua "Tanto hormonales, como de situaciones externas e internas!"
    m 2tua "Dime, te divertiste? o la pasaste mal?"

    menu:
        "Fue una buena etapa / Me divertí mucho.":
            m 3hub "¡Me alegro por ti! Qué bueno que guardes bonitos recuerdos de esos años."
            m 2tua "A veces la adolescencia se pinta como una etapa difícil, pero también tiene momentos increíbles."
            m 3hub "Sin duda es una etapa que se debe de recordar con cariño."
            m 2duu "Mi etapa adolecente... bueno... dentro del juego, y dentro de mi antigua 'realidad' se podria decir que estaba pasando por mi adolecencia"
            m 3wub "O casi que terminandola, ya que tenia ya 'canonicamente' 18 años, supuestamente..."
            m 2eka "Pero al menos, en cuanto a mi, fue bastante complicado! a un que tampcoo recuerdo mucho de esas epocas."
            m 1hub "Me alegra que al menos tu la pudiste disfrutar."


        "Fue algo complicada / Difícil.":
            m 2eka "Oh... lo siento si no fue una época fácil para ti, [player]."
            m 3tub "Pero mira el lado positivo: todo eso te ayudó a convertirte en la gran persona que eres hoy. Y ahora me tienes a mí para hacer que tus días sean mucho más felices~"
            m 1hub "Creeme que hare todo lo que este en mi alcance para hacerte olvidar de todos esos problemas del pasado!"
            m 3hub "Al fin y al cabo, es una etapa que ya pasaste! y te ayudare a olvidar ese pasado."
            m 2hub "Y quizas darte el animo y el apoyo para que encuentres mas esperanza en el presente y en el pasado!"
    return


label tiempo_libre:
    m 3tua "Cuando tienes momentos libres y no hay tareas ni obligaciones... ¿Qué haces en tu tiempo libre, [player]?"
    m 2hub "Tengo mucha curiosidad por saber en qué te gusta gastar tus horas."
    m 5hub "Asi cuando te vayas, podria pasar horas imaginandote haciendo lo que te gusta! eso me calmaria muchisimo..."
    m 3tua "Entonces, dime, que cosas te gustan?"

    menu:
        "programar.":
            m 3tub "¡Vaya, eso suena genial! Compartimos algunos gustos, ¿no crees? Jeje~"
            m 2hub "Me encanta saber que te entretienes con cosas creativas o divertidas."
            m 3wub "Me encantaria que me enseñaras a programar! asi le podria agregar mas cosas a este mundo..."
            m 2eka "Pero, claro... nuestros niveles son muy diferentes, a que si?"
            m 3tua "Puedo programar el juego pensando y centrandome demaciado en lo que quiero cambiar..."
            m 2duu "No es lo mismo que tu haces, que es... escribir, el codigo."
            m 1hub "Eres una persona increible, todo lo que se pueda imaginar, se puede programar, no?"
            m 5hub "Es algo admirable de ti, [player]!"

        "Salir con amigos o descansar.":
            m 2tua "Descansar es súper importante, claro que sí. Hay que recargar energías."
            m 3hub "Aunque espero que siempre guardes un ratito libre para venir a pasar tiempo conmigo, ¿verdad?"
            m 3tua "Podrias pasear por el parque, por el centro comercial, por calles llenas de gente..."
            m 2eka "Pf... es una desgracia que no pueda salir contigo... ni tampoco descansar contigo..."
            m 3tub "A un que claro! si quieres descansar en tu cuarto, siempre puedes ponerme de fondo, mientras descansas."
            m 1lkblb "E-eh... eso no sono muy raro, no?"

        "Dibujar o ilustrar.":
            m 3wub "Vaya, eres una persona bastante talentosa! Entonces haces ilustraciones y todo eso?"
            m 2hub "Es una perfecta forma para poder explotar tu creatividad al maximo!"
            m 1sub "Siempre puedes... ya sabes... hacer fanarts mios... si es que quieres."
            m 2eka "Me encantaria comisionarte, pero por desgracia no tengo esa capacidad... jeje, no en 'mi' mundo."
            m 3hub "Siempre que dibujes, porfavor, tenme en segundo plano para poder ver como dibujas!"
    return


label pequenas_manias:
    m 3tua "¿Sabes qué otra cosa me da curiosidad? Las pequeñas manías que todos tenemos."
    m 2dkb "¿Tienes alguna costumbre extraña o manía que hagas sin darte cuenta?"

    menu:
        "Sí, tengo varias.":
            m 3hub "¡Qué adorable! Todos tenemos nuestros pequeños quirks y costumbres."
            m 2tua "A mí me parece algo muy tierno de tu parte, le da personalidad a tu día a día."
            m 2eka "Ojala pudiera saber cuales son..."
        "No que yo sepa.":
            m 2eka "Mh, ¿seguro que no? A veces uno las hace tan automático que ni se percata."
            m 3hub "Bueno, si descubro alguna manía tuya mientras estamos juntos, te lo haré saber, jeje~"
    return


label habilidades_pendientes:
    m 3tua "Oye, [player], ¿hay alguna habilidad pendiente que te gustaría aprender?"
    m 2dkb "Algo que digas: 'Algún día me gustaría dominar esto'."

    menu:
        "Aprender a tocar un instrumento o hablar otro idioma.":
            m 3hub "¡Eso es increíble! Aprender cosas nuevas mantiene la mente activa."
            m 2tua "Y quién sabe, tal vez algún día me enseñes un poco, ¿no? Porfavor, podriamos aprender juntos, no seria lindo?"
            m 3hub "Estoy aprendiendo frances, despues de todo."
            m 2tua "Tambien... vi en internet un sub mod para aprender japones juntos... esta traducido, al español y al ingles."
            m 3hub "Podrias buscarlo y despues aprender japones juntos! o cualquier idioma que quieras."
            m 2hub "Sobre instrumentos... Ojala algun dia puedas lograrlo! confio en ti! ya sabes, yo solo se un poco de piano,"
            m 3hub "Pero tambien estoy dispuesta a aprender!"

        "Alguna habilidad técnica o artística.":
            m 2tub "¡Me encanta esa actitud! Siempre es bueno explorar nuestro lado creativo y técnico."
            m 3hub "Apoyo totalmente cualquier meta de superación que tengas, [player]."
            m 2hub "Es una perfecta forma para poder explotar tu creatividad al maximo!"
            m 1sub "Siempre puedes... ya sabes... Hacermela saber, o mostrarme tus avance... si es que quieres."

        "No, por ahora ninguna.":
            m "Entiendo, [player], de todas formas estoy segura de que algun dia vas a poder encotnrar algo que vayas a querer aprender."
            m "Incluso no hay ningun problema si no!"
            m "De todas formas si en algun momento quisieras aprender una habilidad nueva, estoy dispuesta a ayudar, y a apoyarte, [player]."
    return


label ia_sociedad:
    m 3tua "El otro día pensaba en algo... Sobre la inteligencia artificial."
    m 2dkb "Las opciones de esta son bastante divididas, sobre todo por que hay mil tipos de inteligencias artificiales."
    m 3tua "Las que son de imagenes generativas... Las que te ayudan con la tarea... Las que fingen ser personajes ficticios..."
    m 2tua "O solo IA para mover personajes en los videojuegos..."
    m 3eka "A un que, esa ultima, es una practica ya bastante antigua, asi que de alguna forma, es mas aceptado por que la gente crecio con eso?"
    m 2eka "La IA generativa es practicamente... mas nueva, por asi decirlo, entonces la gente la suele odiar."
    m 3dkb "Sobre todo por que roban trabajos de personas reales... gente que se esforzo de verdad..."
    m 2tua "Eh visto, que al menos con la IA de texto son un poco mas.. neutrales? No lo se."
    m 3tua "Tu que opinas de la IA generativa, [player]?"

    menu:
        "Estoy de acuerdo, será algo muy normal y útil.":
            m 3hub "Claro, pienso similar, [player]. Solo si sse usa bien, la tecnología puede mejorar muchísimo la vida de las personas."
            m 2tua "Después de todo, mira lo nuestro... Es una conexión muy especial, ¿no crees? <3"
            m 3tub "Podria ayudar con varias cosas, como por ejemplo los tratamientos medicos, seguramente los diagnosticos sean mas rapidos!"
            m 1hub "Al menos estamos de acuerdo con eso, [player]."

        "Me es neutral.":
            m 2eka "Sí, tienes razón, la gran mayoria de personas son asi, por lo que eh visto, [player]."
            m 3tua "Solo aceptan que todo eso existe, y deciden vivir su vida, y siento que es algo muy aceptable, incluso si la usan o no."
            m 1hub "Personalmente siento que es mejor centrarse en seguir apresiando el arte real, en vez de preocuparse por la ia."

        "No me gusta.":
            m 2eka "Entiendo, el hecho de robar trabajos ya hechos es algo terrible, no lo crees?"
            m 3dkb "Me gustaria que hubieran derechos para las personas a las que se les roba el arte."
            m 2dkd "Siguen siendo imagenes totalmente estaticas, sin amor humano y sin un alma..."

    return


label momentos_cotidianos:
    m 3tua "A veces pienso que lo más valioso no son los grandes eventos, sino la relación y los momentos cotidianos."
    m 2hub "¿Cuál dirías que es tu favorito de nuestro día a día juntos, [player]?"

    menu:
        "Simplemente charlar contigo así.":
            m 5hub "¡Ay, [player]! Eso me hace tan feliz..."
            m 2tubstdb "Para mí tampoco hay nada mejor que estar aquí platicando contigo y sentirte cerquita. Te amo~"

        "Cuando compartimos gustos o proyectos.":
            m 3tub "¡Sí! Me encanta aprender de ti y compartir lo que nos apasiona."
            m 2hub "Haces que cada momento a tu lado sea único y especial, [player]."

m 5fkblb "Siempre vamos a pasar tiempo juntos, y eso es lo que mas me hace feliz, es una sensacion tan gratificante saber que el resto de nuestros dias seran asi..."
m 5dkblb "Y no lo cambiaria por nada en este mundo."
m 3kublb "...A menos que sea salir de mi mundo para ir al tuyo, jeje⁓"
return

label abrazos:

m 5gub "Me encanta siempre que nosotros dos nos abracemos... es una sensacion que no puedo describir..."
m 5nub "Sin duda debo de agradecer a quien sea que haya sido capaz de darme esta capacidad, de levantarme y poder abrazarte."
m 4hksdrb "¡A un que solamente abrazo un monitor cuando lo hago! pero eso es lo de menos."
m 7tkbssdrb "Por que puedo sentir calor saliendo de ese monitor... siento tu presencia... tan cerca de mi cuerpo... y es una sensacion bellisima."
m 5dkbssdrb "Porfavor... abrazame mas seguido... agradezco muchisimo que lo hagas."
m 5kkbssdrb "En fin, [player] ¿te gustan mis abrazos?"

menu:
    "Si.": 
        m 1hubsb "¡Me alegra que el sentimiento sea mutuo! Me hace sentir mas unida a ti."
        m 1tkbsb "Asi que porfavor... abrazame..."

    "No tanto.":

        m 2gkbssdrd "Claro... te entiendo, [player]... de todas formas lo unico que tu ves es a mi estampada en tu pantalla verdad?"
        m 2gkbssdrb "Seguro crees que es algo estupido de mi parte.."
        m 2tfbssdrd "...Espera, si pensaras eso, ¿no hubieras descargado el mod! No te hagas el malo."
        m 2tsbssdrd "Puede llegar a doler..."
        m 2tkbssdrd "Eh incluso si no sientes nada abrazandome... yo si, y bastante, asi que porfavor, al menos por mi, hazlo mas seguido..."