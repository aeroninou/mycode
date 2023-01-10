#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""


# import module
import pyfiglet
import json

title = pyfiglet.figlet_format("RPG GAME")

#function to open text files of ascii art of snake 
def snake():
    with open("snake.txt", "r") as snake:
        for line in snake:
            print(line.rstrip("\n"))

#function to open text file of ascii art of potion
def potion():
    with open("potion.txt", "r") as potion:
        for line in potion:
            print(line.rstrip("\n"))

def key():
    with open("key.txt", "r") as key:
        for line in key:
            print(line.rstrip("\n"))

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print(title)
    print('''
        avoid the python and get the key 
    =========================================
    Commands:
      go [direction]   get [item]
    ''')

def showStatus():

    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print(f'{moves} moves done. You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    print('Lives left:', lives)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms

# a dictionary linking a room to other rooms
with open ("room.json", "r") as roomjson:
   rooms = json.load(roomjson)

'''
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Attic',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
             },
            'Garden' : {
                    'north' : 'Dining Room'
                },
            'Attic' : {
                    'south' : 'Hall',
                    'item'  : 'monster'
                }
          }
'''
# start the player in the Hall
currentRoom = 'Hall'

#count the number of moves
moves = 0

#3 lives for each player 
lives = 3

win = False

showInstructions()

# breaking this while loop means the game is over
while lives > 0:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)
    

    #if they type 'go' first
    if move[0] == 'go':

        #total moves
        moves += 1

        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :

        #total moves
        moves += 1

        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        #a monster has attacked you, if you still have lives youll continue or game end
        if lives > 0:
            lives -= 1
            snake()
            print(f'A python has got you... -1 life. You have {lives} lives!')
            continue
        else:
            break

    if 'potion' in inventory:
        potion()
        lives += 1
        print(f'You gained a 1 life with a potion. You now have {lives} lives!')
        continue
    
    if 'key' in inventory:
        key()
        continue
    
    if currentRoom == 'Garden' and 'key' in inventory:
        win = True
        break

if win == True:
    print(pyfiglet.figlet_format("YOU WON ! !"))
    key()
    print(f'You escaped the house in {moves} moves with the ultra rare key...')
else:
    print(pyfiglet.figlet_format("YOU LOSE ! !"))
    print(f'Got bit by the Python. {lives} left.')
