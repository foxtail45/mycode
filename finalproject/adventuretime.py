#!/usr/bin/python3
import map
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Adventure Time
========
Commands:
  go [left]
  get [Grass Sword]
  look [map]
''')

def showStatus():
  #print the player's current status
  print('Find Jake and Defeat the Lich')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see ' + rooms[currentRoom]["item"])
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
  "Finns Room": {
    "down": "Living Room",
    "item": "Jake"
  },
  "Living Room": {
    "up": "Finns Room",
    "down": "Kitchen"
  },
  "Kitchen": {
    "left": "Restroom",
    "up": "Living Room",
    "down": "Outside"
  },
  "Restroom": {
    "right": "Kitchen",
    "item": "Grass Sword"
  },
  "Outside": {
    "up": "Kitchen"
  }
}

currentRoom = 'Kitchen'

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
    if "item" in rooms[currentRoom] and move[1].title() in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory.append(move[1].title())
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if move[0] == 'look' and move[1] == 'map' :
      print(map.treemap)
      
  if currentRoom == "Living Room" and 'Jake' not in inventory :
      print("Hey BMO! have you seen Jake?")
      print("I'm sorry Finn, I have not!")

  if currentRoom == "Living Room" and 'Jake' in inventory :
      print("I see you've found Jake! Now go beat Jeff!")

  if currentRoom == 'Outside' and 'Jake' in inventory and 'Grass Sword' in inventory:
    print('You defeated the Lich with the Grass Sword and Jake... YOU WIN!')
    break

  if currentRoom== "Outside":
    print("You are defeated by The Lich! THE END")
    break


