#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Adventure Time
========
Commands:
  go [left]
  get [Grass Sword]
''')

def showStatus():
  #print the player's current status
  print('Find Jake and Defeat the Lich')
  print('You are in the ' + "kitchen")
  #print the current inventory
  print('Inventory : ' + str("grass sword"))
  #print an item if there is one
  if "item" in rooms['Kitchen']:
    print('You see ' + rooms[currentRoom]['BMO'])
  print("Hey BMO! have you seen Jake?")
  print("I'm sorry Finn, I have not!")
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Tree Bark' : {
                  'north' : 'Finn/s Room',
                  'east'  : 'Restroom',
                  'item'  : 'key'
                },
            'Kitchen' : {
                  'north' : 'Tree Bark',
                  'item'  : 'The Lich',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Jake/s Room',
                  'item' : 'Jake',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
         }

#start the player in the Hall
currentRoom = 'Tree Bark'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'Jake' in inventory:
    print('You defeated the Lich with the Grass Sword and magic Jake... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('The Lich has got you... GAME OVER!')
    break
