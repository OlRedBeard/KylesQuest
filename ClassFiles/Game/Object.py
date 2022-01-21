nightstand_options = {'Lamp':'Turn on the lamp.','Phone':'Check the smartphone','Under':'Check under the nightstand.','Leave':'Go back.'}

def Nightstand(you):

    print("\n\n\n")
    print("On the nightstand next to you, you see a dusty table lamp and a smartphone.\n")
    numbers = 1
    ns_options_list = []

    if you.hasphone == True:
        if 'Phone' in nightstand_options.keys():
            del nightstand_options['Phone']
        else:
            pass

    for key in nightstand_options.keys():
        ns_options_list.append(key)

    if len(nightstand_options.values()) == 1:
        you.checkedns = True

    for value in nightstand_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(nightstand_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(nightstand_options.values())}): ")
        choice = int(choice)

        if ns_options_list[choice -1] == "Lamp":
            print("\n\n\n")
            print(f"After {you.name} makes a few attempts to turn on the lamp it becomes clear it is either unplugged or burnt out.")
            print("Given the amount of likely-flammable dust covering the bulb, you can't help but imagine that's for the best.\n")
            input("Press any key to continue.")
            del nightstand_options['Lamp']

        elif ns_options_list[choice -1] == "Phone":
            print("\n\n\n")
            print(f"You pick up what must be {you.name}'s phone, and give it a quick look over. It seems to have a passcode that you don't know.")
            print("You decide to take the phone with you, it might come in handy.\n")
            input("Press any key to continue.")
            you.hasphone = True
            del nightstand_options['Phone']

        elif ns_options_list[choice -1] == "Under":
            print("\n\n\n")
            print("Leaning down to peer beneath the nightstand you immediately ascertain that this nightstand must be like Las Vegas for spiders.")
            print("The sheer quantity of the cobwebs down here is as astounding as it is off-putting.\n")
            input("Press any key to continue.")
            del nightstand_options['Under']

        elif ns_options_list[choice -1] == "Leave":
            print("\n\n\n")
            print("Nightstands are pretty boring anyways.\n")
            input("Press any key to continue.")
            you.spot = you.last_spot

        break

phone_options = {'Code1':'Try 1234.','Code2':'Try 6969','Code3':'Try 1111','Leave':'Put the phone away.'}

def Phone(you):
    print("\n\n\n")
    if you.unlockedphone == False:
        print("On the screen you see a message has come in from someone simply named 'Bro', unfortunately the message contents don't show up. Guess the only way to learn")
        print(f"more about {you.name} is to crack this passcode.\n")
    else:
        print(f"You unlock {you.name}'s phone once more to see if there is any more information you can glean from its contents.\n")

    numbers = 1
    phone_options_list = []

    for key in phone_options.keys():
        phone_options_list.append(key)

    if len(phone_options.values()) == 1:
        you.checkedphone = True

    for value in phone_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(phone_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(phone_options.values())}): ")
        choice = int(choice)

        if phone_options_list[choice -1] == 'Code1':
            print("\n\n\n")
            print(f"You tap in 1234 and the phone's UI shakes dramatically before informing you that the passcode is incorrect.\n")
            input("Press any key to continue.")
            del phone_options['Code1']

        elif phone_options_list[choice -1] == 'Code2':
            print("\n\n\n")
            print(f"Sensing that {you.name} is incredibly mature, you tap in 6969 for the phone's passcode.")
            print("The phone unlocks! Look at you solving problems!\n")
            input("Press any key to continue.")
            del phone_options['Code2']
            if 'Code1' in phone_options.keys():
                del phone_options['Code1']
            else:
                pass
            if 'Code3' in phone_options.keys():
                del phone_options['Code3']
            else:
                pass
            phone_options['Texts'] = 'Check text messages.'
            phone_options['Calendar'] = 'Check the calendar.'
            you.unlockedphone = True

        elif phone_options_list[choice -1] == 'Code3':
            print("\n\n\n")
            print(f"You tap in 1111 and the phone's UI shakes dramatically before informing you that the passcode is incorrect.\n")
            input("Press any key to continue.")
            del phone_options['Code3']

        elif phone_options_list[choice -1] == 'Leave':
            print("\n\n\n")
            print(f"You decide there are more important things to do than mess with {you.name}'s phone right now.\n")
            input("Press any key to continue.")
            you.spot = you.last_spot

        elif phone_options_list[choice -1] == "Texts":
            print("\n\n\n")
            print(f"You open up the messaging app and check the unread message, it reads:\n")
            print("'Hey Kyle! Good luck today, bro!'\n")
            print(f"Looks like {you.name}'s name is Kyle. That's good to know!\n")
            input("Press any key to continue.")
            you.name = "Kyle"
            del phone_options['Texts']

        elif phone_options_list[choice -1] == "Calendar":
            print("\n\n\n")
            print(f"Opening the calendar app you see an a single event in a sea of open days. It's today! The event reads 'Job Interview.'")
            print(f"Looks like {you.name} has a big interview today, better make sure to get ready for that!\n")
            input("Press any key to continue.")
            you.event = "Interview"
            del phone_options['Calendar']

        break

dresser_options = {'Check':'Check the drawers.','Leave':'Go back.'}

def Dresser(you):
    print("\n\n\n")
    print(f"The dresser seems pretty standard, if remarkably unclean. By the level of dust on the drawers you can tell that {you.name} only uses one of these.\n")

    numbers = 1
    dresser_options_list = []

    for key in dresser_options.keys():
        dresser_options_list.append(key)

    if you.clothed == True:
        if 'Clothes' in dresser_options.keys():
            del dresser_options['Clothes']

    if len(dresser_options.values()) == 1:
        you.checkeddresser = True

    for value in dresser_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(dresser_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(dresser_options.values())}): ")
        choice = int(choice)

        if dresser_options_list[choice -1] == 'Check':
            print("\n\n\n")
            print(f"As you open the drawer you are unsurprised to find that {you.name} doesn't seem to fold their clothing. Shockingly, however, you find that all")
            print("the standard and necessary clothing items are here. Though the sheer number of 'Affliction' logos is somewhat off-putting.\n")
            input("Press any key to continue.")
            del dresser_options['Check']
            dresser_options['Clothes'] = 'Put on clothes.'

        elif dresser_options_list[choice -1] == 'Leave':
            print("\n\n\n")
            print("If you've seen one disgustingly unclean dresser, you've seen them all.\n")
            input("Press any key to continue.")
            you.spot = "bedroom"

        elif dresser_options_list[choice -1] == 'Clothes':
            print("\n\n\n")
            print(f"You grab the least garish of clothing and guide {you.name} to covering their near-nudity with over-priced clothing.")
            print("One step closer to looking vaguely presentable!\n")
            input("Press any key to continue.")
            you.clothed = True

        break

shower_options = {'Sing':'Sing in the shower.','Dance':'Dance in the shower'}

def Shower(you):
    print("\n\n\n")
    print(f"It would seem {you.name} is a bit uneasey in the shower, almost as if they don't get in here that often. You should do something to keep them from bolting out.\n")

    numbers = 1
    shower_options_list = []

    for key in shower_options.keys():
        shower_options_list.append(key)

    for value in shower_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(shower_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(shower_options.values())}): ")
        choice = int(choice)

        if shower_options_list[choice -1] == 'Sing':
            print("\n\n\n")
            print(f"Deciding to exercise some musical muscles, {you.name} begins belting out rhythmless versions of Limp Bizkit's best hits.")
            print(f"'Best' is definitely a very subjective term. After awhile {you.name} is suitably clean and you exit the shower.")
            print(f"You dry {you.name} off with a suspiciously crunchy towel and hang it back over the towel rack.\n")
            input("Press any key to continue.")
            you.clean = True
            you.spot = "bathroom"

        elif shower_options_list[choice -1] == 'Dance':
            print("\n\n\n")
            print(f"Terrified of hearing {you.name}'s 'singing voice' you decide to shake your groove thang a little bit while soaping up.")
            print(f"This turns out to be a terrible idea, it isn't long before {you.name} slips and tumbles over.")
            print("You strike your head against the faucet with a sickening 'CRACK' and your vision slowly fades as the water cascades down upon your face.")
            print(f"And so, {you.name} dies naked on the shower floor.\n")
            input("Press any key to continue.")
            you.spot = "dead"
            you.situation = "Slipped"

        break

fridge_options = {'Look':'Look for food.','Leave':'Go back.'}

def Fridge(you):
    print("\n\n\n")
    print(f"Opening the fridge you see that it is not an oasis of cleanliness in this desert of disgusting. It is as covered in sludge and debris as it is empty.\n")

    numbers = 1
    fridge_options_list = []

    for key in fridge_options.keys():
        fridge_options_list.append(key)

    for value in fridge_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(fridge_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(fridge_options.values())}): ")
        choice = int(choice)

        if fridge_options_list[choice -1] == "Look":
            print("\n\n\n")
            print(f"Searching for sustainance in {you.name}'s fridge is something of a fruitless endeavor, it seems the only items with anything resembling nutritional")
            print("value are a ketchup packet and a wide array of Monster energy drinks.")
            print("The bottom crisper drawers are overflowing with a horrifying black sludge.\n")
            input("Press any key to continue.")
            fridge_options['Ketchup'] = 'Eat a ketchup packet.'
            fridge_options['Monster'] = 'Drink a Monster.'
            fridge_options['Sludge'] = 'Investigate the sludge.'
            del fridge_options['Look']

        elif fridge_options_list[choice -1] == "Leave":
            print("\n\n\n")
            print(f"You're fairly confident the only thing you would get out of this fridge is depression... And maybe E. coli...\n")
            input("Press any key to continue.")
            you.spot = "kitchen"

        elif fridge_options_list[choice -1] == "Ketchup":
            print("\n\n\n")
            print(f"You grab the strangely bloated ketchup package and split it open, you can feel the hairs in {you.name}'s nose curl with the stinging vinegar scent.")
            print(f"You squirt the ketchup into {you.name}'s mouth like a yogurt tube, you really didn't expect it to be this... Chewy...")
            print(f"Unfortunately, despite this brave endeavour, {you.name} still seems hungry.\n")
            input("Press any key to continue.")
            del fridge_options['Ketchup']

        elif fridge_options_list[choice -1] == "Monster":
            print("\n\n\n")
            if you.monster == 0:
                print(f"With an odd sensation of glee, {you.name} deftly cracks open the can of Monster energy drink and guzzles the entire thing at once.")
                print(f"You'd make a comment about what {you.name} must've picked up in college if you weren't fairly confident they never went.")
                print(f"Strangely, {you.name} seems gung-ho to grab another one.\n")
                input("Press any key to continue.")
                fridge_options['Monster'] = 'Drink another Monster.'
                you.monster = you.monster + 1

            elif you.monster == 1:
                print(f"Greedily, {you.name} slams back another Monster. Still it seems they are not satisfied with the level of caffeine and poison in their system.\n")
                input("Press any key to continue.")
                you.monster = you.monster + 1

            elif you.monster == 2:
                print(f"Another can down the hatch, {you.name} lets out a frighteningly loud belch and tosses the can over their shoulder. It feels as though they have")
                print("reached peak performance. There's no way that this could have serious health ramifications, right?")
                print(f"Yet still, {you.name} eyes another can longingly...\n")
                input("Press any key to continue.")
                you.monster = you.monster + 1
                you.fed = True

            elif you.monster == 3:
                print(f"With a mixture of excitement and trepidation, {you.name} opens one more can. As they shotgun its contents down their gullet they begin to feel")
                print("as though they've transcended the mortal world for something beyond...")
                print(f"Unfortunately that feeling was {you.name}'s heart giving out, {you.name} collapses dead on the kitchen floor.\n")
                input("Press any key to continue.")
                you.spot = "dead"
                you.situation = "Monster"

        elif fridge_options_list[choice -1] == "Sludge":
            print("\n\n\n")
            print(f"As {you.name} gently pulls on the crisper drawer handle a low, guttural growl emanates from within.")
            print("Whatever animal, vegetable, or mineral was stored in that drawer has clearly become a sentient ooze now. Best not to press the issue.\n")
            input("Press any key to continue.")
            fridge_options['Press'] = 'Press the issue.'
            del fridge_options['Sludge']

        elif fridge_options_list[choice -1] == "Press":
            print("\n\n\n")
            print(f"Well, you can't say I didn't warn you. As {you.name} approaches once more they tug the crisper drawer fully open and peer into it.")
            print(f"There's hardly enough time to be disgusted by what you see before a inky-black tendril launches out and grabs {you.name} by the neck.")
            print(f"Your vision goes black as {you.name}'s entire body is pulled into the crisper drawer and slowly dissolved by a beast of their own creation.\n")
            input("Press any key to continue.")
            you.spot = "dead"
            you.situation = "Sludge"

        break

cabinets_options = {'Look':'Search for food.','Leave':'Go back.'}

def Cabinets(you):
    print("\n\n\n")
    print(f"You open one cabinet, and then another, each time surprised by the sheer lack of ANYTHING within them. Seems {you.name} doesn't keep many non-perishables.\n")

    numbers = 1
    cabinets_options_list = []

    if len(cabinets_options.values()) == 1:
        you.checkedcabinets = True

    for key in cabinets_options.keys():
        cabinets_options_list.append(key)

    for value in cabinets_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(cabinets_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(cabinets_options.values())}): ")
        choice = int(choice)

        if cabinets_options_list[choice -1] == 'Look':
            print("\n\n\n")
            print(f"Determined to find something for {you.name} to eat, you scower every cabinet available, eventually finding a tub of protein powder.\n")
            input("Press any key to continue.")
            cabinets_options['Shake'] = 'Make a protein shake.'
            cabinets_options['Eat'] = 'Eat a scoop of protein powder.'
            del cabinets_options['Look']

        elif cabinets_options_list[choice -1] == 'Leave':
            print("\n\n\n")
            print(f"You close {you.name}'s cabinets back up after briefly considering hiding in them as a refuge from the endless filth you are surrounded by.\n")
            input("Press any key to continue.")
            you.spot = "kitchen"

        elif cabinets_options_list[choice -1] == 'Shake':
            print("\n\n\n")
            print(f"Looking around, you don't see a single clean cup. Nor do you see a clean bowl, vase, or spoon. Might make mixing a shake a bit difficult.\n")
            input("Press any key to continue.")
            cabinets_options['Hands'] = 'Make a protein shake in your cupped hand.'
            del cabinets_options['Shake']

        elif cabinets_options_list[choice -1] == 'Hands':
            print("\n\n\n")
            print(f"Gross. Okay, well {you.name} dumps a scoop of protein powder into their cupped hand and leans in over the revolting sink, pouring water on top of it")
            print("until their hand is nearly full. They stick a finger in the pile and roughly mix it up before drinking it.")
            if you.clothed == True:
                print(f"After slurping as much of the 'shake' as possible up from their hand, {you.name} wipes their hand off on their pants.\n")
            else:
                print(f"After slurping as much of the 'shake' as possible up from their hand, {you.name} licks their hands clean like a racoon.\n")
            input("Press any key to continue.")
            you.fed = True
            del cabinets_options['Hands']
            del cabinets_options['Eat']

        elif cabinets_options_list[choice -1] == 'Hands':
            print("\n\n\n")
            print(f"The familiarity with this process that {you.name} seems to have is incredibly worrying. After filling the little plastic scoop to the brim {you.name}")
            print("tilts their head back as far as it will go and dumps the powder into their open mouth. After several minutes of laboured swallowing and lip-smacking")
            print(f"{you.name} successfully manages to force the powder down into their stomach.\n")
            input("Press any key to continue.")
            you.fed = True
            if 'Shake' in cabinets_options.keys():
                del cabinets_options['Shake']
            if 'Hands' in cabinets_options.keys():
                del cabinets_options['Hands']
            del cabinets_options['Eat']

        break

futon_options = {'TV':'Turn on the TV.','Play':'Play some Xbox.'}

def Futon(you):
    print("\n\n\n")
    print(f"As you sit down on the futon, you notice both a TV remote and an Xbox controller on the seat next to you. It seems {you.name} is quite comfortable.")
    print(f"It may be a challenge to convince {you.name} to get back up off the futon now.\n")

    numbers = 1
    futon_options_list = []

    if you.tvon == True:
        if 'TV' in futon_options.keys():
            del futon_options['TV']

    if you.event == "Interview":
        if 'Leave' not in futon_options.keys():
            futon_options['Leave'] = 'Get off the futon.'

    for key in futon_options.keys():
        futon_options_list.append(key)

    for value in futon_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(futon_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(futon_options.values())}): ")
        choice = int(choice)

        if futon_options_list[choice -1] == 'TV':
            print("\n\n\n")
            print(f"You press the power button on the TV and see the Xbox menu screen. Pressing the button to change the source quickly lets you know that {you.name}")
            print("doesn't have cable. Too bad, you were hoping to catch some The Price is Right.\n")
            input("Press any key to continue.")
            del futon_options['TV']
            you.tvon = True

        elif futon_options_list[choice -1] == 'Xbox':
            print("\n\n\n")
            if you.tvon == True:
                print(f"You briefly flip through the available games on {you.name}'s Xbox. You pick out the latest Call of Duty over the host of Madden games.")
                if you.event == "Interview":
                    print(f"After a few matches, you remember {you.name} has a job interview! You might want to get off the futon and get going on that!\n")
                    input("Press any key to continue.")
                    futon_options['Xbox2'] = 'Just a few more matches...'
                    del futon_options['Xbox']
                else:
                    print(f"Sitting here shouting slurs at pre-teens and soaking in the sights of whatever war THIS iteration is meant to portray, {you.name} seems content.\n")
                    input("Press any key to continue.")
                    you.spot = "gaming"
            else:
                print(f"It would be very difficult to do that without the TV on.\n")
                input("Press any key to continue.")
                futon_options['TV'] = 'TURN. ON. THE. TV.'

        elif futon_options_list[choice -1] == 'Xbox2':
            print("\n\n\n")
            print(f"You cave in to {you.name}'s desire to keep playing games all day. I mean, what's the worst that could happen missing that interview?\n")
            input("Press any key to continue.")
            you.spot = "gaming"

        elif futon_options_list[choice -1] == 'Leave':
            print("\n\n\n")
            print(f"Summoning a level of self-restraint that you couldn't have possibly imagined given the state of this place, {you.name} gets up from the futon.\n")
            input("Press any key to continue.")
            you.spot = "livingroom"

        break