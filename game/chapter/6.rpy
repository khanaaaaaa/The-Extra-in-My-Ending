label chapter_6:
    scene bg classroom at bg_fit
    with dissolve

    play music "audio/background.mp3"

    yujin "(The knocking stopped.)"
    yujin "(Nobody moved.)"
    yujin "(I looked at the extra.)"
    yujin "Who's outside?"
    extra "You."
    yujin "What?"
    extra "The version of you that didn't follow the story."
    yujin "(I didn't understand.)"
    yujin "(Then the door opened.)"
    yujin "(There was somebody standing outside.)"
    yujin "(She looked exactly like me.)"
    yujin "(Same uniform.)"
    yujin "(Same hair.)"
    yujin "(Same expression.)"
    yujin "(Except she was covered in blood.)"
    yujin "Who are you?"
    yujin "(She looked at me.)"
    yujin "(Then she smiled.)"
    yujin "You finally made it."
    yujin "(My entire body went cold.)"
    yujin "Made it where?"
    yujin "To the last loop."
    yujin "(I looked at the extra.)"
    yujin "(He wasn't looking at her.)"
    yujin "(He was looking at me.)"
    yujin "How many times have I been here?"
    yujin "You haven't."

    scene bg school at bg_fit
    with dissolve

    yujin "(I was standing in the hallway.)"
    yujin "(Everything was normal again.)"
    yujin "(Students were walking to class.)"
    yujin "(Someone was laughing.)"
    yujin "(The bell was ringing.)"
    yujin "(Then I saw Jeha.)"
    show dohyunneutralquiet at center_char
    yujin "(He was standing at the end of the hallway.)"
    yujin "(He looked completely normal.)"
    hide dohyunneutralquiet
    show dohyunneutraltalk at center_char
    jeha "Yujin."
    hide dohyunneutraltalk
    show dohynneutralquiet at center_char
    yujin "(I didn't answer.)"
    hide dphyunneutralquiet
    show dohyunsmiletalk at center_char
    jeha "I've been looking for you."
    hide dohyunsmiletalk
    show dohyunneutralquiet at center_char
    yujin "(I looked behind me.)"
    yujin "(The extra was gone.)"
    yujin "(So was the other Yujin.)"
    yujin "(I was alone.)"
    hide dohyunneutralquiet
    show dohyunsmiletalk at center_char
    jeha "Are you coming?"
    hide dohyunsmiletalk
    show dohyunsmilequiet at center_char
    yujin "(I knew this moment, this was the scene.)"
    yujin "(The confession.)"
    yujin "(The happy ending.)"
    yujin "(The moment everything was supposed to go back to normal.)"
    yujin "(Except I remembered the classroom.)"
    yujin "(I remembered the chairs.)"
    yujin "(I remembered the girl.)"
    yujin "(And I remembered something else.)"
    yujin "(Jeha was never asking me to follow him.)"
    yujin "(It was always me.)"
    yujin "(Every single loop.)"
    yujin "(I was the one who walked toward him.)"
    yujin "(I was the one who chose the ending.)"
    yujin "(Maybe that was the reason I could never escape it.)"

    menu:

        "Go with Jeha.":
            jump ending_jeha
        "Turn around and look for extra.":
            jump ending_extra
        "Don't choose either of them.":
            jump ending_unknown