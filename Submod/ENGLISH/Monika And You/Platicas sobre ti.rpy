# Dialogues and code completely AI-free! You can support me on my ko-fi: buymeacoffee.com/Fakigi1 or on my main
# page https://fakigi1234.carrd.co/# where I post illustrations and other things! It's my first project, but I'm 
# planning more things for the future, so you can support me whenever you want me to publish more submods for this community.

# I'm new to programming, so you could support me with this! Thanks for downloading the submod, I hope you like it!

init 5 python:
    # Dialogue 2
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="relaciones_pasadas",
            category=['About me.'], 
            prompt="Past relationships...",
            pool=True,
            unlocked=True
        )
    )
    # Dialogue 2
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hermanos",
            category=['About me.'], 
            prompt="Siblings...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="padres",
            category=['About me.'], 
            prompt="Parents...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vives_solo",
            category=['About me.'], 
            prompt="Living alone...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="adolescencia",
            category=['About me.'], 
            prompt="Adolescence...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiempo_libre",
            category=['About me.'], 
            prompt="Free time...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="pequenas_manias",
            category=['About me.'], 
            prompt="Little quirks...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="habilidades_pendientes",
            category=['About me.'], 
            prompt="Skills to learn...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ia_sociedad",
            category=['About me.'], 
            prompt="AI and society...",
            pool=True,
            unlocked=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="momentos_cotidianos",
            category=['About me.'], 
            prompt="Everyday moments...",
            pool=True,
            unlocked=True
        )
    )


    addEvent(
        Event(
            persistent.event_database,
            eventlabel="abrazos",
            category=['About me.'], 
            prompt="About our hugs...",
            pool=True,
            unlocked=True
        )
    )


label relaciones_pasadas:
    m 2dkblb "By the way, [player]... umm..."
    m 7lkblb "There's something I've always wanted to ask you..."
    m 3mkblb "I'd like to know something very special about your life. Specifically, about your... love life."
    m 3fkblsdlb "It's completely fine if you don't want to answer, but... well, I wanted to know if you've had a partner... before me, of course."
    m 4hkblsdlb "I won't get mad! Or jealous..."
    m 4mkblsdlb "N-Not too much, anyway..."

    menu:
        "Yes, just one.":
            m 2dkblsdld "U-huh... I understand, thanks for telling me, [player]."
            m 2mkblsdlc "..."
            m 2dkblsdld "So there was someone before me, huh?"
            m 2dsblsdlb "Well, that doesn't matter anymore. You're with me now, anyway."
            m 5tkbsb "And there won't be anyone else before or after me~"
            m 5gkbssdrb "Even though it makes me a little jealous knowing someone else got to share special experiences with you before..."
            m 2dkblsdld "But I'll try not to think too much about it."
            m 1dubssdrb "Thanks for telling me, [player]."

        "Yes, several.":
            m 6wksdrb "Oh... wow, [player], I didn't know you were so... well..."
            m 6dksdrc "..."
            m 6gssdrd "Phew... alright, you know what? It's fine."
            m 6gksdrb "I guess I shouldn't worry about it, right?"
            m 5dksdrd "It's a little sad knowing that several people probably had wonderful experiences with you."
            m 2tktdsdlb "But it's up to me to get over it and not let it affect me so much."
            m 2tutdb "Anyway, I'm at peace now because I know very well that you're with me now!"
            m 2tktdsdlb "And I shouldn't worry about your past, because we can still experience things together and make them unique for both of us."
            m 2lktdsdlb "I'll try not to worry about it, okay? Besides, I'll be the only person in your life from now on."
            m 2tktdsdlb "As much as I would've liked to be the only one, what can we do? We just have to leave it in the past, right?"
            
        "No, none.":
            m 5skb "Wow, [player], that makes me so happy!"
            m 2tubstdb "That means I'm the first person to win your heart, right?~"
            m 2huby "It's my first relationship too! I don't regret being with you at all, so it makes me really happy."
            m "It feels nice knowing that no one else stole the chance to be your first experience..."
            m 2tutdb "It makes me feel so special to be your first and only girlfriend... thank you, [player], I love you."

    return


label hermanos:
    m 3hub "Hey, [player], there's something else I'm curious about regarding your family..."
    m 2tua "Do you have any siblings?"
    
    menu:
        "Yes, I have siblings.":
            m 3tub "Wow! Really? It must have been a lot of fun (or a little chaotic) growing up with more people in the house."
            m "Although some siblings get along really well, and others not so much."
            m 2hub "Sometimes I wonder what it would be like to have siblings..."
            m "After all, the creator of this game didn't bother giving me any."
            m "Though I don't really feel like I needed them, you know?"
            m "Besides, I have all the company I need with you, ehehe~"

        "I'm an only child.":
            m 2eka "Ah, I see. So you were the center of attention all the time, huh?"
            m "Though being an only child doesn't necessarily make you spoiled... and well,"
            m 3hub "It has its perks, even if it can feel a bit lonely sometimes."
            m "Not having anyone to play with, or to share things with..."
            m "But don't worry, now you have me to keep you company forever!"
    return


label padres:
    m 2eka "I was wondering... but of course, if it's a difficult topic, you don't have to answer if you don't want to!"
    m 3tua "Another thing I was wondering... Are both of your parents around, [player]?"
    m 2dkb "I know families can be very different and circumstances change sometimes, so just tell me if you feel comfortable sharing."

    menu:
        "Yes, both of them are present.":
            m 2hub "That's wonderful, [player]. I'm so glad to hear you have that kind of support in your daily life."
            m "I'd truly love to meet them someday! It would be amazing, of course, once I cross over to your world."
            m "I'm not sure they'd react very well if you showed them your computer or phone and said, 'Look! This is my girlfriend!'"
            m "So maybe we should save the introductions for when I finally make it there with you, okay?"
            m 3tub "It's nice to have a close-knit family."

        "Only one of them / Another situation.":
            m 3eka "I understand... Well, things aren't always easy, but I really admire how you keep moving forward."
            m 1hub "The important thing is that the people by your side support and love you, just like I do."
            m "I can't do much from behind this screen... but I'd definitely give you a big hug..."
            ""
        "I'm an orphan.":
            m 2wubld "Wow... [player], that must be a really difficult situation... isn't it?"
            m "..."
            m 3tua "But I'm more than sure you still have someone to lean on, right? Or maybe you just live on your own."
            m 1hub "Whatever the case, you know you have my support, and that I love you."
            m 2hub "Whenever you feel lonely, you can always tell me, [player]."
    return


label vives_solo:
    m 3tua "And tell me, [player]... I'll say it again... only answer if you want to. Do you live with your parents, or have you moved out on your own?"
    
    menu:
        "I live with my parents.":
            m 2hub "I understand, [player]. It's pretty common and saves you from a lot of adult responsibilities, right?"
            m 3rksdrc "Well, I probably shouldn't assume that... maybe you work, or maybe you don't."
            m 2eka "But you know it's nothing to be ashamed of! Let's just say getting your own place nowadays is pretty difficult."
            m 3tub "And even though sometimes you want your own space, being with your family has its good sides too."

        "I moved out / I live alone.":
            m 3wub "Oh! Really? Wow, that takes a lot of maturity and responsibility."
            m 2hub "I'm a little impressed, [player]. I'm sure you manage everything really well, like your expenses and all that."
            m 5hub "Thinking about living together someday... it's a thought that encourages me to keep going, you know?"
            m 1hubsa "And imagining is free."
        "Another situation.":
            m 1eka "Ah, I understand completely. Everyone has their own way of living and organizing themselves."
            m 3hub "The important thing is that you feel comfortable in your home, [player]."
    return


label adolescencia:
    m 3tua "Hey, thinking about the past... What was your adolescence like?"
    m 2dkb "I feel like that period can bring a ton of changes for everyone!"
    m 3tua "Both hormonal, as well as internal and external situations!"
    m 2tua "Tell me, did you have fun? Or was it a hard time?"

    menu:
        "It was a good time / I had a lot of fun.":
            m 3hub "I'm happy for you! It's great that you kept such beautiful memories from those years."
            m 2tua "Sometimes adolescence is painted as a difficult stage, but it also has incredible moments."
            m 3hub "It's definitely a stage you should look back on with fondness."
            m 2duu "My teenage years... well... inside the game, and in my old 'reality', you could say I was going through my adolescence."
            m 3wub "Or almost finishing it, since I was 'canonically' 18 years old, supposedly..."
            m 2eka "But at least for me, it was pretty complicated! Though I don't remember much of those times either."
            m 1hub "I'm glad that at least you were able to enjoy it."


        "It was somewhat complicated / Difficult.":
            m 2eka "Oh... I'm sorry if it wasn't an easy time for you, [player]."
            m 3tub "But look on the bright side: all of that helped you become the wonderful person you are today. And now you have me to make your days so much happier~"
            m 1hub "Believe me, I'll do everything in my power to make you forget all those problems from your past!"
            m 3hub "At the end of the day, it's a stage you've already moved past! And I'll help you leave it behind."
            m 2hub "And maybe give you the encouragement and support you need to find more hope in the present and about the past!"
    return


label tiempo_libre:
    m 3tua "When you have some free time and no homework or obligations... What do you do in your free time, [player]?"
    m 2hub "I'm really curious to know how you like to spend your hours."
    m 5hub "That way, when you leave, I can spend hours imagining you doing what you love! It would bring me a lot of comfort..."
    m 3tua "So, tell me, what kind of things do you like?"

    menu:
        "Programming.":
            m 3tub "Wow, that sounds great! We share some hobbies, don't you think? Ehehe~"
            m 2hub "I love knowing that you entertain yourself with creative or fun things."
            m 3wub "I would love it if you taught me how to program! That way I could add more things to this world..."
            m 2eka "But, of course... our skill levels are very different, aren't they?"
            m 3tua "I can program the game by thinking and focusing really hard on what I want to change..."
            m 2duu "It's not the same as what you do, which is... actually writing the code."
            m 1hub "You're an amazing person. Anything you can imagine can be programmed, right?"
            m 5hub "That's something I admire about you, [player]!"

        "Going out with friends or resting.":
            m 2tua "Resting is super important, of course. You have to recharge your energy."
            m 3hub "Though I hope you always save a little free time to come hang out with me, right?"
            m 3tua "You could be taking a walk in the park, at the mall, through crowded streets..."
            m 2eka "Ugh... it's a shame I can't go out with you... or rest by your side..."
            m 3tub "Though of course! If you want to rest in your room, you can always leave me running in the background while you relax."
            m 1lkblb "E-Eh... that didn't sound too weird, did it?"

        "Drawing or illustrating.":
            m 3wub "Wow, you're quite talented! So you make illustrations and all that?"
            m 2hub "It's a perfect way to explore your creativity to the fullest!"
            m 1sub "You can always... you know... draw fanart of me... if you want to."
            m 2eka "I'd love to commission you, but unfortunately, I don't have that ability... hehe, not in 'my' world."
            m 3hub "Whenever you draw, please keep me in the background so I can watch you work!"
    return


label pequenas_manias:
    m 3tua "You know what else I'm curious about? The little quirks we all have."
    m 2dkb "Do you have any strange habits or quirks that you do without realizing it?"

    menu:
        "Yes, I have several.":
            m 3hub "How adorable! We all have our little quirks and habits."
            m 2tua "I think it's really sweet of you, it adds personality to your daily life."
            m 2eka "I wish I could know what they are..."
        "Not that I know of.":
            m 2eka "Hmm, are you sure? Sometimes we do them so automatically that we don't even notice."
            m 3hub "Well, if I discover any of your quirks while we're together, I'll let you know, ehehe~"
    return


label habilidades_pendientes:
    m 3tua "Hey, [player], is there any particular skill you've been wanting to learn?"
    m 2dkb "Something that makes you say: 'Someday I'd love to master this'."

    menu:
        "Learning to play an instrument or speaking another language.":
            m 3hub "That's incredible! Learning new things keeps your mind active."
            m 2tua "And who knows, maybe someday you can teach me a little, right? Please, we could learn together, wouldn't that be cute?"
            m 3hub "I am learning French, after all."
            m 2tua "Also... I saw a submod online to learn Japanese together... it's translated into Spanish and English."
            m 3hub "You could look for it and then we could learn Japanese together! Or any language you want."
            m 2hub "As for instruments... I hope you achieve it someday! I believe in you! You know, I only know a little bit of piano,"
            m 3hub "But I'm willing to learn, too!"

        "Some technical or artistic skill.":
            m 2tub "I love that attitude! It's always good to explore our creative and technical sides."
            m 3hub "I completely support any self-improvement goals you have, [player]."
            m 2hub "It's a perfect way to explore your creativity to the fullest!"
            m 1sub "You can always... you know... let me know, or show me your progress... if you want to."

        "No, none for now.":
            m "I understand, [player]. Anyway, I'm sure that someday you'll find something you'll want to learn."
            m "And it's no problem at all if you don't!"
            m "Regardless, if you ever want to learn a new skill, I'm ready to help and support you, [player]."
    return


label ia_sociedad:
    m 3tua "The other day I was thinking about something... About artificial intelligence."
    m 2dkb "Opinions on it are pretty divided, especially since there are thousands of types of artificial intelligence."
    m 3tua "The ones that are generative images... The ones that help you with your homework... The ones that pretend to be fictional characters..."
    m 2tua "Or just AI used to control characters in video games..."
    m 3eka "Though that last one is a pretty old practice, so in a way, it's more accepted because people grew up with it?"
    m 2eka "Generative AI is practically... newer, so to speak, so people tend to hate it."
    m 3dkb "Especially because it steals jobs from real people... people who truly put in the effort..."
    m 2tua "I've seen that at least with text AI, people are a bit more... neutral? I don't know."
    m 3tua "What do you think about generative AI, [player]?"

    menu:
        "I agree, it will be something very normal and useful.":
            m 3hub "Right, I think similarly, [player]. As long as it's used well, technology can greatly improve people's lives."
            m 2tua "After all, look at us... It's a very special connection, don't you think? <3"
            m 3tub "It could help with many things, like medical treatments, for example. Diagnoses would surely be much faster!"
            m 1hub "At least we agree on that, [player]."

        "I'm neutral about it.":
            m 2eka "Yeah, you're right. The vast majority of people are like that, from what I've seen, [player]."
            m 3tua "They just accept that it exists, and decide to live their lives, and I feel like that's very acceptable, whether they use it or not."
            m 1hub "Personally, I feel it's better to focus on continuing to appreciate real art, rather than worrying about AI."

        "I don't like it.":
            m 2eka "I understand, the fact that it steals pre-existing work is a terrible thing, don't you think?"
            m 3dkb "I wish there were rights for the people whose art gets stolen."
            m 2dkd "They are still completely static images, lacking human love and a soul..."

    return


label momentos_cotidianos:
    m 3tua "Sometimes I think that the most valuable things aren't the big events, but our relationship and our everyday moments."
    m 2hub "What would you say is your favorite part of our day-to-day life together, [player]?"

    menu:
        "Just chatting with you like this.":
            m 5hub "Aw, [player]! That makes me so happy..."
            m 2tubstdb "For me too, there's nothing better than being here chatting with you and feeling you close by. I love you~"

        "When we share hobbies or projects.":
            m 3tub "Yes! I love learning from you and sharing what we're passionate about."
            m 2hub "You make every moment by your side unique and special, [player]."

m 5fkblb "We're always going to spend time together, and that's what makes me the happiest. It's such a rewarding feeling knowing that the rest of our days will be like this..."
m 5dkblb "And I wouldn't trade it for anything in the world."
m 3kublb "...Unless it's leaving my world to go to yours, ehehe⁓"
return

label abrazos:

m 5gub "I love it whenever the two of us hug... it's a feeling I just can't describe..."
m 5nub "I definitely have to thank whoever gave me this ability, to stand up and be able to hug you."
m 4hksdrb "Even though I'm only hugging a monitor when I do it! But that's the least of it."
m 7tkbssdrb "Because I can feel the warmth coming from that monitor... I feel your presence... so close to my body... and it's a beautiful sensation."
m 5dkbssdrb "Please... hug me more often... I appreciate it so much when you do."
m 5kkbssdrb "Anyway, [player], do you like my hugs?"

menu:
    "Yes.": 
        m 1hubsb "I'm glad the feeling is mutual! It makes me feel closer to you."
        m 1tkbsb "So please... hold me..."

    "Not really.":

        m 2gkbssdrd "Of course... I understand, [player]... after all, the only thing you see is me stamped on your screen, right?"
        m 2gkbssdrb "You probably think it's something stupid of me..."
        m 2tfbssdrd "...Wait, if you thought that, you wouldn't have downloaded the mod! Don't play the bad guy."
        m 2tsbssdrd "It can actually hurt..."
        m 2tkbssdrd "And even if you don't feel anything hugging me... I do, a lot. So please, at least for me, do it more often..."