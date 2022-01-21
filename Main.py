from ClassFiles.Body import TheBody
from ClassFiles.Game import RunGame
from ClassFiles.Game import Room

print("\n\n\n")
print("You wake to the sound of an unfamiliar alarm clock. As you open your eyes you realize that it's happened again.")
print("You're piloting a body that is not your own, isn't it a pain when this happens?")
print("")
print("Well, I guess there's nothing to be done but try and make the best of it.\n")

game_start = 'b'
game_replay = 'b'

while game_start not in ['Y','N']:
    game_start = input('Are you ready to begin? (Y/N): ')
    game_start = game_start.upper()
    
    if game_start == 'Y':
        you = TheBody.WhoAmI()
        RunGame.playing(you)
    else:
        quit()
    break

while game_replay not in ['Y','N']:
    print("\n\n\n")
    game_replay = input('Would you like to play again? (Y/N): ')
    game_replay = game_replay.upper()

    if game_replay == 'Y':
        you = TheBody.WhoAmI()
        RunGame.playing(you)
        game_replay = 'b'
    else:
        quit()