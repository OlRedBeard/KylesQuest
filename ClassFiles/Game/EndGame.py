def YouDied(you):
    print("\n\n\n")
    if you.situation == "Wither":
        print(f"With that, {you.name} had taken the leap from 'more sleep' to 'the big sleep.'\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"It took several weeks for {you.name}'s neighbours to notice that the terrible aroma eminating from the apartment was a different one than usual.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"In the end, {you.name} was buried in a discount coffin, the amount of people wearing Oakleys at the funeral was truly a sight to behold.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("Thank you for playing, you got Ending 1/31\n") #ending 1
        input("Press any key to continue.")
        you.spot = "gameover"

    elif you.situation == "Axe":
        print(f"A few days passed with {you.name} laying dead on the bathroom floor in a congealing pool of blood and body spray.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"Once the pungent fumes of the Axe cleared a few weeks later, the neighbours started to notice the change from the typical stench and this new one.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"When {you.name} was discovered, they were given a proper burial in a discount coffin. The mourners had discovered that Affliction makes suits too.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("Thank you for playing, you got Ending 2/31\n") #ending 2
        input("Press any key to continue.")
        you.spot = "gameover"

    elif you.situation == "Slipped":
        print(f"The following day, {you.name}'s downstairs neighbour noticed their bathroom ceiling leaking, and the landlord was sent to investigate.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"When the landlord entered they discovered {you.name} fully nude, facedown in a full bathtup with the shower running.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"A small funeral was held for {you.name}, later there was a heated debate over which of the mourners would inherit his stockpile of energy drinks.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("Thank you for playing, you got Ending 3/31\n") #ending 3
        input("Press any key to continue.")
        you.spot = "gameover"

    elif you.situation == "Monster":
        print(f"It took quite some time before {you.name} was discovered, as the neighbours had come to expect horrific smells from the apartment.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"When details of {you.name}'s demise reached the news outlets, Monster energy decided to sponsor {you.name}'s funeral.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"There were skateboarders doing tricks on half-pipes, and the mourners arrived via monster truck. {(you.name).capitalize()} was buried in a coffin branded with")
        print("the Monster energy logo. Somehow, you think this is exactly what they would've wanted...\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("Thank you for playing, you got Ending 4/31\n") #ending 4
        input("Press any key to continue.")
        you.spot = "gameover"

    elif you.situation == "Sludge":
        print(f"When {you.name} failed to pay rent for several days, the landlord went in to investigate. They found no sign of {you.name} in the apartment.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"Assuming the place was abandoned, the landlord hired cleaners to thoroughly scrub the apartment from top to bottom so it could be rented out again.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("While many of the stains were suspicious, the most confusing one was the one that seemed to travel from the fridge to the apartment's bathroom.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("It was as though someone had dragged some black oily goo all along the floor and stuffed it down the tub drain. Interestingly, the fridge's cripser drawer")
        print("was immaculately clean.\n") 
        input("Press any key to continue.")
        print("\n\n\n")
        print("Thank you for playing, you got Ending 5/31\n") #ending 5
        input("Press any key to continue.")
        you.spot = "gameover"

def YouLeft(you):
    print("\n\n\n")
    if you.event == "Interview":
        print(f"With confidence in their heart, {you.name} left their apartment to make way to their job interview.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        if you.clothed == False:
            print(f"Ignoring the (apparently) familiar looks of concern and disappointment from the few neighbours that they past, {you.name} strode down the stairs and")
            print("out the apartment's front door to the street outside.\n")
            input("Press any key to continue.")
            print("\n\n\n")
            print(f"It was only then that {you.name} realized they hadn't put on clothes that day...\n")
            input("Press any key to continue.")
            if you.haskeys == True:
                print("\n\n\n")
                print(f"With a sudden flood of shame you didn't think that {you.name} was capable of feeling, they quickly unlocked the apartment door and ran inside.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"Breathing heavy and completely flustered from the experience, {you.name} laid down on the livingroom futon and decided to call the day a wash...\n")
                input("Press any key to continue.")
                print(f"\n\n\n")
                print(f"{(you.name).capitalize()} missed their interview, but if there is anything worse than NOT showing up, it's showing up nearly nude.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print("Thank you for playing, you got Ending 6/31\n") #ending 6
                input("Press any key to continue.")
                you.spot = "gameover"

            elif you.haskeys == False:
                print("\n\n\n")
                print(f"With a sudden flood of shame you didn't think that {you.name} was capable of feeling, they quickly turned around to run back inside the apartment.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"Unfortunately for {you.name}, they hadn't grabbed their keys before leaving the apartment. They tugged on the door frantically while screaming.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"This only served to attract more attention to {you.name} and their thread-bare leopard print thong, strangers were recording on their phone.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"After awhile, the police arrived to deal with the nudist seemingly attempting to break in to the building.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"{(you.name).capitalize()} explained to the police that they lived in the building and had accidentally locked themselves out.")
                print(f"The officers, clearly unsure about the seeming maniac trying to tug a door off its hinges asked if {you.name} had any proof of this.\n")
                input("Press any key to continue.")
                if you.haswallet == True:
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} grabbed their wallet (don't ask where they were keeping it) and showed the officers their ID.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"The officers helped get {you.name} back inside, giving them a blanket to cover up with. And got the landlord to let {you.name} back into their apartment.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"Exhausted from the combination of adrenaline, shame, confusion, and fear, {you.name} collapsed on the futon.")
                    print("They vowed never again to go to a job interview for fear this could happen again. So at least they learned the wrong lesson here.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print("Thank you for playing, you got Ending 7/31\n") #ending 7
                    input("Press any key to continue.")
                    you.spot = "gameover"

                elif you.haswallet == False:
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} frantically searched their body for their wallet, but found that it was missing. Likely still in the apartment.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"With no reason to believe that {you.name} was anything more than a risque lunatic, the police arrested them for indecent exposure.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} spent the rest of the day in a jail cell, thankfully having been given some clothing before being placed in the holding cell.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"Unforunately, this meant that {you.name} missed their big interview. But one of the videos of {you.name} attempting to break the door down did go")
                    print(f"viral. And {you.name} took comfort in the fact that at least they were a little more famous now.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print("Thank you for playing, you got Ending 8/31\n") #ending 8
                    input("Press any key to continue.")
                    you.spot = "gameover"

        elif you.clothed == True:
            print(f"Whistling their favourite Nickleback tune, {you.name} strode down the stairs and out the front doors to the street outside, making their way toward their interview.\n")
            input("Press any key to continue.")
            print("\n\n\n")
            if you.shoed == True:
                print(f"After a brief walk, {you.name} arrived at the interview, and waited anxiously for the interviewer to arrive. It seems {you.name} really wants this job.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"The door opened, and a middle-aged woman in a tasteful suit entered the room, she apologized for the delay and sat accross the desk from {you.name}.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                if you.clean == False and you.spray < 2:
                    print(f"Crinkling her nose slightly, the interviewer looked around puzzled for a moment before settling her gaze back on {you.name}.")
                    print(f"It was at that moment that {you.name} remembered that people usually shower before interviews.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"She asked some routine questions, clearly trying to keep as much physical distance from {you.name} as possible. And ended the interview quite quickly.")
                    print(f"As the woman hurried out of the room while holding her breath, {you.name} sighed deeply.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} made it to the interview, but sadly did not get the job.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print("Thank you for playing, you got Ending 9/31\n") #ending 9
                    input("Press any key to continue.")
                    you.spot = "gameover"

                elif you.clean == False and you.spray >= 2:
                    print(f"For a moment, she looked around puzzled, her nostrils moving slightly as she seemed to be trying to identify the unusual aroma filling the room.")
                    print(f"{(you.name).capitalize()} realized that they had not showered that day, but hoped the body spray they put on would cover it up.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"The interviewer began asking {you.name} standard questions about availability while giving a resume another quick look through.")
                    print(f"'So,' she said calmly, 'what do you think you would bring to this position?' {(you.name).capitalize()} held back a laugh at the word 'position.'\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    if you.fed == False:
                        print(f"As soon as {you.name} went to respond they began feeling faint, it seems in their excitement they had forgotten to eat.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"Your vision went blurry as {you.name} passed out from low blood sugar. Hardly a great first impression to a would-be employer.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, but didn't make a great impression.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 10/31\n") #ending 10
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.fed == True and you.monster < 2:
                        print(f"{(you.name).capitalize()} gave their most diplomatic of answers, making careful efforts not to call the interviewer 'bro' at any point.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"After several more questions back and forth, the interviewer thanked {you.name} for their time and told them the company would let them know.")
                        print(f"As she shook {you.name}'s hand, her nostrils once again twitched as if struggling to identify that bizarre medly of aromas.\n")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, and thinks it went alright overall.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 11/31\n") #ending 11
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.fed == True and you.monster >= 2:
                        print(f"As {you.name} went to answer, instead of words out came a catastrophically loud belch. The interviewer sat in stunned silence.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} apologized for their gastrointestinal outburst, and the interviewer assured them it was fine and carried on.")
                        print(f"Several more questions were asked, and in the end she thanked {you.name} for their time and said the company would let them know.\n")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, and showed the interviewer how loud he could burp.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 12/31\n") #ending 12
                        input("Press any key to continue.")
                        you.spot = "gameover"

                elif you.clean == True and you.spray < 2:
                    print(f"The interviewer smiled politely at {you.name} and made polite small talk about the weather and how {you.name}'s morning had been.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"As the interview progressed, she asked {you.name} a series of routine questions, and {you.name} responded as politely as possible.")
                    print(f"'So,' she said calmly, 'what do you think you would bring to this position?' {(you.name).capitalize()} held back a laugh at the word 'position.'\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    if you.fed == False:
                        print(f"As soon as {you.name} went to respond they began feeling faint, it seems in their excitement they had forgotten to eat.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"Your vision went blurry as {you.name} passed out from low blood sugar. Hardly a great first impression to a would-be employer.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, but passed out from hunger.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 13/31\n") #ending 13
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.fed == True and you.monster < 2:
                        print(f"{(you.name).capitalize()} gave their most diplomatic of answers, making careful efforts not to call the interviewer 'bro' at any point.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"After several more questions back and forth, the interviewer thanked {you.name} for their time and told them the company would let them know.\n")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, and thinks it went pretty good!\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 14/31\n") #ending 14
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.fed == True and you.monster >= 2:
                        print(f"As {you.name} went to answer, instead of words out came a catastrophically loud belch. The interviewer sat in stunned silence.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} apologized for their gastrointestinal outburst, and the interviewer assured them it was fine and carried on.")
                        print(f"Several more questions were asked, and in the end she thanked {you.name} for their time and said the company would let them know.\n")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, and belched louder than ever before.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 15/31\n") #ending 15
                        input("Press any key to continue.")
                        you.spot = "gameover"

                elif you.clean == True and you.spray >= 2:
                    print(f"The interviewer smiled politely at {you.name} and made polite small talk about the weather and how {you.name}'s morning had been.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"Before starting with the questions, the interviewer paused and looked at {you.name} for a moment. 'May I ask a personal question?'")
                    print(f"{(you.name).capitalize()} had been preparing for this moment since the first time they saw an Axe commercial.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"'Are you wearing the new Axe scent?' she continued. {(you.name).capitalize()} nodded in response, possibly a little TOO eagerly.")
                    print(f"She continued with the standard questions, fiddling with her pen as she did so. {(you.name).capitalize()} was waiting for her to pounce.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"'So,' she said calmly, 'what do you think you would bring to this position?' {(you.name).capitalize()}'s eyes widened at the word 'position.'\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    if you.fed == False:
                        print(f"As soon as {you.name} went to respond they began feeling faint, it seems in their excitement they had forgotten to eat.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"Your vision went blurry as {you.name} passed out from low blood sugar. Hardly a great first impression to a would-be employer.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, but fainted because of forgetting that whole 'eating' thing.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 16/31\n") #ending 16
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.fed == True and you.monster < 2:
                        print(f"{(you.name).capitalize()} gave their most diplomatic of answers, trying to avoid staring directly at the interviewer's chest.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"After several more questions back and forth, the interviewer thanked {you.name} for their time. She noted that his application was")
                        print(f"definitely in the short list for candidates. Way to go {you.name}!")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to the interview, and made a great impression!\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 17/31\n") #ending 17
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.fed == True and you.monster >= 2:
                        print(f"As {you.name} went to answer, instead of words out came a catastrophically loud belch. The interviewer sat in stunned silence.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} apologized for their gastrointestinal outburst, but the interviewer held up her hand to stop him from continuing.")
                        print(f"'Let me be honest with you,' she said. 'Since walking into this room, all I've been able to smell is Axe.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"'On top of that, you've been staring at my chest for the last 10 minutes. I can't even tell if you were TRYING to conceal it.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("She slammed her hand down on the table as she continued, 'and now you let out a belch that only an energy drink addict could muster.'")
                        print(f"'I have just one thing to say to you...' {(you.name).capitalize()} still wasn't sure if she was flirting with him or not.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"'You are EXACTLY the type of person we've been looking for here!' She exclaimed enthusiastically. 'Congratulations, {you.name}! You")
                        print("are the referee for the first Ed Hardy Wet T-Shirt Oil Wrestling Championship hosted by Fred Durst!\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} made it to their interview, and with your help has finally landed their dream job!\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 18/31\n") #ending 18 (TRUE ENDING)
                        input("Press any key to continue.")
                        you.spot = "gameover"

            elif you.shoed == False:
                print(f"Unfortunately, after a few blocks of walking {you.name}'s shoeless feet began to ache and sting from the rough bits of gravel and garbage that")
                print(f"they had stepped on over the course of their walk. Sadly, this meant that {you.name} was moving slowly, and by the time he arrived the interviewer")
                print("had already gone home for the day.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"{(you.name).capitalize()} forgot to wear shoes, and was late to their interview.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print("Thank you for playing, you got Ending 22/31\n") #ending 22
                input("Press any key to continue.")
                you.spot = "gameover"
        
    else:
        print(f"Fed up with the filth and odour of the apartment, you steer {you.name} out of the apartment into the world at large.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        if you.clothed == False:
            print(f"Ignoring the (apparently) familiar looks of concern and disappointment from the few neighbours that they past, {you.name} strode down the stairs and")
            print("out the apartment's front door to the street outside.\n")
            input("Press any key to continue.")
            print("\n\n\n")
            print(f"It was only then that {you.name} realized they hadn't put on clothes that day...\n")
            input("Press any key to continue.")
            if you.haskeys == True:
                print("\n\n\n")
                print(f"With a sudden flood of shame you didn't think that {you.name} was capable of feeling, they quickly unlocked the apartment door and ran inside.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"Breathing heavy and completely flustered from the experience, {you.name} laid down on the livingroom futon and decided to call the day a wash...\n")
                input("Press any key to continue.")
                print(f"\n\n\n")
                print(f"{(you.name).capitalize()} flashed their neighborhood and went back to sleep under the weight of their shame.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print("Thank you for playing, you got Ending 19/31\n") #ending 19
                input("Press any key to continue.")
                you.spot = "gameover"

            elif you.haskeys == False:
                print("\n\n\n")
                print(f"With a sudden flood of shame you didn't think that {you.name} was capable of feeling, they quickly turned around to run back inside the apartment.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"Unfortunately for {you.name}, they hadn't grabbed their keys before leaving the apartment. They tugged on the door frantically while screaming.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"This only served to attract more attention to {you.name} and their thread-bare leopard print thong, strangers were recording on their phone.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"After awhile, the police arrived to deal with the nudist seemingly attempting to break in to the building.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                print(f"{(you.name).capitalize()} explained to the police that they lived in the building and had accidentally locked themselves out.")
                print(f"The officers, clearly unsure about the seeming maniac trying to tug a door off its hinges asked if {you.name} had any proof of this.\n")
                input("Press any key to continue.")
                if you.haswallet == True:
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} grabbed their wallet (don't ask where they were keeping it) and showed the officers their ID.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"The officers helped get {you.name} back inside, giving them a blanket to cover up with. And got the landlord to let {you.name} back into their apartment.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"Exhausted from the combination of adrenaline, shame, confusion, and fear, {you.name} collapsed on the futon.")
                    print(f"Weeks later, {you.name} became known to millions as 'Thong Bro.' It seems one of the videos the neighbours had taken of {you.name} went viral.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print("Thank you for playing, you got Ending 20/31\n") #ending 20
                    input("Press any key to continue.")
                    you.spot = "gameover"

                elif you.haswallet == False:
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} frantically searched their body for their wallet, but found that it was missing. Likely still in the apartment.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"With no reason to believe that {you.name} was anything more than a risque lunatic, the police arrested them for indecent exposure.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} spent the rest of the day in a jail cell, thankfully having been given some clothing before being placed in the holding cell.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} was soon thereafter shown one of the videos of themself screaming and tugging on the locked door in a thong.")
                    print(f"The video was already exploding with popularity, and {you.name} felt their smile return as they had a new found level of popularity!\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print("Thank you for playing, you got Ending 21/31\n") #ending 21
                    input("Press any key to continue.")
                    you.spot = "gameover"
        
        elif you.clothed == True:
            print(f"{(you.name).capitalize()} trotted down the apartment stairs and out the front door, seemingly planning a little recreational walk around the block.\n")
            input("Press any key to continue.")
            print("\n\n\n")
            if you.shoed == False:
                print(f"Walking along the street suddenly {you.name} felt a sharp pain in their foot. Looking down they saw a rusty old nail poking out of their shooeless")
                print(f"foot. {(you.name).capitalize()} squatted down onto the ground to pull the nail from their sole, after which they slowly limped back to their apartment.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                if you.haskeys == True:
                    print(f"{(you.name).capitalize()} hobbled their way back to their apartment, and sat down on the futon with a sigh. Today just didn't go great.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print(f"{(you.name).capitalize()} forgot to put on shoes and got a nasty foot-wound. (And probably tetanus)\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    print("Thank you for playing, you got Ending 23/31\n") #ending 23
                    input("Press any key to continue.")
                    you.spot = "gameover"

                elif you.haskeys == False:
                    print(f"However, after arriving at the building {you.name} realized that they had forgotten their keys. They couldn't get back into their apartment.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    if you.haswallet == True:
                        print(f"{(you.name).capitalize()} decided to hop on one foot across the street, to the coffee shop. Where they disgusted several patrons by insisting")
                        print("on showing them the new 'war wound' on their foot while sipping on a fresh cup of coffee.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} spent the day grossing out strangers by showing them a hole they punched in their foot by not wearing shoes.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 24/31\n") #ending 24
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.haswallet == False:
                        print(f'{(you.name).capitalize()} patted their pockets for their wallet and realized they had forgotten that too. Concerned that sitting outside until')
                        print(f"someone let them into the building may end badly with the new foot wound, {you.name} decided something had to be done.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} had heard of tourniquets before, and not fully understanding what they are or what they were for, took off their sock")
                        print(f"and tied it as tightly as possible around their ankle. {(you.name).capitalize()} then laid down in the alley for a relaxing nap.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} tied a sock around their ankle and called it medicine... And ended up losing their foot.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 25/31\n") #ending 25
                        input("Press any key to continue.")
                        you.spot = "gameover"

            elif you.shoed == True:
                print(f"{(you.name).capitalize()} wandered down the street toward a nearby convenience store, the somewhat faded 'Monster Energy' poster out front acted")
                print(f"like a beacon, drawing {you.name} in. Stepping inside the store {you.name}'s eyes immediately locked onto the energy drinks cooler.\n")
                input("Press any key to continue.")
                print("\n\n\n")
                if you.haswallet == True:
                    print(f"{(you.name).capitalize()} grabbed as many Monster energy drinks as their arms could hold and proudly marched them up to the counter.")
                    print(f"They paid on credit card and happily skipped back to their apartment.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    if you.haskeys == True:
                        print(f"{(you.name).capitalize()} happily re-entered their apartment with an armful of liquid poison and plopped down on the futon.")
                        print(f"They cracked open a fresh can of some esoteric flavour like 'riptide' or 'bike ride' or whatever and fired up a game of CoD.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} excitedly bought energy drinks and spent the rest of the day relaxing.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 26/31\n") #ending 26
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.haskeys == False:
                        print(f"When {you.name} returned to the building, they quickly realized that they had left their keys inside. At least there were plenty of cans")
                        print(f"of Monster to keep them company while they wait for someone to let them in!\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"After chugging down numerous cans on the front step, {you.name}'s eye gave an erratic twitch as their heart suddenly stopped.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} died on their front step, veins running green with whatever the hell 'Carnitine L-Tartrate' is.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 27/31\n") #ending 27
                        input("Press any key to continue.")
                        you.spot = "gameover"

                elif you.haswallet == False:
                    print(f"After opening the cooler, {you.name} pauses for a moment to check their pockets, only to realize they have forgotten their wallet.")
                    print(f"Shoulders slumped and head hung low, {you.name} slowly wandered back to their apartment.\n")
                    input("Press any key to continue.")
                    print("\n\n\n")
                    if you.haskeys == True:
                        print(f"{(you.name).capitalize()} wandered back upstairs to their apartment and flopped down on the futon releasing a cloud of trapped flatulence.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} tried to buy an energy drink, forgot their wallet, and spent the day moping about it.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 28/31\n") #ending 28
                        input("Press any key to continue.")
                        you.spot = "gameover"

                    elif you.haskeys == False:
                        print(f"Upon arriving, however, {you.name} realized that they had forgotten their keys. They fell to their knees and started screaming at the heavens.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"People wandering the neighbourhood began to gawk at the man letting out a pained scream on the steps of an apartment with his fists held high.")
                        print(f"After running out of breath to scream, {you.name} tuckered themself out and curled up on the front step for a nap.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print(f"{(you.name).capitalize()} had a really lousy day.\n")
                        input("Press any key to continue.")
                        print("\n\n\n")
                        print("Thank you for playing, you got Ending 29/31\n") #ending 29
                        input("Press any key to continue.")
                        you.spot = "gameover"

def YouGamed(you):
    print("\n\n\n")
    if you.event == "Interview":
        print(f"{(you.name).capitalize()} fired up 'one more match' which quickly turned into 'a day long gaming binge,' completely ignoring their big interview.")
        print(f"You don't necessarily get a sense that {you.name} is disappointed in themself, but they do seem a little mopey.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"{(you.name).capitalize()} ignored their obligations and spent the day gaming, and I'm sure no one reading this can identify with that...\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("Thank you for playing, you got Ending 30/31\n") #ending 30
        input("Press any key to continue.")
        you.spot = "gameover"
    else:
        print(f"{(you.name).capitalize()} kicked up their feet, creating a miniature avalanche of empty fast food containers and cups. They played hours upon hours playing")
        print(f"various iterations of Call of Duty, chugging energy drinks, and shouting at their television.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print(f"{(you.name).capitalize()} spent their day exercising their trigger finger in a series of competitive death matches.\n")
        input("Press any key to continue.")
        print("\n\n\n")
        print("Thank you for playing, you got Ending 31/31\n") #ending 31
        input("Press any key to continue.")
        you.spot = "gameover"