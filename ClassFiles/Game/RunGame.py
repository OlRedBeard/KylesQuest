from ClassFiles.Game import Room
from ClassFiles.Game import Object
from ClassFiles.Game import EndGame

global game_on

def playing(you):
    game_on = True
    while game_on:
        #room interactions
        if you.spot == "bed":
            Room.Bed(you)   
        elif you.spot == "bedroom":
            Room.Bedroom(you)   
        elif you.spot == "hallway":
            Room.Hallway(you)
        elif you.spot == "bathroom":
            Room.Bathroom(you)
        elif you.spot == "kitchen":
            Room.Kitchen(you)
        elif you.spot == "livingroom":
            Room.Livingroom(you)
        #object interactions       
        elif you.spot == "nightstand":
            Object.Nightstand(you)   
        elif you.spot == "phone":
            Object.Phone(you)
        elif you.spot == "dresser":
            Object.Dresser(you)
        elif you.spot == "shower":
            Object.Shower(you)
        elif you.spot == "fridge":
            Object.Fridge(you)
        elif you.spot == "cabinets":
            Object.Cabinets(you)
        elif you.spot == "futon":
            Object.Futon(you)
        #ending interactions
        elif you.spot == "dead":
            EndGame.YouDied(you)
        elif you.spot == "outside":
            EndGame.YouLeft(you)
        elif you.spot == "gaming":
            EndGame.YouGamed(you)
        #detect gameover
        elif you.spot == "gameover":
            game_on = False
