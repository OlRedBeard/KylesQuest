global player_ready
global game_on

bed_options = {'Wither':'Wither away in bed.','Scream':'Scream at the top of your lungs.','Look':'Look around the room.','Leave':'Get out of the bed.'}

def Bed(you):
    
    print("\n\n\n")
    print("You are laying in bed.\n")
    
    numbers = 1
    bed_options_list = []

    if you.hasphone == True and you.unlockedphone == False:
        bed_options['Unlock'] = "Unlock phone"

    if you.unlockedphone == True:
        if 'Unlock' in bed_options.keys():
            del bed_options['Unlock']
        bed_options['CheckPhone'] = "Check phone"

    if you.checkedphone == True:
        if 'CheckPhone' in bed_options.keys():
            del bed_options['CheckPhone']

    if you.checkedns == True:
        if 'Nightstand' in bed_options.keys():
            del bed_options['Nightstand']

    for key in bed_options.keys():
        bed_options_list.append(key)

    for value in bed_options.values():
        print(f'{numbers}) {value}')
        numbers += 1
        
    choice = 'b'
    while choice not in range(1-len(bed_options.values())):

        choice = input(f"\nWhat would you like to do? (1-{len(bed_options.values())}): ")
        choice = int(choice)

        if bed_options_list[choice - 1] == "Wither":
            print("\n\n\n")
            print("You do your best impression of a coma patient, and after some time, it seems to work!")
            print("You have successfully withered away! You are now dead!\n")
            input("Press any key to continue.")
            you.spot = "dead"
            you.situation = "Wither"

        elif bed_options_list[choice - 1] == "Scream":
            print("\n\n\n")
            print(f"{you.name} lets loose a shrill and ear-piercing scream that fills the apartment. The dogs in the courtyard outside begin howling along.")
            print("You hear people shouting expletives of various intensity. If nothing else you're making an impression on the neighbors.\n")
            input("Press any key to continue.")
            del bed_options['Scream']

        elif bed_options_list[choice -1] == "Look":
            print("\n\n\n")
            print("After taking a moment to marvel at the outright impressive number of cobwebs collected on the ceiling of the room you glance around at its contents.")
            print("You spot a full length mirror carefully adorned with stickers, a dresser with a collection of Monster cans lined up atop it, and a nightstand.\n")
            bed_options['Nightstand'] = "Check the nightstand"
            input("Press any key to continue.")
            del bed_options['Look']

        elif bed_options_list[choice -1] == "Nightstand":
            print("\n\n\n")
            print("You turn to investigate the items on the particle board nightstand that sits next to you.\n")
            input("Press any key to continue.")
            you.last_spot = "bed"
            you.spot = "nightstand"

        elif bed_options_list[choice -1] == "Leave":
            print("\n\n\n")
            print("You stand up from the bed, as your weight shifts the moving bed sheets unleash the trapped aroma of particulary pungent flatulence.")
            print(f"You are genuinely concerned about {you.name}'s diet.\n")
            input("Press any key to continue.")
            you.spot = "bedroom"
        
        elif bed_options_list[choice -1] == "Unlock":
            print("\n\n\n")
            print(f"You look at the lock screen of {you.name}'s phone. The unfilled dots indicate a four-digit password is required to unlock it.")
            print(f"Four digits can't be that hard to crack, could it?\n")
            input("Press any key to continue.")
            you.last_spot = "bed"
            you.spot = "phone"

        elif bed_options_list[choice -1] == 'CheckPhone':
            print("\n\n\n")
            print(f"You decide to have another look at {you.name}'s phone.\n")
            input("Press any key to continue.")
            you.last_spot = "bed"
            you.spot = "phone"

        break

bedroom_options = {"Look":"Look around the bedroom.","Bed":"Crawl back into bed.","Leave":"Leave the bedroom."}

def Bedroom(you):

    print("\n\n\n")
    print(f"You stand in a small bedroom, your feet instinctively begin to itch as whatever debris is in the carpet rubs against {you.name}'s bare feet.")
    print(f"It would seem that if {you.name} even owns a vaccuum it is entirely for show.\n")

    numbers = 1
    bedroom_options_list = []

    if you.hasphone == True and you.unlockedphone == False:
        bedroom_options["Unlock"] = "Unlock phone"

    if you.unlockedphone == True:
        if 'Unlock' in bedroom_options.keys():
            del bedroom_options['Unlock']
        bedroom_options['CheckPhone'] = "Check phone"

    if you.checkedphone == True:
        if 'CheckPhone' in bedroom_options.keys():
            del bedroom_options['CheckPhone']

    if you.checkedns == True:
        if 'Nightstand' in bedroom_options.keys():
            del bedroom_options['Nightstand']

    for key in bedroom_options.keys():
        bedroom_options_list.append(key)

    for value in bedroom_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(bedroom_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(bedroom_options.values())}): ")
        choice = int(choice)

        if you.checkeddresser == True:
            if 'Dresser' in bed_options.keys():
                del bed_options['Dresser']

        if bedroom_options_list[choice -1] == "Look":
            print("\n\n\n")
            print("In the room you spot a full length mirror with the frame plastered with various stickers sporting various beer & energy drink logos,")
            print("a dusty dresser with only the lineup of Monster cans breaking through the layers of dust and touching the wood, as well as a nightstand beside the bed.\n")
            input("Press any key to continue.")
            bedroom_options["Dresser"] = "Look in the dresser."
            bedroom_options["Mirror"] = "Look in the mirror"
            bedroom_options["Nightstand"] = "Check the nightstand"
            del bedroom_options['Look']

        elif bedroom_options_list[choice -1] == "Bed":
            print("\n\n\n")
            print("Debating between wandering further into the sea of filth and crawling back into the crusty, un-washed blankets, the latter somehow seems more appealing.")
            print(f"It seems {you.name} agrees with your assessment, and happily shuffles underneath the covers.\n")
            input("Press any key to continue.")
            you.spot = "bed"

        elif bedroom_options_list[choice -1] == "Leave":
            print("\n\n\n")
            print(f"Fed up of the musty, dusty bedroom you decide it's time to pilot {you.name} out into the rest of the apartment.")
            print("The door opens with a creak and you step out into the hallway.\n")
            input("Press any key to continue.")
            you.spot = "hallway"
        
        elif bedroom_options_list[choice -1] == "Dresser":
            print("\n\n\n")
            print(f"You walk to the dust-caked dresser adorned with the shells of fallen energy drinks. It's time to see what {you.name} keeps in these drawers.")
            print("(Don't take that out of context.)\n")
            input("Press any key to continue.")
            you.spot = "dresser"

        elif bedroom_options_list[choice -1] == "Mirror":
            print("\n\n\n")
            print(f"Walking up to the full length mirror, {you.name} immediately begins flexing their meager musculature and posing in front of the mirror.")
            print(f"It seems {you.name} is a bit like a parakeet: transfixed by their own reflection... And with similarly skinny legs.\n")
            input("Press any key to continue.")
            del bedroom_options['Mirror']
            

        elif bedroom_options_list[choice -1] == "Nightstand":
            print("\n\n\n")
            print("You walk over to the particle board nightstand next to the bed and have a look at its contents.\n")
            input("Press any key to continue.")
            you.last_spot = "bedroom"
            you.spot = "nightstand"      

        elif bedroom_options_list[choice -1] == "Unlock":
            print("\n\n\n")
            print(f"You look at the lock screen of {you.name}'s phone. The unfilled dots indicate a four-digit password is required to unlock it.")
            print(f"Four digits can't be that hard to crack, could it?\n")
            input("Press any key to continue.")
            you.last_spot = "bedroom"
            you.spot = "phone"

        elif bedroom_options_list[choice -1] == 'CheckPhone':
            print("\n\n\n")
            print(f"You decide to have another look at {you.name}'s phone.\n")
            input("Press any key to continue.")
            you.last_spot = "bedroom"
            you.spot = "phone"

        break

hallway_options = {'Bathroom':'Go into the bathroom.','Kitchen':'Head down to the kitchen.','LRoom':'Head out into the front room.','Bedroom':'Head back to the bedroom'}

def Hallway(you):

    print("\n\n\n")
    print("Much like the bedroom, you get the impression that, to the dust bunnies in the hall carpet, a vaccuum is a mythical creature made up to scare their children.")
    print(f"You also notice the series of fist-sized holes in the wall, upon noticing them it feels like {you.name} is oddly proud of themself.\n")

    numbers = 1
    hallway_options_list = []

    if you.hasphone == True and you.unlockedphone == False:
        hallway_options["Unlock"] = "Unlock phone"

    if you.unlockedphone == True:
        if 'Unlock' in hallway_options.keys():
            del hallway_options['Unlock']
        hallway_options['CheckPhone'] = "Check phone"

    if you.checkedphone == True:
        if 'CheckPhone' in hallway_options.keys():
            del hallway_options['CheckPhone']

    for key in hallway_options.keys():
        hallway_options_list.append(key)

    for value in hallway_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(hallway_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(hallway_options.values())}): ")
        choice = int(choice)

        if hallway_options_list[choice -1] == "Bathroom":
            print("\n\n\n")
            print(f"You decide to steer {you.name} towards the bathroom, not sure whether you're more curious or terrified about the state it will be in.\n")
            input("Press any key to continue.")
            you.spot = "bathroom"

        elif hallway_options_list[choice -1] == "Kitchen":
            print("\n\n\n")
            print("You feel as though (if you were in your own body) the hairs on the back of your neck would be standing up as you walk down the hallway toward the kitchen.")
            print(f"Given the state of cleanliness you've seen so far you cannot imagine the biological horrors that await in the kitchen.\n")
            input("Press any key to continue.")
            you.spot = "kitchen"

        elif hallway_options_list[choice -1] == "LRoom":
            print("\n\n\n")
            print(f"Piloting {you.name} down the hallway and past the kitchen, you try not to make direct eye-contact with the filth as you hurry to the front room.")
            print("You pretend the crunching sounds beneath your feet are fallen leaves rather than bits of food and toenail clippings.\n")
            input("Press any key to continue.")
            you.spot = "livingroom"

        elif hallway_options_list[choice -1] == "Bedroom":
            print("\n\n\n")
            print(f"Heading back to where you started it all, you pilot {you.name} back towards the bedroom.\n")
            input("Press any key to continue.")
            you.spot = "bedroom"

        elif hallway_options_list[choice -1] == "Unlock":
            print("\n\n\n")
            print(f"You look at the lock screen of {you.name}'s phone. The unfilled dots indicate a four-digit password is required to unlock it.")
            print(f"Four digits can't be that hard to crack, could it?\n")
            input("Press any key to continue.")
            you.last_spot = "hallway"
            you.spot = "phone"

        elif hallway_options_list[choice -1] == 'CheckPhone':
            print("\n\n\n")
            print(f"You decide to have another look at {you.name}'s phone.\n")
            input("Press any key to continue.")
            you.last_spot = "hallway"
            you.spot = "phone"

        break

bathroom_options = {'Look':'Look around the bathroom.','Leave':'Go back into the hallway.'}

def Bathroom(you):

    print("\n\n\n")
    print("Well, it certainly could've been worse. The bathroom has its own distinct aroma, an acrid perfumed smell. As though a fragrence counter from a")
    print(f"department store crawled in here to die. You stand in a small apartment bathroom.\n")

    numbers = 1
    bathroom_options_list = []

    if you.hasphone == True and you.unlockedphone == False:
        bathroom_options["Unlock"] = "Unlock phone"

    if you.unlockedphone == True:
        if 'Unlock' in bathroom_options.keys():
            del bathroom_options['Unlock']
        bathroom_options['CheckPhone'] = "Check phone"

    if you.checkedphone == True:
        if 'CheckPhone' in bathroom_options.keys():
            del bathroom_options['CheckPhone']

    for key in bathroom_options.keys():
        bathroom_options_list.append(key)

    for value in bathroom_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(bathroom_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(bathroom_options.values())}): ")
        choice = int(choice)

        if bathroom_options_list[choice -1] == "Look":
            print("\n\n\n")
            print("In the small bathroom you take immediate notice of the water-spot speckled mirror. At least you like to assume that it's water...")
            print("The countertop has a bone-dry toothbrush and a can of Axe body spray on top of it, the toilet seat is up leaving a clear view into the bowl, and a strangely")
            print("crusty towel is hung over a towel rack next to the shower.\n")
            input("Press any key to continue.")
            bathroom_options['Brush'] = 'Brush your teeth.'
            bathroom_options['Spray'] = 'Apply body spray.'
            bathroom_options['Shower'] = 'Take a shower.'
            del bathroom_options['Look']

        elif bathroom_options_list[choice -1] == "Leave":
            print("\n\n\n")
            print(f"You decide to exit the bathroom before you notice anything particularly disgusting and become compelled to try and convince {you.name} to vomit.\n")
            input("Press any key to continue.")
            you.spot = "hallway"

        elif bathroom_options_list[choice -1] == "Unlock":
            print("\n\n\n")
            print(f"You look at the lock screen of {you.name}'s phone. The unfilled dots indicate a four-digit password is required to unlock it.")
            print(f"Four digits can't be that hard to crack, could it?\n")
            input("Press any key to continue.")
            you.last_spot = "bathroom"
            you.spot = "phone"

        elif bathroom_options_list[choice -1] == "Brush":
            print("\n\n\n")
            print(f"Have you ever tried to brush a dog or cat's teeth? The physical recoil you see in {you.name}'s body language is very reminiscent of that experience.")
            print(f"After your best attempts to convince {you.name} to brush their teeth, you decide to let it go. Come to think of it, you don't remember seeing toothpaste...\n")
            input("Press any key to continue.")
            del bathroom_options['Brush']

        elif bathroom_options_list[choice -1] == "Spray":
            print("\n\n\n")
            if you.spray == 0:
                print(f"With a level of enthusiasm you wish {you.name} would apply to housekeeping, you pop the top off the can of Axe and spray yourself from head to toe.")
                print("The bathroom's distinct aroma becomes more understandable as your nostrils sting with the scent.\n")
                input("Press any key to continue.")
                you.spray += 1
            elif you.spray > 0 and you.spray < 3:
                print(f"It would seem that {you.name} has never under heard the concept of 'too much of a good thing.' Or a bad thing, for that matter...")
                print("You grab the can of Axe and douse yourself once more.")
                input("Press any key to continue.")
                you.spray += 1
            elif you.spray >= 3:
                print(f"With a seemingly diminished level of enthusiasm, {you.name} sprays another hearty dose of perfumed garbage onto their body and begins to cough.")
                print(f"The coughing begins to quicken in place, and {you.name} struggles to breathe, you can feel your legs trembling as you hack and choke.\n")
                print(f"Suddenly, {you.name} slips on the dirty linoleum floor, cracking their head on the countertop on their expeditious trip to the floor.")
                print(f"Your vision fades to a white nothingness, it seems that {you.name} has died unceremoneously on the bathroom floor.\n")
                input("Press any key to continue.")
                you.spot = "dead"
                you.situation = "Axe"

        elif bathroom_options_list[choice -1] == "Shower":
            print("\n\n\n")
            if you.clean == True:
                print(f"As shocking as it may seem based on the environment you're surrounded with, {you.name} is actually completely clean and has no need to shower again.\n")
                input("Press any key to continue.")
            elif you.clean == False and you.clothed == False:
                print(f"With all the trepidition of a cow being lead to slaughter, {you.name} cautiously enters the shower and turns on the taps.\n")
                input("Press any key to continue.")
                you.spot = "shower"
            elif you.clean == False and you.clothed == True:
                print(f"Rather than get your clothes wet, you decide to have {you.name} disrobe and toss their outfit on the floor before entering the shower.\n")
                input("Press any key to continue.")
                you.clothed = False
                bathroom_options['Redress'] = 'Put your clothes back on.'
                you.spot = "shower"

        elif bathroom_options_list[choice -1] == 'CheckPhone':
            print("\n\n\n")
            print(f"You decide to have another look at {you.name}'s phone.\n")
            input("Press any key to continue.")
            you.last_spot = "bathroom"
            you.spot = "phone"

        elif bathroom_options_list[choice -1] ==  "Redress":
            print("\n\n\n")
            print(f"You pick up {you.name}'s clothes from the floor and dress yourself once more. Being clean and clothed has never felt like more of an accomplishment.\n")
            input("Press any key to continue.")
            you.clothed = True
            del bathroom_options['Redress']

        break

kitchen_options = {'Look':'Look around the kitchen.','Leave':'Go back into the hallway'}

def Kitchen(you):

    print("\n\n\n")
    print(f"As you've come to expect, it seems {you.name} isn't particularly fond of cleaning this room either. The humid smell of mold and decaying food stuffs stings")
    print("your nostrils and you feel like anyone not used to the aroma would begin reflexively gagging. You stand in a horribly aromatic kitchen.\n")

    numbers = 1
    kitchen_options_list = []

    if you.hasphone == True and you.unlockedphone == False:
        kitchen_options["Unlock"] = "Unlock phone"

    if you.unlockedphone == True:
        if 'Unlock' in kitchen_options.keys():
            del kitchen_options['Unlock']
        kitchen_options['CheckPhone'] = "Check phone"

    if you.checkedphone == True:
        if 'CheckPhone' in kitchen_options.keys():
            del kitchen_options['CheckPhone']

    if you.checkedcabinets == True:
        if 'Cabinets' in kitchen_options.keys():
            del kitchen_options['Cabinets']

    for key in kitchen_options.keys():
        kitchen_options_list.append(key)

    for value in kitchen_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(kitchen_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(kitchen_options.values())}): ")
        choice = int(choice)

        if kitchen_options_list[choice -1] == "Look":
            print("\n\n\n")
            print("The most apparent feature of this kitchen is the mountainous pile of dishes stacked in the sink that extends outwards covering most of the counter as")
            print("well as the stovetop. After mentally processing Mt. Filth, you notice a fairly standard apartment fridge, as well as several cabinets.\n")
            input("Press any key to continue.")
            kitchen_options['Dishes'] = 'Do the dishes.'
            kitchen_options['Fridge'] = 'Check the fridge.'
            kitchen_options['Cabinets'] = 'Search the cabinets.'
            del kitchen_options['Look']

        elif kitchen_options_list[choice -1] == "Leave":
            print("\n\n\n")
            print("The horrifying smell of the room alone is enough to make you regret coming in here, you head back into the hallway.\n")
            input("Press any key to continue.")
            you.spot = "hallway"

        elif kitchen_options_list[choice -1] == "Dishes":
            print("\n\n\n")
            print(f"As you approach the mound of dishes the smell becomes more and more overwhelming, even {you.name} seems disgusted which is a feat on its own.")
            print("Something deep within the pile moves, causing the dishes to clatter. Maybe it's not the best idea to go putting your hands in there...")
            print(f"Not to mention, nowhere surrounding the mountain of decay is a visible bottle of soap or a brush to clean the dishes with.\n")
            input("Press any key to continue.")
            del kitchen_options['Dishes']

        elif kitchen_options_list[choice -1] == "Fridge":
            print("\n\n\n")
            print(f"Sensing that perhaps {you.name} could use something to eat to start the day, you open the refridgerator.\n")
            input("Press any key to continue.")
            you.spot = "fridge"

        elif kitchen_options_list[choice -1] == "Cabinets":
            print("\n\n\n")
            print(f"It's probably a good idea to make sure that {you.name} eats today. You begin searching the cabinets in hopes of finding food.\n")
            input("Press any key to continue.")
            you.spot = "cabinets"

        elif kitchen_options_list[choice -1] == "Unlock":
            print("\n\n\n")
            print(f"You look at the lock screen of {you.name}'s phone. The unfilled dots indicate a four-digit password is required to unlock it.")
            print(f"Four digits can't be that hard to crack, could it?\n")
            input("Press any key to continue.")
            you.last_spot = "kitchen"
            you.spot = "phone"

        elif kitchen_options_list[choice -1] == 'CheckPhone':
            print("\n\n\n")
            print(f"You decide to have another look at {you.name}'s phone.\n")
            input("Press any key to continue.")
            you.last_spot = "kitchen"
            you.spot = "phone"

        break

livingroom_options = {'Look':'Look around the living room.','Leave':'Go back into the hallway.','Exit':'Leave the apartment.'}

def Livingroom(you):

    print("\n\n\n")
    print(f"Walking out into the front room you see that {you.name} has an even more impressive collection of Monster cans than you had previously thought.")
    print("The texture of the crunchy bits in the carpet changes slightly in this room, feeling more like jagged bits of chips poking your feet than petrified dust.")
    print("You are in a dusty living room with a door leading out of the apartment.\n")

    numbers = 1
    livingroom_options_list = []

    if you.hasphone == True and you.unlockedphone == False:
        livingroom_options["Unlock"] = "Unlock phone"

    if you.unlockedphone == True:
        if 'Unlock' in livingroom_options.keys():
            del livingroom_options['Unlock']
        livingroom_options['CheckPhone'] = "Check phone"

    if you.checkedphone == True:
        if 'CheckPhone' in livingroom_options.keys():
            del livingroom_options['CheckPhone']

    for key in livingroom_options.keys():
        livingroom_options_list.append(key)

    for value in livingroom_options.values():
        print(f'{numbers}) {value}')
        numbers += 1

    choice = "b"
    while choice not in range(1-len(livingroom_options.values())):
        choice = input(f"\nWhat would you like to do? (1-{len(livingroom_options.values())}): ")
        choice = int(choice)

        if livingroom_options_list[choice -1] == "Look":
            print("\n\n\n")
            print("Apart from the immediately apparent pyramid of cans, you spot a TV, an Xbox, a suspiciously stained futon, and a dusty coffee table.")
            print("By the door out of the apartment you spot a jacket hanging on a hook and a pair of sneaker.\n")
            input("Press any key to continue.")
            livingroom_options['Futon'] = 'Sit on the futon.'
            livingroom_options['Coffee'] = 'Check the coffee table.'
            livingroom_options['TV'] = 'Turn on the TV.'
            livingroom_options['Jacket'] = 'Check the jacket.'
            livingroom_options['Shoes'] = 'Put on shoes.'
            del livingroom_options['Look']

        elif livingroom_options_list[choice -1] == "Futon":
            print("\n\n\n")
            print("Doing your best to imagine non-disgusting reasons behind the myriad of stains, you sit down on the futon.\n")
            input("Press any key to continue.")
            you.spot = "futon"

        elif livingroom_options_list[choice -1] == "Coffee":
            print("\n\n\n")
            print(f"You rummage around in the various cans, wrappers and assorted debris that {you.name} decorates the coffee table with.")
            print("After awhile you manage to find a set of keys. You decide to take the keys with you, they're probably important.\n")
            input("Press any key to continue.")
            you.haskeys = True
            del livingroom_options['Coffee']

        elif livingroom_options_list[choice -1] == "TV":
            print("\n\n\n")
            print(f"You press the power button on the TV and see the Xbox menu screen. Pressing the button to change the source quickly lets you know that {you.name}")
            print("doesn't have cable. Too bad, you were hoping to catch some The Price is Right.\n")
            input("Press any key to continue.")
            del livingroom_options['TV']
            you.tvon = True

        elif livingroom_options_list[choice -1] == "Jacket":
            print("\n\n\n")
            print(f"Rummaging through the pockets of {you.name}'s (apparently) only jacket. You find a wallet containing an ID and a debit card. You decide to take it.")
            print(f"You also find a handful of miscellaneous wrappers crumpled and stuffed in pockets. At least {you.name} isn't a litter bug.\n")
            input("Press any key to continue.")
            you.haswallet = True
            del livingroom_options['Jacket']

        elif livingroom_options_list[choice -1] == "Shoes":
            print("\n\n\n")
            print(f"You head over to the shoes next to the door and slide {you.name}'s feet into them. Your feet are now thoroughly protected from the nightmarish")
            print("cavalcade of debris and detritus mixed into the carpet fibres.\n")
            input("Press any key to continue.")
            you.shoed = True
            del livingroom_options['Shoes']

        elif livingroom_options_list[choice -1] == "Leave":
            print("\n\n\n")
            print(f"You head out of the living room and back into the hallway.\n")
            input("Press any key to continue.")
            you.spot = "hallway"
        
        elif livingroom_options_list[choice -1] == "Exit":
            print("\n\n\n")
            print(f"You open the apartment door and immediately breathe in the freshest air you've encountered all day. You step out of {you.name}'s apartment.")
            print(f"The door swings closed behind you and you hear it lock. Well at least that's one thing that {you.name} can't neglect to do.\n")
            input("Press any key to continue.")
            you.spot = "outside"

        elif livingroom_options_list[choice -1] == "Unlock":
            print("\n\n\n")
            print(f"You look at the lock screen of {you.name}'s phone. The unfilled dots indicate a four-digit password is required to unlock it.")
            print(f"Four digits can't be that hard to crack, could it?\n")
            input("Press any key to continue.")
            you.last_spot = "livingroom"
            you.spot = "phone"

        elif livingroom_options_list[choice -1] == 'CheckPhone':
            print("\n\n\n")
            print(f"You decide to have another look at {you.name}'s phone.\n")
            input("Press any key to continue.")
            you.last_spot = "livingroom"
            you.spot = "phone"

        break